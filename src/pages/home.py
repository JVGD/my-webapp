import streamlit as st


def show_home():
    """Display the portfolio landing page"""

    # Header section
    st.title("🚀 Welcome to My Portfolio")
    st.markdown("---")

    # Hero section
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Hi, I'm [Your Name]")
        st.markdown("""
        **[Add your professional title/role here]**

        Welcome to my portfolio! I'm passionate about [your interests/expertise].
        Here you'll find some of my projects and experiments in [your field].

        🔧 **Skills & Technologies:**
        - Python, Machine Learning, Data Science
        - Streamlit, FastAPI, React
        - PyTorch, Transformers, NLP
        - [Add your other skills here]

        📫 **Connect with me:**
        - 📧 Email: [your.email@example.com]
        - 💼 LinkedIn: [Your LinkedIn Profile]
        - 🐙 GitHub: [Your GitHub Profile]
        - 🌐 Website: [Your Website]
        """)

    with col2:
        st.markdown(
            """
        <div style="text-align: center; padding: 20px;">
            <div style="width: 150px; height: 150px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 50%; margin: 0 auto; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 60px;">👨‍💻</span>
            </div>
            <p style="margin-top: 10px; font-style: italic;">Your Photo Here</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Projects section
    st.header("🔥 Featured Projects")

    # Project cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🔤 Tokenizers Demo
        Explore text tokenization with different models and see how text is processed.

        **Technologies:** Transformers, PyTorch, Streamlit

        💡 *Use the sidebar navigation to explore this demo!*
        """)

    with col2:
        st.markdown("""
        ### 🚧 Project 2 (Coming Soon)
        [Description of your next project]

        **Technologies:** [Technologies you'll use]
        """)
        st.button("Coming Soon", disabled=True, key="project2_btn")

    with col3:
        st.markdown("""
        ### 🚧 Project 3 (Coming Soon)
        [Description of another project]

        **Technologies:** [Technologies you'll use]
        """)
        st.button("Coming Soon", disabled=True, key="project3_btn")

    st.markdown("---")

    # About section
    st.header("📖 About Me")
    st.markdown("""
    [Add a more detailed description about yourself, your background, interests, and goals.
    This is where you can tell your story and what drives your passion for technology.]

    ### 🎯 Current Focus
    - [What you're currently working on or learning]
    - [Your current interests or goals]
    - [Technologies you're exploring]

    ### 🏆 Achievements
    - [Your notable achievements]
    - [Certifications or awards]
    - [Notable projects or contributions]
    """)

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #666;'>Built with ❤️ using Streamlit</div>", unsafe_allow_html=True
    )
