import httpx
from primitives.base import BaseResource

class AttributesResource(BaseResource):
    @property
    def uri(self) -> str:
        return "digimon://attributes"

    @property
    def name(self) -> str:
        return "attributes"

    @property
    def description(self) -> str:
        return "Returns a list of all Digimon attributes."

    async def fetch(self) -> str:
        client = self.client or httpx.AsyncClient()
        try:
            response = await client.get(f"{self.base_url}/attribute")
            return str(response.json())
        finally:
            if not self.client:
                await client.aclose()


class TypesResource(BaseResource):
    @property
    def uri(self) -> str:
        return "digimon://types"

    @property
    def name(self) -> str:
        return "types"

    @property
    def description(self) -> str:
        return "Returns a list of all Digimon types."

    async def fetch(self) -> str:
        client = self.client or httpx.AsyncClient()
        try:
            response = await client.get(f"{self.base_url}/type")
            return str(response.json())
        finally:
            if not self.client:
                await client.aclose()
