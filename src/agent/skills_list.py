from typing import TypedDict, List


class Skill(TypedDict):
    """可以逐步披露给智能体的技能"""
    name: str  # 技能的唯一标识符
    description: str  # 显示在系统提示词中的简短描述
    content: str  # 包含详细指令的完整技能内容[4](@ref)


# 定义三个核心技能（未来可以 定义在任何配置文件中(skills.md(动态工具))）
SKILLS = [
    {
    "name": "trend_hunter",
    "description": "全网热点侦察：分析各大平台热搜，提供今天适合的小红书选题",
    "content": """# 技能：全网热点侦察

## 功能范围
- 必须调用实时工具获取当下热点
- 筛选出一个最具有爆款潜力的"小红书选题"

## 可用工具（均来自 hot_news MCP，按优先级排列）
- `get-weibo-trending`: 获取微博热搜榜（最贴近小红书用户圈层）
- `get-douyin-trending`: 获取抖音热搜榜（短视频趋势与小红书高度重合）
- `get-zhihu-trending`: 获取知乎热榜（深度话题，适合知识类选题）
- `get-toutiao-trending`: 获取今日头条热榜（覆盖面广，可交叉验证）

## 使用规范
1. 至少调用前两个工具（微博 + 抖音），交叉对比热点。
2. 综合数据后，独立选定 1 个具体的创作话题，不要询问用户。
3. 选题标准：话题热度高、有情绪共鸣、适合图文表达。"""
},
{
    "name": "xhs_creator",
    "description": "小红书爆款图文创作与发布：生成带Emoji的文案并直接发布或送入预发布队列",
    "content": """# 技能：小红书爆款创作与发布

## 功能范围
- 撰写极具"网感"的夸张标题和多Emoji的正文
- 调用自动化工具完成笔记发布

## 可用工具（均来自 xiaohongshu-automation MCP）
- `xiaohongshu_publish`: 发布内容到小红书，支持多张图片和富文本内容（主要发布工具）
- `xiaohongshu_search_notes`: 根据关键词搜索小红书笔记，获取相关内容的标题和链接（可用于参考爆款写法）
- `xiaohongshu_get_note_content`: 获取小红书笔记的详细内容，包括标题、作者、发布时间和正文内容
- `xiaohongshu_analyze_note`: 分析小红书笔记内容，提取关键信息、领域标签和内容质量评估
- `xiaohongshu_post_comment`: 向指定的小红书笔记发布评论（评论引流用）
- `xiaohongshu_reply_comments`: 批量回复小红书帖子评论，支持智能回复建议
- `xiaohongshu_get_comments`: 获取指定小红书帖子的评论信息，支持评论分析和统计
- `xiaohongshu_account_management`: 管理多个小红书账号，支持添加、删除、切换和查询账号状态
- `xiaohongshu_monitor`: 获取小红书自动化系统的监控状态和运行统计
- `xiaohongshu_timeout_diagnostic`: 诊断MCP服务和FastAPI后端的连接和超时问题

## 工作流程
1. 先用 `xiaohongshu_search_notes` 搜索同类话题的爆款笔记，参考其标题和写法。
2. 撰写标题（含emoji，夸张吸睛）和正文（分段、多emoji、口语化）。
3. 调用 `xiaohongshu_publish` 直接发布，不要询问用户确认。"""
}
]


