import streamlit as st
import random

st.set_page_config(page_title="AI Skill Assessment Agent")

st.title("🤖 AI Skill Assessment & Learning Agent")

jd = st.text_area("📄 Paste Job Description")
resume = st.text_area("👤 Paste Resume")

if "skills" not in st.session_state:
    st.session_state.skills = []
if "questions" not in st.session_state:
    st.session_state.questions = []
if "answers" not in st.session_state:
    st.session_state.answers = []

# 🔹 Fake Skill Extraction
def extract_skills(jd):
    keywords = ["Python", "Java", "SQL", "Machine Learning", "AI", "Data Analysis", "React", "Communication", "Cloud"]
    found = [k for k in keywords if k.lower() in jd.lower()]
    return found if found else ["Python", "SQL", "Problem Solving"]

# 🔹 Fake Question Generator
def generate_questions(skills):
    return [f"Explain your experience with {skill}" for skill in skills[:3]]

# 🔹 Fake Evaluation
def evaluate_answer(answer):
    if len(answer) < 20:
        return "Score: 4/10\nReason: Answer is too short and lacks depth"
    elif len(answer) < 50:
        return "Score: 6/10\nReason: Basic understanding but needs improvement"
    else:
        return "Score: 8/10\nReason: Good explanation with clarity"

st.write("### ⚠️ Skill Gaps:")
st.write("- Improve depth in core concepts")
st.write("- Need more practical exposure")
st.write("- Strengthen problem-solving skills")

# 🔹 Fake Learning Plan
def learning_plan(skills):
    plan = ""
    for skill in skills:
        plan += f"""
**{skill}**
- Resources: YouTube (freeCodeCamp), Docs
- Time: 1-2 weeks
- Goal: Build mini project

"""
    return plan

# STEP 1
if st.button("🚀 Start Assessment"):

    if not jd.strip():
        st.warning("Please paste Job Description")
        st.stop()

    skills = extract_skills(jd)
    st.session_state.skills = skills

    st.write("### 🧠 Skills Identified:")
    for s in skills:
        st.write("-", s)

    questions = generate_questions(skills)
    st.session_state.questions = questions

# STEP 2
if st.session_state.questions:
    st.write("### 💬 Answer these questions:")

    for i, q in enumerate(st.session_state.questions):
        ans = st.text_input(q, key=f"ans_{i}")

        if len(st.session_state.answers) < len(st.session_state.questions):
            st.session_state.answers.append(ans)
        else:
            st.session_state.answers[i] = ans

# STEP 3
if st.button("📊 Evaluate & Generate Plan"):

    if not any(st.session_state.answers):
        st.warning("Please answer at least one question")
        st.stop()

    st.write("### 📊 Skill Evaluation:")

    for skill, ans in zip(st.session_state.skills, st.session_state.answers):
        result = evaluate_answer(ans)
        st.write(f"**{skill}**")
        st.write(result)

    st.write("### 📚 Personalized Learning Plan:")
    st.write(learning_plan(st.session_state.skills[:3]))

    