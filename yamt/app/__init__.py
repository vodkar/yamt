from abc import ABC, abstractproperty


class AbstractSettings(ABC):
    @abstractproperty
    def threads_num(self):
        pass


class Settings(AbstractSettings):
    @property
    def threads_num(self):
        return 6


def get_settings() -> AbstractSettings:
    return Settings()
