from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __str__(self):
        pass