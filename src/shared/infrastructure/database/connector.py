import abc

import pandas as pd
import sqlalchemy
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from src.shared.infrastructure.environments.variables import db_url_value
from threading import Lock


class DeclarativeABCMeta(DeclarativeMeta, abc.ABCMeta):
    pass


Base = declarative_base(metaclass=DeclarativeABCMeta)
metadata = Base.metadata


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class SQLConnector(metaclass=SingletonMeta):
    action = None
    engine = None
    connection = None
    session = None

    def __init__(self, action):
        self.action = action
        self.engine = create_engine(url=db_url_value(),
                                    echo=True,
                                    pool_pre_ping=True,
                                    pool_recycle=3600,
                                    isolation_level="READ UNCOMMITTED")
        self.connection = self.engine.connect()
        session_maker = sessionmaker(bind=self.engine)
        self.session = session_maker()
        Base.metadata.create_all(self.engine)

    def __str__(self):
        return "Conexión establecida"

    def run_query(self, query):
        try:
            if query != "":
                return self.connection.execute(sqlalchemy.text(query))
            else:
                return None
        except Exception as e:
            print("Error: ", query, e)
            return None

    def run_pandas_query(self, query):
        try:
            if query != "":
                return pd.read_sql_query(sqlalchemy.text(query), con=self.connection)
            else:
                return None
        except Exception as e:
            print("Error: ", query, e)
            print('----------------------')
            return None

    def save_pandas_to_db_and_replace(self, dataframe, table, schema):
        dataframe.to_sql(name=table, schema=schema, index=False, con=self.engine, if_exists='replace',
                         method="multi")

    def save_pandas_to_database(self, dataframe, table, schema, output_columns, exists='append'):
        dataframe.to_sql(name=table, schema=schema,
                         if_exists=exists, index=False, con=self.connection, method="multi", dtype=output_columns)
