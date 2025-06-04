from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os 
from app.crew.crew import get_crew_result

# Load encvironment varibale
load_dotenv()

#Initialzie FastAPI app
app = FastAPI(title="CrewAI Q&A System ")