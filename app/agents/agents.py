import os
from crewai import Agents
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load environemnt varibales
load_dotenv()

class CustomAgents:
    """Defining custom agents for the crew
    """
    
    # Initializing LLM configuration
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.serper_api_key = os.getenv("SERPER_API_KEY")
        
        if not self.openai_api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if not self.serper_api_key:
            raise ValueError("SERPER_API_KEY not found in environment variables")

    
