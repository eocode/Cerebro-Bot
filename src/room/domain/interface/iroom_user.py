from abc import ABCMeta, abstractmethod


class IRoomUser(metaclass=ABCMeta):
    @property
    @abstractmethod
    def id(self):
        pass

    @property
    @abstractmethod
    def user_id(self):
        pass

    @property
    @abstractmethod
    def room_id(self):
        pass

    @property
    @abstractmethod
    def end_date(self):
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
