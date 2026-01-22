"""
Main Agri-agent Streamlit Application
Run with: streamlit run main.py
"""
import streamlit as st
from config import STREAMLIT_CONFIG
import sys
import os

# Add src to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Configure Streamlit
st.set_page_config(
    page_title="Agri-agent",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom theme
st.markdown("""
    <style>
    .main {
        padding: 0rem 0rem;
    }
    .block-container {
        padding: 1rem 1rem 1rem 1rem;
        max-width: 1400px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

# Sidebar navigation
with st.sidebar:
    st.title("🌾 Agri-agent")
    st.markdown("---")
    
    st.markdown("### Navigation")
    
    # Navigation options
    nav_options = [
        "Home",
        "Disease Detection",
        "AI Assistant",
        "Report Portal",
        "Price Prediction",
        "Analytics Dashboard",
        "Collaboration"
    ]
    
    selected_page = st.radio(
        "Select Feature",
        options=nav_options,
        index=nav_options.index(st.session_state.current_page) if st.session_state.current_page in nav_options else 0,
        label_visibility="collapsed"
    )
    
    st.session_state.current_page = selected_page
    
    st.markdown("---")
    
    # User section
    with st.expander("👤 User Account", expanded=False):
        st.text_input("Username", value="farmer@agriagent.com")
        st.selectbox("Farm Location", ["Punjab", "Karnataka", "Maharashtra", "Uttar Pradesh"])
        st.metric("Farm Area", "50 hectares")
    
    st.markdown("---")
    
    # Information
    col1, col2 = st.columns(2)
    with col1:
        if st.button("❓ Help"):
            st.info("Visit our help center for more information")
    with col2:
        if st.button("⚙️ Settings"):
            st.info("Coming soon!")
    
    st.markdown("---")
    
    st.markdown("""
    ### About
    **Agri-agent** is an AI-powered platform for smart and sustainable agriculture.
    
    **Version**: 1.0.0  
    **Last Updated**: Jan 2024
    """)

# Route to selected page
try:
    if st.session_state.current_page == "Home":
        st.markdown("""
        # 🌾 Welcome to Agri-agent

        An AI-powered web platform for smart and sustainable agriculture offering:

        - 🔍 **Disease Detection** - PyTorch CNN for crop disease identification
        - 📋 **Report Portal** - Comprehensive crop and soil health reports
        - 💰 **Price Prediction** - Market price forecasting
        - 📈 **Analytics Dashboard** - Real-time farming insights
        - 👥 **Collaboration** - Connect with farming community

        Select a feature from the navigation menu on the left to get started.
        """)

        # Feature cards
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("🔍 **Disease Detection**\n\nIdentify crop diseases early using our PyTorch CNN model for better crop health.")

        with col2:
            st.info("📋 **Report Portal**\n\nCreate detailed health reports for your crops and soil conditions.")

        with col3:
            st.info("💰 **Price Prediction**\n\nMarket price forecasting to help you make informed selling decisions.")

        col4, col5 = st.columns(2)

        with col4:
            st.info("📈 **Analytics Dashboard**\n\nReal-time insights and comprehensive analytics for your farming operations.")

        with col5:
            st.info("👥 **Collaboration**\n\nConnect with other farmers and share knowledge in our farming community.")
    
    elif st.session_state.current_page == "Disease Detection":
        from src.pages_data.pages_4_disease_detection import main
        main()
    
    elif st.session_state.current_page == "AI Assistant":
        from src.pages_data.pages_9_ai_assistant import main
        main()
    
    elif st.session_state.current_page == "Report Portal":
        from src.pages_data.pages_8_report_portal import main
        main()
    
    elif st.session_state.current_page == "Price Prediction":
        from src.pages_data.pages_5_price_prediction import main
        main()
    
    elif st.session_state.current_page == "Analytics Dashboard":
        from src.pages_data.pages_6_analytics_dashboard import main
        main()
    
    elif st.session_state.current_page == "Collaboration":
        from src.pages_data.pages_7_collaboration import main
        main()

except ImportError as e:
    st.error(f"Error loading page: {str(e)}")
    st.info("Make sure all page modules are properly installed and configured.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.info("Please check the page implementation and try again.")

if __name__ == "__main__":
    pass
