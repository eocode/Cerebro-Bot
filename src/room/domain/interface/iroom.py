from abc import ABCMeta, abstractmethod


class IRoom(metaclass=ABCMeta):
    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def rooms(self):
        pass

    @property
    @abstractmethod
    def capacity(self):
        pass

    @property
    @abstractmethod
    def amount(self):
        pass

    @property
    @abstractmethod
    def home_id(self):
        pass

    @property
    @abstractmethod
    def bathroom(self):
        pass

    @property
    @abstractmethod
    def kitchen(self):
        pass

    @property
    @abstractmethod
    def patio(self):
        pass

    @property
    @abstractmethod
    def is_active(self):
        pass

    @property
    @abstractmethod
    def created_at(self):
        pass

    @property
    @abstractmethod
    def updated_at(self):
        pass
