import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "app/agents/__init__.py",
    "app/agents/agents.py",
    "app/tasks/__init__.py",
    "app/tasks/tasks.py",
    "app/crew/__init__.py",
    "app/crew/crew.py",
    "app/main.py",
    "frontend/__init__.py",
    "frontend/streamlit_app.py",
    ".env",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    # Create directory if needed (for subdirectories only)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')
    
    # Create the file (regardless of directory level)
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")