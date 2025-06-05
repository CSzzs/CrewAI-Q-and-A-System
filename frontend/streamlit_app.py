import streamlit as st
import requests
import json
import logging


# Configure logging for stereamlit_app
logging.basicConfig(
    level=logging.INFO,
    format = '%(asctime)s | %(name)s | %(message)s',
    handlers=[
        logging.FileHandler("streamlit_app.log"),
        logging.StreamHandler()
    ]
)

# Create logger for this module
logger = logging.getLogger(__name__)

# Configure streamlit page

st.set_page_config(
    page_title="CrewAI Q&A system",
    page_icon="🤖",
    layout= "wide"
)

logger.info("Streamlit app started")

# Main title
st.title("🤖 CrewAI Agentic Q&A System")
st.markdown("Ask any question and get comprehensive, well-formatted answers!")

# Creating two columns for better layout
col1, spacer, col2 = st.columns([3, 0.5, 1])

with col1:
    # input field for user question
    user_question = st.text_area(
        "Enter your question:",
        placeholder="Type your question here....",
        height=100
    )
    
    # Submit button
    button_clicked = st.button("🔍 Get Answer", type="primary")
    if button_clicked:
        logger.info(f"User clicked submit button with question: {user_question[:100]}...")
        if user_question.strip():
        # Show Loading spinner
            with st.spinner("Processing Your Question through our AI Agents..."):
                try:
                    logger.info("Making API Request to FastAPI backend...")
                    
                # Make API request to FastAPI Backend
                    response= requests.post(
                        "http://127.0.0.1:8000/ask/",
                        json={"question": user_question},
                        timeout=240
                )
                    logger.info(f"Api response status code:{response.status_code}")
                
                    if response.status_code == 200:
                        result = response.json()
                        answer = result["answer"]
                        
                        logger.info("Succesfully recevied answer from the API")
                    
                        # Dispalying the answer
                        st.success("✅ Answer received")
                        st.markdown("### 📝 Response:")
                        st.markdown(answer)
                
                    else:
                        error_detail = response.json().get('detail', 'Unknown error')
                        logger.error(f"API returned error status {response.status_code}: {error_detail}")
                        st.error(f"❌ Error: {error_detail}")
                    
                except requests.exceptions.ConnectionError as e:
                    logger.error(f"Connection error to FastAPI backend: {str(e)}")
                    st.error("❌ Connection Error: Make sure the FastAPI backend is running on http://127.0.0.1:8000")
                    
                except requests.exceptions.Timeout as e:
                    logger.error(f"Request timeout: {str(e)}")
                    st.error("❌ Timeout Error: The request took too long. Please try again.")
                    
                except Exception as e:
                    logger.error(f"Unexpected error in Streamlit app: {str(e)}", exc_info=True)
                    st.error(f"❌ Unexpected Error: {str(e)}")
    
        else:
            logger.warning("User submitted empty question")
            st.warning("⚠️ Please enter a question before submitting.")
                

with col2:
    st.markdown("### ℹ️ How This works:")
    st.markdown("""
    1. **🛡️ Safety Filter**: Checks for harmful content
    2. **🌐 Web Research**: Searches for relevant information
    3. **📋 Formatting**: Presents answers in clear format
    """)

# Footer
st.markdown("---")
st.markdown("*Powered by CrewAI, SeperDevTool, FastAPI, and Streamlit*")
st.markdown("*Built By CS*")      

logger.debug("Streamlit app layout completed")