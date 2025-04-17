import streamlit as st
import pandas as pd
import random
from datetime import datetime

quotes = [
    "You don’t have to be perfect, just consistent.",
    "Every time you resist, you rewrite your story.",
    "The pain of discipline is always less than the pain of regret.",
    "Small changes lead to big transformations.",
    "You're not failing – you're learning how to win."
]


st.set_page_config(page_title="Break the Habit Tracker", layout="centered")


st.title("🚫 Break the Habit: Self-Improvement Tracker")
st.markdown("<h2 style='font-size: 28px;'>Log your journey to quitting a bad habit. Reflect, grow, and win each day.</h2>", unsafe_allow_html=True)

st.markdown("""
    <style>
    .streamlit-expanderHeader, .streamlit-expanderContent {
        font-size: 30px;
    }
    .stTextInput, .stTextArea, .stSlider, .stRadio {
        font-size: 30px;
    }
    .stButton, .stFormSubmitButton {
        font-size: 30px;
    }
    .stMarkdown, .stCaption {
        font-size: 30px;
    }
    </style>
""", unsafe_allow_html=True)


with st.form("habit_form"):
    did_resist = st.radio("🛑 Did you resist the habit today?", ["Yes", "No"])
    trigger = st.text_input("⚠️ What triggered the urge?")
    response = st.text_area("💭 How did you respond?")
    feeling = st.text_area("🧠 How did you feel afterward?")
    plan = st.text_input("📌 What will you do differently next time?")
    submitted = st.form_submit_button("Log Today's Reflection")


if "habit_log" not in st.session_state:
    st.session_state.habit_log = []


if submitted and (trigger or response or feeling):
    log_entry = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Resisted": did_resist,
        "Trigger": trigger,
        "Response": response,
        "Feeling": feeling,
        "Next Time Plan": plan
    }
    st.session_state.habit_log.append(log_entry)
    st.success("✅ Entry logged successfully!")

    with st.expander("📌 View your logged reflection"):
        st.markdown(f"**🗓️ Date:** {log_entry['Date']}")
        st.markdown(f"**🛑 Resisted Habit:** {log_entry['Resisted']}")
        st.markdown(f"**⚠️ Trigger:** {log_entry['Trigger']}")
        st.markdown(f"**💭 Response:** {log_entry['Response']}")
        st.markdown(f"**🧠 Feeling After:** {log_entry['Feeling']}")
        st.markdown(f"**📌 Plan for Next Time:** {log_entry['Next Time Plan']}")

if st.session_state.habit_log:
    st.subheader("📘 Your Habit Journey")
    df = pd.DataFrame(st.session_state.habit_log)
    st.dataframe(df, use_container_width=True)

st.markdown("### 🌟 Encouraging Quote")
st.info(random.choice(quotes))

# --- Footer ---
st.markdown("---")
st.caption("Built with strength 💪 using Streamlit")
