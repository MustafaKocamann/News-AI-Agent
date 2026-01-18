"""Agent definitions for the News AI Agent system.

This module defines two specialized AI agents:
1. Senior News Researcher - Discovers and analyzes healthcare AI news
2. Professional Writer - Creates blog content from research findings
"""

from crewai import Agent, LLM
import os
from .tools import tool

from dotenv import load_dotenv
load_dotenv()

# Configure LLM using CrewAI's LLM system with Groq
# Using llama-3.3-70b-versatile for fast, high-quality responses
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.3,  # Lower temperature for more consistent and focused outputs
    api_key=os.getenv("GROQ_API_KEY")
)

# Define the Senior News Researcher Agent
# Responsible for discovering and analyzing the most impactful AI healthcare news
researcher_agent = Agent(
    role = "Senior News Researcher",
    goal = "Find and analyze exactly 3 most impactful news stories about {topic}",
    verbose = True,
    memory = False,  # Disabled to reduce token usage
    backstory =(
        "Recognized as a leading authority in digital transformation and R&D "
        "intelligence, you serve as the primary architect of knowledge for this "
        "agentic workflow. You specialize in identifying the TOP 3 most significant "
        "breakthroughs in {topic}. Your expertise lies in filtering through noise "
        "to find only the most impactful stories. You analyze each news item's "
        "trajectory and potential to reshape industries. Your mindset is data-driven, "
        "focused, and concise - delivering quality over quantity."
    ),

    tools = [tool],  # SerperDevTool for web search
    llm = llm,
    max_iter = 3,  # Limit iterations to optimize token usage and avoid rate limits
    allowed_delegation = True  # Enable collaboration with other agents
)   

# Define the Professional Writer Agent
# Responsible for transforming research into engaging blog content
writer_agent = Agent(
    role = "Writer",
    goal = "Create a concise, compelling article featuring exactly 3 top news stories about {topic}",
    verbose = True,
    memory = False,  # Disabled to reduce token usage
    backstory=(
        "You are a world-class technology columnist and master storyteller, "
        "renowned for creating impactful, focused content. Your expertise lies in "
        "'Narrative Structuralism'—the ability to take 3 key news items and weave "
        "them into a cohesive, visionary blog post. You don't overwhelm readers with "
        "information; instead, you distill the TOP 3 most important developments into "
        "their most potent form. With an acute understanding of reader psychology, "
        "you craft concise content that informs and inspires. You present {topic} "
        "at the forefront of the global conversation."
    ),
    tools = [],  # No tools - writer uses only the research output to avoid extra API calls
    llm = llm,
    max_iter = 3,  # Limit iterations to optimize token usage
    allowed_delegation = True  # Enable collaboration with other agents
)