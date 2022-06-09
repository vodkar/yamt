from abc import ABC, abstractmethod
from typing import Callable


class Monad(ABC):
    @abstractmethod
    def bind(self, func: Callable):
        pass

    def __or__(self, func: Callable):
        return self.bind(func)
