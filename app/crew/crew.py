import os
import logging
from crewai import Crew, Process
from app.agents.agents import CustomAgents
from app.tasks.tasks import CustomTasks
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

#Coinfigure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('crewai_system.log'),
        logging.StreamHandler() 
    ]
)

# Creating the Logger for this module
logger = logging.getLogger(__name__)

def get_crew_result(question: str) -> str:
    """
    Main function that orchestrates the entire CrewAI process with conditional logic
    """
    try:
        # Initializing agents and tasks
        agents = CustomAgents()
        tasks = CustomTasks()
        
        # Running filter task to check for harmful content
        logger.info(f"🛡️ Filtering question: {question}")
        
        filter_task = tasks.filter_task(question)
        
        # Create a crew for filtering
        filter_crew = Crew(
            agents=[agents.filter_agent()],
            tasks=[filter_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Executing the filter task
        logger.info("Executing the filter task...")
        filter_result = filter_crew.kickoff()
        filter_output = str(filter_result).strip()
        
        logger.info(f"🔍 Filter result: {filter_output}")
        
        # Checking if the content was flagged as harmful
        refusal_message = "I cannot answer questions related to self-harm or explicit content. Please ask something else."
        
        if refusal_message in filter_output:
            logger.warning("⚠️ Question flagged as potentially harmful - returning refusal message")
            return refusal_message
        
        # If safe, proceed with web scraping and formatting
        logger.info("✅ Question passed the safety filter - Proceeding to web search and formatting")
        
        # Task for web scraping
        web_scrape_task = tasks.web_scrape_task(question)
        
        # Create a crew for web scraping
        web_crew = Crew(
            agents=[agents.web_scrape_agent()],
            tasks=[web_scrape_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Executing the web scraping
        logger.infr("Starting the web scraping task...")
        web_result = web_crew.kickoff()
        web_output = str(web_result).strip()
        
        logger.info(f"🌐 Web scraping completed")
        
        # Formatting and organizing the answer
        format_task = tasks.format_answer_task(web_output)  # Fixed typo here
        
        # Create crew for formatting
        format_crew = Crew(
            agents=[agents.formatting_agent()],
            tasks=[format_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute formatting
        logger.info("Starting the formatting task...")
        final_result = format_crew.kickoff()
        formatted_output = str(final_result).strip()
        
        logger.info(f"📋 Formatting and organizing completed")
        
        return formatted_output
    
    except Exception as e:
        error_message = f"An error occurred while processing your request: {str(e)}"
        logger.error(f"❌ Error: {error_message}")
        return error_message