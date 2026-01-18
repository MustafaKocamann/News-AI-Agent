"""Main orchestration module for the News AI Agent system.

This module defines the NewsAICrew class which coordinates the multi-agent workflow.
It manages the sequential execution of research and writing tasks.
"""

from crewai import Crew, Process
from .tasks import research_task, write_task
from .agents import researcher_agent, writer_agent

class NewsAICrew:
    """
    NewsAICrew orchestrator for managing AI agents and tasks.
    
    This class initializes and manages a crew of AI agents that work together
    to discover, analyze, and write about AI developments in healthcare.
    """
    
    def __init__(self):
        """Initialize the crew with agents and tasks."""
        self.crew = Crew(
            agents=[researcher_agent, writer_agent],
            tasks=[research_task, write_task],
            process=Process.sequential,  # Execute tasks one after another
        )
    
    def run(self, topic: str):
        """
        Execute the news analysis workflow for a given topic.
        
        Args:
            topic (str): The topic to analyze (e.g., "AI in healthcare")
            
        Returns:
            str: The final analysis result (blog post content)
        """
        result = self.crew.kickoff(inputs={"topic": topic})
        return result

# Execute when run as a script
if __name__ == "__main__":
    news_crew = NewsAICrew()
    result = news_crew.run("AI in healthcare")
    print(result)