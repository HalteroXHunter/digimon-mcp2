from fastmcp import FastMCP
import httpx

# Import our abstract classes
from primitives.resources.api_resources import AttributesResource, TypesResource
from primitives.tools.api_tools import DigimonInfoTool

# from tools.scraper_tools import fetch_digimon_resistances

# 1. Initialize the server
mcp = FastMCP("Digimon_Architect_Pro")

# Using a shared client for pooling benefits since we aren't using the registry pattern yet.
# We will pass this to our class instances
shared_client = httpx.AsyncClient()

# 2. Register Resources (Corrected Method)
attributes_resource = AttributesResource(client=shared_client)
@mcp.resource(attributes_resource.uri, name=attributes_resource.name, description=attributes_resource.description)
async def fetch_attributes() -> str:
    """Returns a list of all Digimon attributes."""
    return await attributes_resource.fetch()

types_resource = TypesResource(client=shared_client)
@mcp.resource(types_resource.uri, name=types_resource.name, description=types_resource.description)
async def fetch_types() -> str:
    """Returns a list of all Digimon types."""
    return await types_resource.fetch()

# 3. Register Tools (Corrected Method)
digimon_info_tool = DigimonInfoTool(client=shared_client)
@mcp.tool(name=digimon_info_tool.name, description=digimon_info_tool.description)
async def fetch_digimon_info(name: str) -> str:
    """Fetch general information about a specific Digimon by name."""
    return await digimon_info_tool.execute(name=name)

# mcp.tool(name="get_digimon_resistances")(fetch_digimon_resistances)

if __name__ == "__main__":
    # Run locally via stdio
    mcp.run()
