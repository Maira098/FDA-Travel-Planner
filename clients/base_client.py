from abc import ABC, abstractmethod
import logging

class AbstractAPIClient(ABC):
    """
    Abstract base class for all API clients.
    """

    @abstractmethod
    def fetch(self, *args, **kwargs):
        """
        Fetch data from an external API.
        """
        pass
