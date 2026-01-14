import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="GenAI Academic Mentor",
    page_icon="🎓",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ---------- DYNAMIC BACKGROUND ----------
def set_background(color):
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {color};
    }}
    .title {{
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1f2d3d;
    }}
    .subtitle {{
        text-align: center;
        font-size: 18px;
        color: #2c3e50;
    }}
    </style>
    """, unsafe_allow_html=True)

# ---------- WELCOME PAGE (PEARL) ----------
if st.session_state.page == "welcome":
    set_background("#f8f6f0")  # Pearl color

    st.markdown("<div class='title'>🎓 GenAI Academic Mentor</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Your personal AI learning companion</div><br>", unsafe_allow_html=True)

    st.markdown("### Hey there!👋 Welcome!")
    st.write( "Feeling confused? Stuck on a topic? No worries!") 
    st.write("I’m your AI mentor here to break things down, answer your questions, and make learning feel way less scary. Let’s do this! 💪✨")

    if st.button("🚀 Start Learning"):
        st.session_state.page = "app"
        st.rerun()

# ---------- MAIN APP PAGE (LACE) ----------
elif st.session_state.page == "app":
    set_background("#fff5ee")  # Lace color

    st.markdown("<div class='title'>✍️ Ask Your Question</div><br>", unsafe_allow_html=True)

    question = st.text_input(
        "Enter the topic or question you are confused about:"
    )

    if st.button("📘 Get Explanation"):
        if question != "":
            st.success("✅ Simple Explanation:")
            st.write("Let me explain this in an easy and clear way...")

            if "confuse" in question.lower() or "don't understand" in question.lower():
                st.warning("😟 You seem confused.")
                st.write("Let me explain more slowly with an example.")
        else:
            st.error("❌ Please enter a question.")

    if st.button("⬅️ Back to Welcome Page"):
        st.session_state.page = "welcome"
        st.rerun()
