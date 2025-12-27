"""
CrewAI crew manager for orchestrating agents and tasks
"""
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from crew.agents import create_keyword_agent
from crew.tasks import create_keyword_task
from tools import creativity_tool
import os


class CrewManager:
    """Manages CrewAI crews and executes tasks"""
    
    def __init__(self, model: str = "gpt-4-turbo-preview", temperature: float = 0.9):
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.creativity_tool = creativity_tool
    
    def generate_keywords(
        self,
        topic_description: str,
        use_search: bool = True,
        creativity_level: str = "high"
    ) -> dict:
        """
        Generate keyword and word suggestions for a given topic
        
        Args:
            topic_description: Description of the topic/concept
            use_search: Whether to enable web search for trending keywords
            creativity_level: Level of creativity (low, medium, high)
        
        Returns:
            Dictionary with keyword suggestions and metadata
        """
        try:
            # Get creative suggestions using creativity tool
            creative_suggestions = self.creativity_tool.get_creative_suggestions(
                topic_description, 
                count=15
            )
            
            # Build backstory for the agent
            backstory = f"""
You are an expert in generating creative and relevant keywords and word suggestions.
Your specialties include:
- Understanding topic context and extracting key concepts
- Generating creative word variations and combinations
- Identifying trending and relevant keywords
- Creating memorable and impactful word suggestions
- Adapting creativity level based on requirements

Creativity Level: {creativity_level}
"""
            
            # Build task description
            task_description = f"""
Based on the following topic description: "{topic_description}"

Generate a comprehensive list of keyword and word suggestions. Include:
1. Core keywords that directly relate to the topic
2. Related keywords and synonyms
3. Creative variations and combinations
4. Industry-specific terminology (if applicable)
5. Trending keywords (if web search is enabled)

Consider these creative suggestions as inspiration:
- Variations: {', '.join(creative_suggestions.get('variations', [])[:5])}
- Combinations: {', '.join(creative_suggestions.get('combinations', [])[:5])}
- Styled words: {', '.join(creative_suggestions.get('styled', [])[:5])}
- Acronyms: {', '.join(creative_suggestions.get('acronyms', [])[:3])}
- Blends: {', '.join(creative_suggestions.get('blends', [])[:5])}

Format the output as a clear, organized list with categories.
"""
            
            # Create keyword agent
            agent = create_keyword_agent(
                llm=self.llm,
                goal="Generate the most relevant and creative keywords for the given topic",
                backstory=backstory,
                use_search=use_search
            )
            
            # Create task
            task = create_keyword_task(
                agent=agent,
                description=task_description,
                expected_output="A comprehensive, categorized list of keyword and word suggestions"
            )
            
            # Create and run crew
            crew = Crew(
                agents=[agent],
                tasks=[task],
                process=Process.sequential,
                verbose=True
            )
            
            result = crew.kickoff()
            
            return {
                "success": True,
                "keywords": str(result),
                "creative_suggestions": creative_suggestions,
                "topic": topic_description,
                "creativity_level": creativity_level,
                "search_enabled": use_search
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "topic": topic_description
            }
  
