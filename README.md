# CrewAI Agentic Q&A System

A comprehensive Q&A system built with CrewAI that features safety filtering, web scraping, and professional answer formatting. The system uses three specialized AI agents working together to provide safe, accurate, and well-formatted responses to user questions.

## 🎯 Project Overview

This agentic system processes user questions through three stages:

1. **🛡️ Safety Filter Agent**: Screens questions for self-harm or explicit content
2. **🌐 Web Scraper Agent**: Gathers comprehensive information from the web using SerperDevTool
3. **📋 Formatting Agent**: Presents answers in clear, professional markdown format

## 🏗️ Architecture

- **FastAPI Backend**: RESTful API for processing questions
- **Streamlit Frontend**: User-friendly web interface
- **CrewAI Framework**: Orchestrates the multi-agent workflow
- **Conditional Logic**: Ensures harmful content is filtered before processing

## 🚀 Setup Instructions

### 1. Clone and Setup Environment

```bash
# Clone the repository (if applicable)
git https://github.com/CSzzs/CrewAI-Q-and-A-System
cd to project created path

# Create virtual environment
uv venv --python=3.12 .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
uv add -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root and add your API keys:

```env
# Get your SERPER_API_KEY from https://serper.dev/
SERPER_API_KEY=your_actual_serper_api_key_here

# Get your OpenAI API key from https://platform.openai.com/
OPENAI_API_KEY=your_actual_openai_api_key_here

OPENAI_MODEL_NAME="add Your prefered Model"
```

**Important**: 
- Never commit your actual API keys to version control

## 🖥️ Running the Application

### Start the FastAPI Backend

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://127.0.0.1:8000`
- API Documentation: `http://127.0.0.1:8000/docs`

### Start the Streamlit Frontend

Open a new terminal window and run:

```bash
streamlit run frontend/streamlit_app.py
```

The web interface will be available at: `http://localhost:8501`

## 🤖 Agent Roles

### Filter Agent
- **Role**: Input Filter
- **Responsibility**: Screens user input for harmful content
- **Safety Feature**: Politely declines to answer inappropriate questions

### Web Scrape Agent  
- **Role**: Information Gatherer
- **Responsibility**: Searches the web using SerperDevTool
- **Capability**: Gathers comprehensive, up-to-date information

### Formatting Agent
- **Role**: Answer Formatter  
- **Responsibility**: Formats responses into professional markdown
- **Output**: Clear bullet points, numbered lists, and structured content

## 📝 Usage Example

1. Open the Streamlit interface at `http://localhost:8501`
2. Enter your question in the text area
3. Click "🔍 Get Answer"
4. The system will:
   - Filter your question for safety
   - Search the web for relevant information
   - Format the response professionally
   - Display the final answer

## 🛠️ API Endpoints

### POST `/ask/`
Process a user question through the CrewAI system.

**Request Body:**
```json
{
  "question": "Your question here"
}
```

**Response:**
```json
{
  "answer": "Formatted answer from the AI agents"
}
```

## 🔧 Troubleshooting

### Common Issues

1. **API Keys Not Working**
   - Verify your API keys are correctly set in the `.env` file
   - Ensure you have sufficient credits/quota for both APIs

2. **Connection Errors**
   - Make sure the FastAPI backend is running before starting Streamlit
   - Check that ports 8000 and 8501 are not blocked

3. **Module Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're using the correct virtual environment

### Getting Help

- Check the FastAPI docs at `http://127.0.0.1:8000/docs`
- Review the console output for detailed error messages
- Ensure all environment variables are properly configured

## 📦 Project Structure

```
app
   |-- __pycache__
   |   |-- main.cpython-312.pyc
   |-- agents
   |   |-- __init__.py
   |   |-- __pycache__
   |   |   |-- __init__.cpython-312.pyc
   |   |   |-- agents.cpython-312.pyc
   |   |-- agents.py
   |-- crew
   |   |-- __init__.py
   |   |-- __pycache__
   |   |   |-- __init__.cpython-312.pyc
   |   |   |-- crew.cpython-312.pyc
   |   |-- crew.py
   |-- main.py
   |-- tasks
   |   |-- __init__.py
   |   |-- __pycache__
   |   |   |-- __init__.cpython-312.pyc
   |   |   |-- tasks.cpython-312.pyc
   |   |-- tasks.py
frontend
   |-- __init__.py
   |-- streamlit_app.py
pyproject.toml
.env
requirements.txt
template.py
uv.lock
```

## 🔒 Security Notes

- The system includes built-in safety filtering
- API keys are stored securely in environment variables
- Harmful content is rejected at the filtering stage
- All web searches are conducted through legitimate APIs

## 📄 License

This project is provided as-is for educational and development purposes.
```