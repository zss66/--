

from crewai import Agent
from tools import tool_searcher, search, dalle_tool
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
import os


llm = ChatOpenAI(
    model="gpt-4o-mini",
)

# 创建一个研究员代理，用于寻找学术论文
paper_researcher = Agent(
    role="调研员",  # 角色
    goal="寻找关于【{topic}】的最新和最相关的学术论文",  # 目标
    verbose=True,  # 启用详细日志
    memory=True,  # 启用记忆功能
    backstory=(
        "你需要为话题搜索出最为相关的学术论文，这些论文将会为后续文章写作提供帮助"
    ),
    tools=[tool_searcher],  # 使用的工具
    llm=llm,  # 语言模型
    allow_delegation=True,  # 允许委托任务
)
