hot_news_mcp_server_config = {
    "transport": "sse",  # 注意：ModelScope 托管版通常使用 SSE 协议
    "url": "https://mcp.api-inference.modelscope.net/c40013eda8b94a/sse"
    }

xhs_mcp_server_config = {        # 小红书 - 本地服务，先启动再用
    "transport": "stdio",
    "command": "uvx",
    "args": ["--from", "xiaohongshu-automation", "xhs-mcp"],
    "env": {
        "FASTAPI_URL": "http://localhost:8000"  # 你实际跑在8000，保持不变
    }
}