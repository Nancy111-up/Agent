import asyncio
from agent.skills_agent import get_agent


async def main():
    agent = await get_agent()
    # 启动 agent，输入一条消息触发运行
    result = await agent.ainvoke({
        "messages": [{"role": "user", "content": "开始今天的运营"}]
    })
    print(result)

if __name__ == "__main__":
    asyncio.run(main())