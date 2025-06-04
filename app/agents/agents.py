import os
from crewai import Agent
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

    def filter_agent(self):
        """
        Agent responsible for filtering harmful contents
        """
        return Agent(
            role = 'Input Fiter',
            goal = 'Filter user inputs for self-harmor explicit content.',
            backstory = '''You are a helpful and responsible AI assitant that prioritizes safety.
                            You are designed to identify and politely decline to answer questions
                            related to self harm or explicit content.''',
            verbose = True,
            allow_delgation = False,
            
        )
        
    def web_scrape_agent(self):
        """
        Agent responsible for gathering information from the web
        """
        # Initialize SerperDevTool with API key
        serper_tool = SerperDevTool(api_key=self.serper_api_key)
        
        return Agent(
            role = 'Information Gatherer',
            goal = 'Web scrape information using SerperDevTool to answer user question comprehensively.',
            backstory = '''You are an expert at extracting relevent infromation from the web
                            to anwer user queries comprehensively. You use reliable source and
                            provide accutrate, most up-to-date information.''',
            verbose = True,
            allow_delegation = False,
        )

    def formatting_agent(self):
        """
        Agent responsible for fromatting the final answer with clean, eye catching markdown,
        including appropriate emojis, bullet points, and numbered lists.
        """
        return Agent(
            role = 'Markdown Formatting Expert',
            goal = 'Transform the answer into a clean engaging, and visually ppealing Markdown format     using emojis, bullet points, and numbered lists to maximize readability and user satisfaction.',
            backstory = '''You are sesonded markdown expert with a flair for design and user-friendly presentation.
                            Your speciality is transformin plain text into beautifully markdown that is easy on the eyes and attractive to read.
                            You are intuitively know which mojis to use to match the tone and content, and you use layout elements (like spacing and indentation) to produce well-balanced, polished outputs. 
                            You never alter the original meaning but enhance clarity and engagement.''',
            verbose = True,
            allow_delegation = False,
        )
        
