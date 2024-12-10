'''
Author: zss zjb520zll@gmail.com
Date: 2024-12-10 14:53:08
LastEditors: zss zjb520zll@gmail.com
LastEditTime: 2024-12-10 14:57:04
FilePath: /代码/crewai_init/crew.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from langsmith import traceable
from crewai import Crew, Process
from tasks import (
    research_papers_task,
 
)
from agents import (
    paper_researcher,

)
from dotenv import load_dotenv

load_dotenv()

# 初始化环境变量

# Forming the research and writing crew
crew = Crew(
    agents=[
        paper_researcher,

    ],
    tasks=[
        research_papers_task,
    ],
    process=Process.sequential,
)


# Function to run the crew and return the result
def run_crew(topic):
    result = crew.kickoff(inputs={"topic": topic})
    return result
