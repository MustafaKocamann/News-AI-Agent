"""Task definitions for the News AI Agent system.

This module defines the tasks assigned to each agent:
1. Research Task - Assigned to the Senior News Researcher
2. Writing Task - Assigned to the Professional Writer
"""

from crewai import Task
from .tools import tool
from .agents import researcher_agent, writer_agent

# Define the Research Task
# This task is focused on discovering and analyzing exactly 3 impactful news stories
research_task = Task(
  description=(
    "Find and analyze EXACTLY 3 most impactful news stories about {topic}. "
        "For each of the 3 news items, provide: "
        "1. Title & Source: Clear headline and credible source. "
        "2. Key Breakthrough: What makes this news significant? "
        "3. Impact Assessment: Brief analysis of market/technical impact. "
        "4. Risk Factors: Any challenges or limitations. "
        "Focus on QUALITY over QUANTITY - only the TOP 3 stories. "
        "Keep your analysis concise to avoid token limits."
    ),
    expected_output=(
        "A concise 'Executive Intelligence Briefing' with EXACTLY 3 news stories. "
        "Format: "
        "- Executive Summary (2-3 sentences). "
        "- Story 1: [Title, Source, Breakthrough, Impact, Risks]. "
        "- Story 2: [Title, Source, Breakthrough, Impact, Risks]. "
        "- Story 3: [Title, Source, Breakthrough, Impact, Risks]. "
        "- Brief Future Outlook (2-3 sentences). "
        "Keep it concise and actionable."
    ),
  tools=[tool],  # SerperDevTool for web search
  agent=researcher_agent,
)

# Define the Writing Task
# This task transforms the research findings into a professional blog post
write_task = Task(
  description=(
   "Transform the 3 news stories from the Researcher into a compelling, "
        "concise blog article about {topic}. Structure: "
        "1. Opening Hook: Engaging introduction (2-3 sentences). "
        "2. Story 1: Present the first breakthrough with impact analysis. "
        "3. Story 2: Present the second breakthrough with impact analysis. "
        "4. Story 3: Present the third breakthrough with impact analysis. "
        "5. Conclusion: Forward-looking perspective (2-3 sentences). "
        "Keep it focused and concise to avoid token limits."
    ),
    expected_output=(
        "A polished blog article in Markdown format featuring EXACTLY 3 news stories. "
        "Requirements: "
        "- Catchy H1 headline. "
        "- Brief intro paragraph. "
        "- 3 clearly separated sections (one for each story). "
        "- Each section: H2 headline + 2-3 paragraphs. "
        "- Brief conclusion paragraph. "
        "Total length: Concise and impactful (avoid lengthy analysis)."
    ),
  tools=[],  # No tools - writer uses only the research output
  agent=writer_agent,
  async_execution=False,  # Execute synchronously
  output_file='new-blog-post.md'  # Save output to file
)
