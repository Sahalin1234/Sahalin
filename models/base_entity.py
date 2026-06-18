from abc import ABC, abstractmethod

class BaseEntity(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
