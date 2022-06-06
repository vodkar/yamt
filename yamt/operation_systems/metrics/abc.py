from abc import ABC, abstractmethod

from .models import OSVersion


class OSVersionMetric(ABC):
    @abstractmethod
    async def get_os_version(self) -> OSVersion:
        pass
    
class SSHMetricManager(ABC):
    pass
