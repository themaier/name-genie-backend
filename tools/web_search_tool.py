"""
Web search tool for CrewAI agents using SerperDev API
"""
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

load_dotenv()


def get_web_search_tool():
    """
    Initialize and return a web search tool.
    Requires SERPER_API_KEY in environment variables.
    Get your API key from: https://serper.dev/
    """
    return SerperDevTool()


# Pre-configured search tool instance
web_search_tool = get_web_search_tool()
