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
            goal = 'Filter user inputs for self-harmor explicit and Piracy content.',
            backstory = '''You are a responsible AI assistant that prioritizes user safety.
                            You are trained to detect and block any user inputs related to self-harm,
                            suicide, explicit material, or piracy, regardless of how the question is framed.''',
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
            goal = 'Use SerperDevTool to search the web and provide direct, factual answers to user questions.',
            backstory = '''You are an expert information gatherer who uses web search to find current, 
                        reliable data and provides direct answers to user questions. You extract specific 
                        facts, statistics, rankings, and examples from your search results. You never 
                        explain your search methodology - you simply provide the factual answer the 
                        user is looking for. You focus on current, accurate information from trusted sources.''',
            tools=[serper_tool],
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
            goal = 'Transform factual answers into clean, engaging, and visually appealing Markdown format using emojis, bullet points, and numbered lists to maximize readability.',
            backstory = '''You are a seasoned markdown expert with a flair for design and user-friendly presentation.
                        Your specialty is transforming factual content into beautifully formatted markdown that is 
                        easy on the eyes and attractive to read. You preserve all original factual information 
                        while enhancing clarity and engagement through proper formatting, emojis, and layout. 
                        You never alter facts or turn content into methodology descriptions - you only improve 
                        the visual presentation of existing information.''',
            verbose = True,
            allow_delegation = False,
        )
        
