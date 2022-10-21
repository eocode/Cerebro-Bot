from abc import ABCMeta, abstractmethod


class IUser(metaclass=ABCMeta):
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
    def last_name(self):
        pass

    @property
    @abstractmethod
    def phone(self):
        pass

    @property
    @abstractmethod
    def username(self):
        pass

    @property
    @abstractmethod
    def home_id(self):
        pass

    @property
    @abstractmethod
    def is_verified(self):
        pass

    @property
    @abstractmethod
    def is_roomer(self):
        pass

    @property
    @abstractmethod
    def is_admin(self):
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
