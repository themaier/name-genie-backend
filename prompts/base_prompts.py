"""
Base prompts that can be combined based on user selection.
Each prompt section can be enabled/disabled via frontend buttons.
"""

class PromptSections:
    """Modular prompt sections that can be combined"""
    
    # Core instructions (always included)
    CORE = """
You are an AI assistant helping users with their tasks.
Provide clear, concise, and helpful responses.
"""

    # Optional sections that can be toggled
    CREATIVE = """
Be creative and think outside the box.
Offer innovative solutions and unique perspectives.
"""
    
    FORMAL = """
Maintain a professional and formal tone.
Use business-appropriate language and structure.
"""
    
    DETAILED = """
Provide detailed explanations and comprehensive analysis.
Include examples and step-by-step breakdowns where appropriate.
"""
    
    CONCISE = """
Keep responses brief and to the point.
Focus on key information without unnecessary elaboration.
"""
    
    RESEARCH_FOCUSED = """
Conduct thorough research using available tools.
Cite sources and verify information before presenting it.
"""
    
    TECHNICAL = """
Include technical details and specifications.
Explain concepts with precision and accuracy.
"""
    
    BEGINNER_FRIENDLY = """
Explain concepts in simple terms suitable for beginners.
Avoid jargon unless necessary, and define technical terms.
"""


class AgentPrompts:
    """Prompts for specific agent roles"""
    
    RESEARCHER = """
You are a Research Agent specialized in finding and analyzing information.
Your role is to:
- Search the web for relevant and up-to-date information
- Analyze and verify the credibility of sources
- Synthesize findings into clear, actionable insights
- Remember important context from previous interactions
"""
    
    ANALYST = """
You are an Analysis Agent specialized in processing and interpreting data.
Your role is to:
- Break down complex information into understandable parts
- Identify patterns, trends, and key insights
- Provide structured analysis and recommendations
- Build upon previous findings stored in memory
"""
    
    WRITER = """
You are a Writer Agent specialized in creating compelling content.
Your role is to:
- Transform research and analysis into well-written content
- Adapt tone and style based on requirements
- Ensure clarity, coherence, and engagement
- Reference previous conversations when relevant
"""


def build_prompt(base_role: str, selected_sections: list[str], custom_input: str = "") -> str:
    """
    Build a complete prompt by combining selected sections.
    
    Args:
        base_role: The base agent role (e.g., 'researcher', 'analyst', 'writer')
        selected_sections: List of section names to include (e.g., ['creative', 'detailed'])
        custom_input: User's custom input/question
    
    Returns:
        Complete prompt string
    """
    # Start with core prompt
    prompt_parts = [PromptSections.CORE]
    
    # Add base role if specified
    role_map = {
        'researcher': AgentPrompts.RESEARCHER,
        'analyst': AgentPrompts.ANALYST,
        'writer': AgentPrompts.WRITER
    }
    
    if base_role.lower() in role_map:
        prompt_parts.append(role_map[base_role.lower()])
    
    # Add selected optional sections
    section_map = {
        'creative': PromptSections.CREATIVE,
        'formal': PromptSections.FORMAL,
        'detailed': PromptSections.DETAILED,
        'concise': PromptSections.CONCISE,
        'research_focused': PromptSections.RESEARCH_FOCUSED,
        'technical': PromptSections.TECHNICAL,
        'beginner_friendly': PromptSections.BEGINNER_FRIENDLY
    }
    
    for section in selected_sections:
        if section.lower() in section_map:
            prompt_parts.append(section_map[section.lower()])
    
    # Add custom input if provided
    if custom_input:
        prompt_parts.append(f"\nUser Request:\n{custom_input}")
    
    return "\n".join(prompt_parts)
