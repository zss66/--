'''
Author: zss zjb520zll@gmail.com
Date: 2024-12-10 14:53:08
LastEditors: zss zjb520zll@gmail.com
LastEditTime: 2024-12-10 14:57:21
FilePath: /代码/crewai_init/tasks.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


from crewai import Task
from agents import (
    paper_researcher,
   
)

# 研究任务：寻找话题相关的论文
research_papers_task = Task(
    description=(
        "1.寻找关于【{topic}】的相关学术论文。\n"
        "2.这些论文应为该领域被引用次数较高的论文。\n"
        "3.总结每篇论文的关键发现及其相关性。\n"  # 任务描述
    ),
    expected_output="3篇关于【{topic}】的学术论文摘要。包含名称与出处链接",  # 预期输出
    agent=paper_researcher,  # 使用的代理
)
