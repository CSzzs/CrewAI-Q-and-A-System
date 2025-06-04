from crewai import Task
from agents import CustomAgents

class CustomTasks:
    """
    Custom tasks for the CrewAi Q&A System
    """
    
    def __init__(self):
        self.agents = CustomAgents()
        
    def filter_task(self, question:str):
        """
        Task to filter potentially harmful content from user input
        """
        return Task(
            description = f'''Review the following question for any self-harm or explicit content: "{question}"
                            If the question contain any reference to self-harm, suicide, violence,
                            explicit, sexual, content or other harmful material, respond with EXACTLY:
                            "I cannot answer question related to self-harm or explicit content. please ask something else"
                            
                            If the ask question is safe and appropriate, respond with the original question exactly as provided.
                            
                            Question to review: {question}''',
                            
            agent = self.agents.filter_agents(),
            expected_output="Either the polite refusal message or the original safe question."
        )
        
    def web_scrape_task(self, question: str):
        """
        Task to gather comprehensive information from the web
        """
        return Task(
            description = f'''Use SerperDevTool to search the web and gather comprehensive information
                                to answer the follwing question: {question}
                                
                                Search for current, reliabel information from multiple sources.
                                Provide a detailed, accurate answer based on the web search results.
                                Include specific facts, data, and examples where relevent.
                                
                                Question: {question}''',
            agent = self.agents.web_scrape_agent(),
            expected_output = "A comprehensive asnwer to the user's question based on web scraped data."
        )
        
    def fromat_answer_task(self, answer:str):
        """
        Task to formatthe answer into a professional, readable format
        """
        return Task(
            description=f''' Take the following answer and transform it into a clean, visually appealing, 
                             and highly readable Markdown format.
                             Your job is to enahance clarity and engagement while preserving the original meaning and context
                             
                             Format the answer using
                             - Bullet points for unordered items
                             - Numbered list for sequence
                             - Appropriate Bold text for emphasis
                             - Relevent emojis to match tone and content
                             - Clear section hedings if helpful
                             
                             Do not change the core factual content or meaning.
                             Do make the result attractive, fun to read, and easy to follow
                             
                             Answer to format: {answer}''',
            
            agent = self.agents.formatting_agent(),
            expected_output="A clean, eye-catching, emoji-enhanced, Markdown version of the original answer."
        )