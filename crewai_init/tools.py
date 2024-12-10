'''
Author: zss zjb520zll@gmail.com
Date: 2024-12-10 14:53:08
LastEditors: zss zjb520zll@gmail.com
LastEditTime: 2024-12-10 14:57:50
FilePath: /代码/crewai_init/tools.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from dotenv import load_dotenv

load_dotenv()
import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
from crewai_tools import SerperDevTool
from langchain_community.utilities import GoogleSerperAPIWrapper

# Initialize the tool for internet searching capabilities
tool_searcher = SerperDevTool()
from crewai_tools import tool

# # 创建 DuckDuckGoSearchAPIWrapper 实例，并设置搜索类型为 "images"
# from crewai_tools import DallETool

# dalle_tool = DallETool(model="dall-e-3", size="1024x1024", quality="standard", n=1)


from openai import OpenAI


@tool("img_generate")
def dalle_tool(prompt: str):
    """use dalle to generate images"""
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url

