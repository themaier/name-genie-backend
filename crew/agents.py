"""
CrewAI agents configuration
"""
from crewai import Agent
from tools import web_search_tool
from langchain_openai import ChatOpenAI


def create_keyword_agent(llm: ChatOpenAI, goal: str, backstory: str, use_search: bool = True) -> Agent:
    """
    Create a keyword suggestion agent specialized in generating creative word suggestions
    and keywords based on topic descriptions
    """
    tools_list = [web_search_tool] if use_search else []
    
    return Agent(
        role='Keyword & Word Suggestion Specialist',
        goal=goal,
        backstory=backstory,
        tools=tools_list,
        llm=llm,
        verbose=True,
        allow_delegation=False,
        memory=True
    )
