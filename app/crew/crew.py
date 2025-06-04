import os
from crewai import Crew, Process
from app.agents.agents import CustomAgents
from app.tasks.tasks import CustomTasks
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

def get_crew_result(question:str) -> str:
    """
    Main function that orchestrate the entire CrewAI process with conditionl logic
    """
    try:
        # Initializing agents and tasks
        agents = CustomAgents()
        tasks = CustomTasks()
        
        # Runing filter task to check for harmful content
        print(f"🛡️ Filtering question:{question}")
        
        filter_task = tasks.filter_task(question)
        
        #Create a crew for filtering
        filter_crew = Crew(
            agents=[agents.filter_agent()],
            tasks=[filter_task],
            process=Process.sequential,
            verbose=True
        )
        
        #Executing the filter task
        filter_result = filter_crew.kickoff()
        filter_output = str(filter_result).strip()
        
        print(f"🔍 Filter result: {filter_output}")
        
        #checking the content was flagges as harmful
        refusal_messge = "I cannot answer questions related to self-harm or explicit content. Please ask something else."
        
        if refusal_messge in filter_output:
            print("⚠️ Question flagged as potentially harmful - returning refusal message")
            return refusal_messge
        
        # if sage, proceed with web scraping and formatting
        print("✅ Question Passed the safety filter - Proceeding to web search and formatting")
        
        #Task for web scraping and formatting
        web_scrape_task = tasks.web_scrape_task(question)
        
        #Create a crew for webscraping
        web_crew = Crew(
            agents=[agents.web_scrape_agent()],
            tasks=[web_scrape_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Excuting the web scraping
        web_result = web_crew.kickoff()
        web_output = str (web_result).strip()
        
        print(f"🌐 Web scraping completed")
        
        #formatting and organizing the answer
        
        format_task = tasks.fromat_answer_task(web_output)
        
        # Create crew for formatting
        format_crew = Crew(
            agents=[agents.formatting_agent()],
            tasks=[format_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Execute Formatting
        final_result = format_crew.kickoff()
        formatted_output = str(final_result).strip()
        
        print(f"📋 Formatting and organizing completed")
        
        return formatted_output
    
    except Exception as e:
        error_message = f"An error occured while processing your request: {str(e)}"
        print(f"❌ Error: {error_message}")
        return error_message