
import streamlit as st
import pandas as pd
import plotly.express as px

from chatbot import get_career_guidance
from model import recommend_careers
from resources import get_learning_resources
from progress_tracker import render_progress_tracker


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Skillora AI | Career Intelligence",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# PREMIUM UI
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: #080d1b;
        color: #e8edff;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stSidebar"] {
        background: #10182b;
        border-right: 1px solid #263451;
    }

    [data-testid="stHeader"] {
        background: rgba(8, 13, 27, 0.9);
    }

    h1, h2, h3 {
        color: #f5f7ff !important;
        font-family: 'Inter', sans-serif;
    }

    p, label, li, [data-testid="stMarkdownContainer"] {
        color: #cbd5ee;
    }

    .hero {
        padding: 30px;
        border: 1px solid #30416a;
        border-radius: 22px;
        background: linear-gradient(120deg, #17274a, #171638, #102d3c);
        margin-bottom: 25px;
    }

    .hero-tag {
        color: #67e8f9;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 2px;
    }

    .hero-title {
        font-size: clamp(28px, 4vw, 42px);
        font-weight: 800;
        color: #ffffff;
        margin: 12px 0;
    }

    .hero-description {
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.8;
    }

    .section-label {
        color: #67e8f9;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 1.5px;
        margin-bottom: 6px;
    }

    .metric-card {
        background: linear-gradient(145deg, #141f38, #101729);
        border: 1px solid #293858;
        padding: 20px;
        border-radius: 16px;
        min-height: 125px;
    }

    .metric-label {
        color: #9caed0;
        font-size: 13px;
    }

    .metric-value {
        color: #ffffff;
        font-size: 28px;
        font-weight: 800;
        margin-top: 10px;
    }

    .career-card {
        background: linear-gradient(145deg, #16213b, #11192d);
        border: 1px solid #304363;
        padding: 20px;
        border-radius: 17px;
        min-height: 165px;
        margin-bottom: 12px;
    }

    .career-name {
        font-size: 19px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
    }

    .career-score {
        font-size: 30px;
        font-weight: 800;
        color: #67e8f9;
    }

    .muted {
        color: #9aacca;
        font-size: 13px;
    }

    .chat-info {
        background: #111d33;
        border: 1px solid #293b5b;
        border-radius: 14px;
        padding: 16px;
        margin: 8px 0 16px 0;
    }

    .stButton > button,
    .stDownloadButton > button,
    .stFormSubmitButton > button {
        border-radius: 10px;
        min-height: 42px;
        font-weight: 700;
        border: 1px solid #3d76a5;
        transition: 0.2s ease;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        border-color: #67e8f9;
        color: #67e8f9;
    }

    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea {
        background: #111a2d !important;
        color: #ffffff !important;
    }

    div[data-baseweb="select"] > div {
        background: #111a2d;
        border-color: #304363;
    }

    [data-testid="stChatMessage"] {
        background: #111a2d;
        border: 1px solid #293858;
        border-radius: 14px;
        padding: 12px;
    }

    hr {
        border-color: #283652;
    }

    .footer {
        text-align: center;
        color: #8191b2;
        font-size: 12px;
        padding: 25px 0 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "skillora_chat_history" not in st.session_state:
    st.session_state.skillora_chat_history = []

if "skillora_analysis" not in st.session_state:
    st.session_state.skillora_analysis = None

if "skillora_completed_steps" not in st.session_state:
    st.session_state.skillora_completed_steps = []


# =========================================================
# HEADER
# =========================================================

with st.sidebar:
    st.markdown("## 🎯 Skillora AI")
    st.caption("CAREER INTELLIGENCE PLATFORM")
    st.divider()

    st.markdown("### 🧭 Navigation")
    st.markdown(
        """
        - Career Dashboard
        - Skill Gap Analysis
        - Learning Roadmap
        - Learning Resources
        - AI Career Assistant
        """
    )

    st.divider()
    st.markdown("### 🛠️ Your Skills")

    default_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Data Analysis",
        "Communication",
        "Power BI",
        "Excel",
        "Java",
        "C++",
        "Deep Learning",
        "Statistics",
        "Git",
        "HTML",
        "CSS",
        "Mechanical Design",
    ]

    selected_skills = st.multiselect(
        "Select skills you already know",
        options=default_skills,
        default=[],
        help="Select the skills you have actually learned.",
    )

    custom_skills_text = st.text_area(
        "Add other skills",
        placeholder="Example: Streamlit, Pandas, AutoCAD",
        height=90,
    )

    custom_skills = [
        skill.strip()
        for skill in custom_skills_text.split(",")
        if skill.strip()
    ]

    all_skills = list(
        dict.fromkeys(selected_skills + custom_skills)
    )

    analyze_clicked = st.button(
        "🚀 Analyze My Career",
        type="primary",
        width="stretch",
    )

    st.caption("Your skills help personalize career recommendations.")

    st.divider()
    st.caption("Skillora AI • Learning starts with one step.")


st.markdown(
    """
    <div class="hero">
        <div class="hero-tag">AI-POWERED CAREER INTELLIGENCE</div>
        <div class="hero-title">Build Your Future with Skillora AI</div>
        <div class="hero-description">
            Discover career opportunities, identify skill gaps,
            create a learning roadmap, and prepare for your next
            career milestone — all in one place.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# CAREER ANALYSIS
# =========================================================

if analyze_clicked:
    if not all_skills:
        st.warning(
            "Please select or enter at least one skill before analysis."
        )
    else:
        try:
            with st.spinner("Analyzing your skills and career options..."):
                result = recommend_careers(all_skills)

                st.session_state.skillora_analysis = {
                    "skills": all_skills,
                    "result": result,
                }

                # Start a fresh roadmap when skills are analyzed again.
                st.session_state.skillora_completed_steps = []

        except Exception as error:
            st.error(
                "Career analysis failed. Check model.py and try again."
            )
            st.exception(error)


# =========================================================
# NORMALIZE RECOMMENDATION RESULTS
# =========================================================

analysis = st.session_state.skillora_analysis
career_rows = []
best_match = "Not selected"
missing_skills = []

if analysis:
    result = analysis["result"]

    if isinstance(result, pd.DataFrame):
        career_rows = result.to_dict(orient="records")

    elif isinstance(result, list):
        career_rows = result

    elif isinstance(result, dict):
        if "recommendations" in result:
            recommendations = result["recommendations"]

            if isinstance(recommendations, pd.DataFrame):
                career_rows = recommendations.to_dict(
                    orient="records"
                )
            elif isinstance(recommendations, list):
                career_rows = recommendations
            else:
                st.warning(
                    "The recommendations format is not supported."
                )
        else:
            career_rows = [result]

    if career_rows:
        first_row = career_rows[0]

        best_match = (
            first_row.get("career")
            or first_row.get("Career")
            or first_row.get("role")
            or first_row.get("Role")
            or first_row.get("job_role")
            or "Recommended Career"
        )

        possible_gaps = (
            first_row.get("missing_skills")
            or first_row.get("skill_gaps")
            or first_row.get("missing")
            or []
        )

        if isinstance(possible_gaps, str):
            missing_skills = [
                item.strip()
                for item in possible_gaps.split(",")
                if item.strip()
            ]
        elif isinstance(possible_gaps, list):
            missing_skills = possible_gaps

        # If the model does not provide gaps, use a simple fallback.
        if not missing_skills:
            missing_skills = [
                skill
                for skill in [
                    "Python",
                    "SQL",
                    "Machine Learning",
                    "Communication",
                ]
                if skill.lower() not in {
                    s.lower() for s in analysis["skills"]
                }
            ]


# =========================================================
# CAREER DASHBOARD
# =========================================================

st.markdown(
    '<div class="section-label">YOUR OVERVIEW</div>',
    unsafe_allow_html=True,
)
st.header("📊 Career Dashboard")

if analysis and career_rows:
    metric1, metric2, metric3, metric4 = st.columns(4)

    metrics = [
        (metric1, "Skills Selected", len(analysis["skills"])),
        (metric2, "Career Matches", len(career_rows)),
        (metric3, "Skills to Explore", len(missing_skills)),
        (
            metric4,
            "Roadmap Progress",
            f"{len(st.session_state.skillora_completed_steps)} steps",
        ),
    ]

    for column, label, value in metrics:
        with column:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">{label}</div>
                    <div class="metric-value">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### ✨ Your Top Career Matches")

    career_columns = st.columns(min(3, len(career_rows)))

    for index, row in enumerate(career_rows[:3]):
        career_name = (
            row.get("career")
            or row.get("Career")
            or row.get("role")
            or row.get("Role")
            or row.get("job_role")
            or f"Career Option {index + 1}"
        )

        score = (
            row.get("match_percentage")
            or row.get("match_score")
            or row.get("score")
            or row.get("similarity")
            or row.get("percentage")
        )

        with career_columns[index]:
            if isinstance(score, (int, float)):
                if 0 <= score <= 1:
                    score_display = f"{score * 100:.1f}%"
                else:
                    score_display = f"{score:.1f}%"
            else:
                score_display = "Recommended"

            st.markdown(
                f"""
                <div class="career-card">
                    <div class="muted">CAREER MATCH #{index + 1}</div>
                    <div class="career-name">{career_name}</div>
                    <div class="career-score">{score_display}</div>
                    <div class="muted">Based on your profile</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("### 📈 Career Match Overview")

    chart_data = []

    for index, row in enumerate(career_rows):
        name = (
            row.get("career")
            or row.get("Career")
            or row.get("role")
            or row.get("Role")
            or row.get("job_role")
            or f"Career {index + 1}"
        )

        score = (
            row.get("match_percentage")
            or row.get("match_score")
            or row.get("score")
            or row.get("similarity")
            or row.get("percentage")
        )

        if isinstance(score, (int, float)):
            if 0 <= score <= 1:
                score = score * 100

            chart_data.append(
                {"Career": name, "Match Score": score}
            )

    if chart_data:
        chart_df = pd.DataFrame(chart_data)

        fig = px.bar(
            chart_df,
            x="Career",
            y="Match Score",
            color="Match Score",
            color_continuous_scale=["#3b82f6", "#22d3ee"],
            template="plotly_dark",
            title="Career Match Scores",
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="#e8edff",
            xaxis_title="Career",
            yaxis_title="Match Score (%)",
            margin=dict(l=10, r=10, t=55, b=10),
        )

        st.plotly_chart(fig, width="stretch")

    with st.expander("📄 View all recommendation details"):
        st.dataframe(
            pd.DataFrame(career_rows),
            width="stretch",
            hide_index=True,
        )

    csv_data = pd.DataFrame(career_rows).to_csv(index=False)

    st.download_button(
        "⬇️ Download Career Report (CSV)",
        data=csv_data,
        file_name="skillora_career_report.csv",
        mime="text/csv",
    )

else:
    st.markdown(
        """
        <div class="chat-info">
            <h3>👋 Welcome to your career dashboard!</h3>
            <p>
                Select your skills in the sidebar and click
                <b>Analyze My Career</b> to unlock personalized
                career recommendations, skill-gap analysis,
                and a learning roadmap.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# SKILL GAP ANALYSIS
# =========================================================

st.divider()
st.markdown(
    '<div class="section-label">GROW YOUR SKILLS</div>',
    unsafe_allow_html=True,
)
st.header("🧩 Skill Gap Analysis")

if analysis:
    st.write(f"**Current target career:** {best_match}")

    if missing_skills:
        st.write("Skills you can consider learning next:")

        for skill in missing_skills:
            st.markdown(f"- 📌 {skill}")

        selected_gap = st.selectbox(
            "Choose a skill to focus on",
            options=missing_skills,
        )

        if selected_gap:
            st.info(
                f"Recommended next step: learn the fundamentals "
                f"of **{selected_gap}**, practise with exercises, "
                "and build a small project."
            )
    else:
        st.success(
            "No skill gaps were returned by the recommendation model."
        )
else:
    st.info(
        "Run career analysis first to view personalized skill gaps."
    )


# =========================================================
# LEARNING ROADMAP
# =========================================================

st.divider()
st.markdown(
    '<div class="section-label">YOUR ACTION PLAN</div>',
    unsafe_allow_html=True,
)
st.header("🗺️ Learning Roadmap")

roadmap_steps = [
    "Review the fundamentals of your selected career.",
    "Choose one important missing skill.",
    "Complete a beginner-friendly tutorial.",
    "Practise using small exercises.",
    "Build a mini-project using the skill.",
    "Upload your project to GitHub.",
    "Update your resume and portfolio.",
    "Practise interview questions.",
]

completed_count = 0

for index, step in enumerate(roadmap_steps):
    is_completed = st.checkbox(
        step,
        value=index in st.session_state.skillora_completed_steps,
        key=f"roadmap_step_{index}",
    )

    if is_completed:
        completed_count += 1

        if index not in st.session_state.skillora_completed_steps:
            st.session_state.skillora_completed_steps.append(index)
    else:
        if index in st.session_state.skillora_completed_steps:
            st.session_state.skillora_completed_steps.remove(index)

progress = completed_count / len(roadmap_steps)

st.progress(progress)
st.caption(
    f"Roadmap progress: {completed_count}/{len(roadmap_steps)} steps completed"
)

st.divider()
render_progress_tracker()

# =========================================================
# LEARNING RESOURCES
# =========================================================

st.divider()

st.markdown(
    '<div class="section-label">KEEP LEARNING</div>',
    unsafe_allow_html=True,
)

st.header("📚 Learning Resources")

resource_topics = [
    "Python",
    "SQL",
    "Machine Learning",
    "Pandas",
    "Data Analysis",
    "Data Visualization",
    "Streamlit",
    "Git",
    "HTML",
    "CSS",
    "Power BI",
    "Excel",
    "Deep Learning",
    "Communication",
    "Interview Preparation",
]

resource_topic = st.selectbox(
    "Select a learning topic",
    options=resource_topics,
    key="resource_topic_selector",
)

if st.button(
    "🔎 Find Learning Resources",
    key="find_resources",
    type="primary",
):
    try:
        # Use the actual function defined in resources.py.
        resource_results = get_learning_resources(resource_topic)

        if resource_results:
            st.success(
                f"Found {len(resource_results)} resource(s) "
                f"for {resource_topic}."
            )

            for index, resource in enumerate(resource_results, start=1):
                title = resource.get("title", "Learning Resource")
                provider = resource.get("provider", "Learning Platform")
                level = resource.get("level", "All levels")
                url = resource.get("url", "")

                with st.container(border=True):
                    st.markdown(f"### {index}. {title}")
                    st.caption(f"Provider: {provider}")
                    st.caption(f"Level: {level}")

                    if url:
                        st.markdown(f"[📖 Open Learning Resource]({url})")
                    else:
                        st.info("No link is available for this resource.")
        else:
            st.info("No resources found for this topic.")

    except Exception as error:
        st.error("Unable to load learning resources.")
        st.code(str(error))

# =========================================================
# AI CAREER ASSISTANT — AVAILABLE WITHOUT ANALYSIS
# =========================================================

st.divider()
st.markdown(
    '<div class="section-label">ASK • LEARN • IMPROVE</div>',
    unsafe_allow_html=True,
)
st.header("🤖 Skillora AI Career Assistant")

st.markdown(
    """
    <div class="chat-info">
        Ask questions about Python, AI/ML, careers, projects,
        interviews, learning plans, or your skill gaps.
        <br><br>
        <b>Try:</b> Explain Machine Learning, What should I learn next?,
        or Help me prepare for interviews.
    </div>
    """,
    unsafe_allow_html=True,
)

# Build context even if the user has not run career analysis.
chat_skills = (
    analysis["skills"]
    if analysis
    else all_skills
)

chat_career = best_match if analysis else "Not selected"

chat_missing_skills = missing_skills if analysis else []

# Display previous messages.
for message in st.session_state.skillora_chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input + Search button.
with st.form("skillora_chat_form", clear_on_submit=True):
    chat_col, search_col = st.columns([5, 1])

    with chat_col:
        user_question = st.text_input(
            "Ask Skillora AI",
            placeholder="Type your question here...",
            label_visibility="collapsed",
        )

    with search_col:
        search_clicked = st.form_submit_button(
            "🔍 Search",
            type="primary",
            width="stretch",
        )

if search_clicked:
    if not user_question.strip():
        st.warning("Please type a question first.")
    else:
        question = user_question.strip()

        st.session_state.skillora_chat_history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        try:
            answer = get_career_guidance(
                question=question,
                user_skills=chat_skills,
                career=chat_career,
                missing_skills=chat_missing_skills,
            )

        except Exception:
            answer = (
                "Sorry, I couldn't answer that right now. "
                "Please check chatbot.py and try again."
            )

        st.session_state.skillora_chat_history.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        st.rerun()

if st.session_state.skillora_chat_history:
    if st.button("🗑️ Clear Chat", key="clear_skillora_chat"):
        st.session_state.skillora_chat_history = []
        st.rerun()


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Skillora AI · Career Intelligence & Learning Platform
        <br>
        Learn consistently. Build projects. Grow your future.
    </div>
    """,
    unsafe_allow_html=True,
)
