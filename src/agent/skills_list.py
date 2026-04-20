from typing import TypedDict, List


class Skill(TypedDict):
    """可以逐步披露给智能体的技能"""
    name: str  # 技能的唯一标识符
    description: str  # 显示在系统提示词中的简短描述
    content: str  # 包含详细指令的完整技能内容[4](@ref)


# 定义三个核心技能（未来可以 定义在任何配置文件中(skills.md(动态工具))）
SKILLS = [
    {
        "name": "gaode_navigation",
        "description": "高德地图服务：查询天气、地图信息、查询各种地址和规划行程路线",
        "content": """# 高德地图导航技能

## 功能范围
- 实时天气查询：获取指定位置的天气状况
- 地图信息查询：搜索地点、POI信息
- 路线规划：驾车、步行、公交路线规划
- 地理编码：地址与坐标互相转换
- 各种地址查询：包括酒店、加油站、餐馆和学校等各种地图上可查的地址标记

## 使用规范
1. 当用户询问天气、位置、路线时使用此技能
2. 需要明确具体的地理位置信息
3. 路线规划需提供起点和终点

## 部分工具说明
- weather_query: 查询天气信息
- map_search: 地图搜索
- route_planning: 路线规划
- geocoding: 地理编码转换"""
    },
    {
        "name": "railway_booking",
        "description": "12306铁路查询：查询火车站信息和火车票务",
        "content": """# 12306铁路查询技能

## 功能范围
- 车站查询：搜索火车站、高铁站信息
- 车票查询：查询火车、高铁班次和余票
- 票务服务：订票、退改签相关操作
- 时刻表查询：列车运行时刻信息

## 使用规范
1. 专门处理铁路交通相关查询
2. 需要明确出发地、目的地、日期等信息
3. 实时票务信息可能会有延迟

## 部分工具说明
- station_search: 车站信息查询
- ticket_query: 车票查询
- booking_management: 票务管理"""
    }

]


