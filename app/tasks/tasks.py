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