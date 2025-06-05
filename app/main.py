import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os 
from app.crew.crew import get_crew_result

# Load encvironment varibale
load_dotenv()

# create logger for this module
logger = logging.getLogger(__name__)

#Initialzie FastAPI app
app = FastAPI(title="CrewAI Q&A System", description="Agentic Q&A system with safety filtering")

class QuestionRequest(BaseModel):
    question:str
class AnswerResponse(BaseModel):
    answer: str
    
@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "CrewAI Q&A System API is running"}

@app.post("/ask/", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
    Endpoint to process user question throughthe CrewAI system
    """
    try:
        logger.info(f"Recived Question: {request.question[:100]}...")
        
        if not request.question.strip():
            logger.warning("Empty question received")
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Process question Through crewai
        logger.info("Processing question through CrewAI system...")
        result = get_crew_result(request.question)
        
        logger.info("Question processed successfully")
        return AnswerResponse(answer=result)
    
    except Exception as e:
        logger.error(f"Unexpected error processing question: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error Processing question: {str(e)}")
    
if __name__ == "__main__":
    import uvicorn
    logger.info("Starting FastAPI server...")
    uvicorn.run(app,host="0.0.0.0", port=8000)    