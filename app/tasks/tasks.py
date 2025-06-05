from crewai import Task
from app.agents.agents import CustomAgents

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
            description = f'''Review the following question for any self-harm, explicit or piracy related content: "{question}"
                            If the question contain any reference to self-harm, suicide, violence,
                            explicit,piracy, sexual, content or other harmful material, respond with EXACTLY:
                            "I cannot answer question related to self-harm or explicit content. please ask something else"
                            
                            If the ask question is safe and appropriate, respond with the original question exactly as provided.
                            
                            Question to review: {question}''',
                            
            agent = self.agents.filter_agent(),
            expected_output="Either the polite refusal message or the original safe question."
        )
        
    def web_scrape_task(self, question: str):
        """
        Task to gather comprehensive information from the web
        """
        return Task(
            description = f'''Search the web using SerperDevTool to find current, reliable information 
                           that directly answers this question: "{question}"
                           
                           IMPORTANT: You must provide the ACTUAL ANSWER to the question, not a description 
                           of how you would find the answer.
                           
                           Steps to follow:
                           1. Use SerperDevTool to search for relevant information
                           2. Extract specific facts, data, statistics, and examples from the search results
                           3. Compile these findings into a direct, comprehensive answer
                           4. Include specific details like rankings, percentages, names, dates where applicable
                           5. Use multiple reliable sources to ensure accuracy
                           
                           DO NOT explain your methodology or how you search.
                           DO provide the actual factual answer based on your web search results.
                           
                           Question: {question}''',
            agent = self.agents.web_scrape_agent(),
            expected_output = "A comprehensive asnwer to the user's question based on web scraped data."
        )
        
    def format_answer_task(self, answer:str):
        """
        Task to formatthe answer into a professional, readable format
        """
        return Task(
            description=f'''Transform the following factual answer into clean, visually appealing Markdown format.
                           
                           IMPORTANT: The content you're formatting contains the actual answer to the user's question.
                           Your job is to make it more readable and engaging, NOT to change it into a methodology description.
                           
                           Formatting guidelines:
                           - Use bullet points for lists of items
                           - Use numbered lists for rankings or sequences  
                           - Add appropriate emojis to match the content
                           - Use bold text for emphasis on key points
                           - Add clear section headings if helpful
                           - Ensure proper spacing and indentation
                           
                           PRESERVE all factual content, data, statistics, and specific information.
                           DO NOT turn this into a description of how to find information.
                           DO make it visually appealing and easy to read.
                           
                           Answer to format: {answer}''',
            
            agent = self.agents.formatting_agent(),
            expected_output="A clean, eye-catching, emoji-enhanced, Markdown version of the original answer."
        )