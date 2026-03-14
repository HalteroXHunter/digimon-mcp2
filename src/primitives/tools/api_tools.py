import httpx
from primitives.base import BaseTool

class DigimonInfoTool(BaseTool):
    @property
    def name(self) -> str:
        return "get_digimon_info"
        
    @property
    def description(self) -> str:
        return "Fetch general information about a specific Digimon by name."

    async def execute(self, name: str) -> str:
        client = self.client or httpx.AsyncClient()
        try:
            response = await client.get(f"{self.base_url}/digimon/{name.lower()}")
            if response.status_code == 200:
                return str(response.json())
            return f"Could not find Digimon: {name}"
        finally:
            if not self.client:
                await client.aclose()
