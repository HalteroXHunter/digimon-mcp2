import asyncio

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            # "digimon": {
            #     "command": "uv",
            #     "args": [
            #         "run",
            #         "/code/mcp-servers/digimon-mcp2/src/server.py",
            #     ],
            #     "transport": "stdio",
            # },
            "remote_digimon": {
                "url": "https://digimon2.fastmcp.app/mcp",
                "transport": "http",
                "headers": {
                    "Authorization": "Bearer fmcp_MNTsdqK9D1XV37JX5DQqTy88ETB71YRajYWKpOoN8rM"
                },
            }
        }
    )
    tools = await client.get_tools()

    agent = create_agent(
        model="gpt-4.1-mini",
        tools=tools,
        system_prompt="You are a helpful assistant.",
    )
    response = await agent.ainvoke(
        {
            "messages": [
                {"role": "user", "content": "what are the attributes for Agumon?"}
            ]
        }
    )

    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
