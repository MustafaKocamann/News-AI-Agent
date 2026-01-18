"""Tool configuration for the News AI Agent system.

This module sets up the SerperDevTool for web search functionality.
The tool is optimized to return only 3 results to minimize token usage.
"""

from dotenv import load_dotenv
load_dotenv()

import os

# Set up the Serper API key from environment variables
# Handles both local .env and Streamlit Cloud secrets
serper_key = os.getenv("SERPER_API_KEY")
if not serper_key:
    try:
        import streamlit as st
        serper_key = st.secrets.get("SERPER_API_KEY")
    except:
        pass

if serper_key:
    os.environ["SERPER_API_KEY"] = serper_key

from crewai_tools import SerperDevTool

# Configure SerperDevTool with result limit
# n_results=3 limits search results to reduce token consumption and avoid rate limits
tool = SerperDevTool(n_results=3)