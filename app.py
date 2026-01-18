"""
Streamlit application for AI Healthcare News Agent.

This is the main web interface that allows users to discover and analyze
the latest AI developments in healthcare through an intuitive UI.
"""

import streamlit as st
import sys
from pathlib import Path
import time

# Add the crew module to the Python path
sys.path.append(str(Path(__file__).parent))
from crew.crew import NewsAICrew

# Configure the Streamlit page
st.set_page_config(
    page_title="AI Healthcare News 🏥",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional design with gradient themes
st.markdown("""
    <style>
    /* Main theme colors with gradient background */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Başlık stilleri */
    .big-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: gradient 3s ease infinite;
    }
    
    .subtitle {
        text-align: center;
        color: #e0e0e0;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Button stilleri */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea22 0%, #764ba222 100%);
    }
    
    /* Alert boxes */
    .success-box {
        background: rgba(40, 167, 69, 0.2);
        color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .info-box {
        background: rgba(23, 162, 184, 0.2);
        color: #d1ecf1;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #17a2b8;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    /* Markdown content container */
    .markdown-content {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    
    /* Animasyonlar */
    @keyframes gradient {
        0% { filter: hue-rotate(0deg); }
        50% { filter: hue-rotate(20deg); }
        100% { filter: hue-rotate(0deg); }
    }
    </style>
""", unsafe_allow_html=True)

# Page header and subtitle
st.markdown('<h1 class="big-title">🏥 AI Healthcare News Agent</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover the latest AI developments in healthcare</p>', unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.markdown("## ⚙️ About")
    st.markdown("---")
    
    st.markdown("""
    ### 🏥 AI Healthcare News
    
    Intelligent news agent that automatically analyzes 
    AI developments in the healthcare sector.
    """)
    
    st.markdown("---")
    st.markdown("### 📊 Statistics")
    
    # Initialize session state for tracking analyses
    if 'total_analyses' not in st.session_state:
        st.session_state.total_analyses = 0
    
    # Display statistics metrics
    st.metric("Total Analysis", st.session_state.total_analyses)
    st.metric("Active Agents", "2")
    st.metric("News Count", "3")
    
    st.markdown("---")
    st.markdown("""
    ### 🎯 Features
    - 🔍 AI-powered research
    - 📰 Top 3 latest news
    - 📝 Auto blog generation
    - ⚡ Fast results
    """)
## Main content area
col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.markdown("### 🎯 Get AI Healthcare News")
    
    # Fixed topic for healthcare AI news
    topic = "AI in healthcare"
    
    # Main action button
    if st.button("🚀 Get Latest News", use_container_width=True):
        # Initialize progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Stage 1: Initialize agents
            status_text.markdown('<div class="info-box">🔍 Starting AI agents...</div>', unsafe_allow_html=True)
            progress_bar.progress(10)
            time.sleep(0.5)
            
            # Stage 2: Research phase
            status_text.markdown('<div class="info-box">📊 Scanning news sources...</div>', unsafe_allow_html=True)
            progress_bar.progress(30)
            
            # Initialize the News AI Crew
            news_crew = NewsAICrew()
            
            progress_bar.progress(40)
            status_text.markdown('<div class="info-box">🤖 AI agents working...</div>', unsafe_allow_html=True)
            
            # Execute the crew workflow
            result = news_crew.run(topic)
            
            progress_bar.progress(80)
            status_text.markdown('<div class="info-box">✍️ Generating blog post...</div>', unsafe_allow_html=True)
            time.sleep(0.5)
            
            # Stage 3: Complete
            progress_bar.progress(100)
            status_text.markdown('<div class="success-box">✅ Analysis completed!</div>', unsafe_allow_html=True)
            
            # Update statistics
            st.session_state.total_analyses += 1
            
            # Display results
            st.markdown("---")
            st.markdown("## 📰 Results")
            
            # Create tabs for different views
            tab1, tab2 = st.tabs(["📝 Blog Post", "📊 Analysis Summary"])
            
            with tab1:
                # Read and display the generated blog post
                blog_file = Path("crew/new-blog-post.md")
                if blog_file.exists():
                    with open(blog_file, 'r', encoding='utf-8') as f:
                        blog_content = f.read()
                    st.markdown(blog_content)
                    
                    # Provide download button for the blog post
                    st.download_button(
                        label="📥 Download Blog Post",
                        data=blog_content,
                        file_name="ai_healthcare_news.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                else:
                    st.markdown(result)
            
            with tab2:
                # Display analysis metadata and process details
                st.markdown("""
                ### 📊 Analysis Details
                
                **Topic:** AI in Healthcare
                
                **News Analyzed:** 3
                
                **AI Agents Used:**
                - 🔍 Senior News Researcher
                - ✍️ Professional Writer
                
                **Process:**
                1. ✅ News sources scanned
                2. ✅ Top 3 news selected
                3. ✅ Detailed analysis performed
                4. ✅ Blog format generated
                """)
            
        except Exception as e:
            # Handle and display any errors
            status_text.markdown(f'<div class="info-box" style="border-left-color: #dc3545;">❌ Error: {str(e)}</div>', unsafe_allow_html=True)
            st.error(f"An error occurred: {str(e)}")
            progress_bar.empty()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #e0e0e0; padding: 2rem;">
    <p>Powered by CrewAI & Groq 🚀 | Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)
