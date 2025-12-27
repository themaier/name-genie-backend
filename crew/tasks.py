"""
CrewAI tasks configuration
"""
from crewai import Task, Agent


def create_keyword_task(agent: Agent, description: str, expected_output: str) -> Task:
    """
    Create a keyword generation task
    """
    return Task(
        description=description,
        agent=agent,
        expected_output=expected_output
    )
