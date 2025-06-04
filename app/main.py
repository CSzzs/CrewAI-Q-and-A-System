from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os 
from app.crew.crew import get_crew_result

# Load encvironment varibale
load_dotenv()

#Initialzie FastAPI app
app = FastAPI(title="CrewAI Q&A System", description="Agentic Q&A system with safety filtering")

class QuestionRequest(BaseModel):
    question:str
class AnswerResponse(BaseModel):
    answer: str
    
@app.get("/")
def read_root():
    return {"message": "CrewAI Q&A System API is running"}

@app.post("/ask/", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    """
    Endpoint to process user question throughthe CrewAI system
    """
    try:
        if not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")
        
        # Process question Through crewai
        result = get_crew_result(request.question)
        
        return AnswerResponse(answer=result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error Processing question: {str(e)}")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8000)    