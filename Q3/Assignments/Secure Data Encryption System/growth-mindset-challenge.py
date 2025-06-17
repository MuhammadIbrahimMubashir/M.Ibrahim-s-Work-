import streamlit as st

# Initialize session state for counting users (no file needed)
if "challenge_count" not in st.session_state:
    st.session_state.challenge_count = 0

# --- Title and Header ---
st.title("🌱 Growth Mindset Challenge")
st.subheader("Believe in your ability to grow and improve!")

# --- What is Growth Mindset ---
st.markdown("""
### 💭 What is a Growth Mindset?

A **growth mindset** means believing that your intelligence and skills can be developed through effort and learning.
It’s okay to make mistakes. Every mistake helps you grow.

**Dr. Carol Dweck** shared this idea.
""")

# --- Why Adopt It ---
st.markdown("""
### 💪 Why Should You Have a Growth Mindset?

- ✅ Embrace challenges  
- ✅ Learn from mistakes  
- ✅ Keep trying when things are tough  
- ✅ Celebrate your effort, not just results  
- ✅ Stay open to feedback  
""")

# --- How to Practice It ---
st.markdown("""
### 🧠 How Can You Practice a Growth Mindset?

- 🎯 Set learning goals  
- ✍️ Reflect on your learning  
- 🗣️ Accept feedback  
- 😊 Stay positive and keep improving!  
""")

# --- Challenge Section ---
st.markdown("## 🎉 Ready to Accept the Challenge?")
accept = st.checkbox("Yes, I accept the Growth Mindset Challenge!")

if accept:
    st.success("Awesome! You’re on your way to becoming a better learner! 🚀")

    # Ask for user's goal this week
    goal = st.text_input("🌟 What will you do this week with a growth mindset?")

    if goal:
        st.write(f"✅ Great! Your goal: **{goal}**. Keep going! 💪")

    # Increment the session-based counter
    if "submitted" not in st.session_state:
        st.session_state.challenge_count += 1
        st.session_state.submitted = True

    st.info(f"📈 Total students accepted the challenge (this session): **{st.session_state.challenge_count}**")

# --- Footer ---
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit by Muhammad Ibrahim Mubashir")
