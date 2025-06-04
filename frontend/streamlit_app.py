import streamlit as st
import requests
import json

# Configure streamlit page

st.set_page_config(
    page_title="CrewAI Q&A system",
    page_icon="🤖",
    layout= "wide"
)

# Main title
st.title("🤖 CrewAI Agentic Q&A System")
st.markdown("Ask any question and get comprehensive, well-formatted answers!")

# Creating two columns for better layout
col1, col2 = st.columns([2, 1])

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
        if user_question.strip():
        # Show Loading spinner
            with st.spinner("Processing Your Question through our AI Agents..."):
                try:
                # Make API request to FastAPI Backend
                    response= requests.post(
                        "http://127.0.0.1:8000/ask/",
                        json={"question": user_question},
                        timeout=240
                )
                
                    if response.status_code == 200:
                        result = response.json()
                        answer = result["answer"]
                    
                        # Dispalying the answer
                        st.success("✅ Answer received")
                        st.markdown("### 📝 Response:")
                        st.markdown(answer)
                
                    else:
                        st.error(f"❌ Error: {response.json().get('detail', 'Unknown error')}")
                    
                except requests.exceptions.ConnectionError:
                    st.error("❌ Connection Error: Make sure the FastAPI backend is running on http://127.0.0.1:8000")
                except requests.exceptions.Timeout:
                    st.error("❌ Timeout Error: The request took too long. Please try again.")
                except Exception as e:
                    st.error(f"❌ Unexpected Error: {str(e)}")
    
    else:
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