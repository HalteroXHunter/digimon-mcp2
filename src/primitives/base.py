from abc import ABC, abstractmethod
import httpx

class BasePrimitive(ABC):
    """Base class for all MCP primitives."""
    def __init__(self, client: httpx.AsyncClient = None):
        self.client = client
        self.base_url = "https://digi-api.com/api/v1"

class BaseTool(BasePrimitive):
    """Abstract Base Class for an MCP Tool."""
    @property
    @abstractmethod
    def name(self) -> str:
        """The tool's registered name."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """Description for the LLM."""
        pass

    @abstractmethod
    async def execute(self, **kwargs) -> str:
        """Core execution logic."""
        pass

class BaseResource(BasePrimitive):
    """Abstract Base Class for an MCP Resource."""
    @property
    @abstractmethod
    def uri(self) -> str:
        """The URI for the resource."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Name of the resource."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """Description of the resource."""
        pass

    @abstractmethod
    async def fetch(self) -> str:
        """Core execution logic to fetch the resource."""
        pass
