import streamlit as st
import pandas as pd
import plotly.express as px

from chatbot import get_career_guidance
from model import recommend_careers
from resources import get_learning_resources
from progress_tracker import render_progress_tracker
from resources import get_all_skills, get_learning_resources
from practice_platform import (
    render_dsa_page,
    render_aptitude_page,
)

from student_auth import (
    init_auth_db,
    create_student,
    authenticate_student,
    load_student_profile,
    save_student_profile,
)

# =========================================================
# PAGE CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Skillora AI | Career Intelligence",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
/* Professional Demo Login Button */
div.stButton > button[kind="secondary"] {
    background: linear-gradient(135deg, #1D4ED8, #2563EB);
    color: #FFFFFF;
    border: 1px solid #1D4ED8;
    border-radius: 10px;
    padding: 0.65rem 1rem;
    font-weight: 600;
    transition: all 0.2s ease;
}

div.stButton > button[kind="secondary"]:hover {
    background: linear-gradient(135deg, #1E40AF, #1D4ED8);
    color: #FFFFFF;
    border-color: #1E40AF;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
}
</style>
""", unsafe_allow_html=True)



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
# SIMPLE SKILLORAAI LOGIN PAGE
# =========================================================

init_auth_db()

if "student" not in st.session_state:
    st.session_state["student"] = None


if st.session_state.student is None:

    # ---------- ANIMATED LOGIN DESIGN ----------
    st.markdown("""
    <style>
    @keyframes floatCap {
        0%, 100% { transform: translateY(0) rotate(-5deg); }
        50% { transform: translateY(-10px) rotate(5deg); }
    }

    @keyframes glowTitle {
        0%, 100% { text-shadow: 0 0 10px #22d3ee55; }
        50% { text-shadow: 0 0 28px #22d3ee, 0 0 45px #6366f1; }
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(circle at 15% 15%, #172b50, transparent 40%),
            radial-gradient(circle at 85% 75%, #302047, transparent 42%),
            #080d1b;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stMainBlockContainer"] {
        max-width: 760px;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }

    .skillora-header {
        text-align: center;
        margin: 0 auto 30px auto;
        animation: fadeUp 0.8s ease-out;
    }

    .skillora-cap {
        font-size: 66px;
        line-height: 1.3;
        display: inline-block;
        animation: floatCap 3s ease-in-out infinite;
        filter: drop-shadow(0 0 14px #22d3ee88);
    }

    .skillora-title {
        font-size: clamp(32px, 6vw, 44px);
        font-weight: 850;
        letter-spacing: -1px;
        color: #ffffff;
        margin-top: 8px;
        animation: glowTitle 3s ease-in-out infinite;
    }

    .skillora-title span {
        color: #67e8f9;
    }

    .skillora-tagline {
        color: #aab9d5;
        font-size: 14px;
        margin-top: 8px;
        letter-spacing: 0.4px;
    }

    [data-testid="stTextInput"] label {
        color: #e5eaff !important;
        font-weight: 600;
    }

    [data-testid="stTextInput"] input {
        background: #0e172a !important;
        color: #ffffff !important;
        border: 1px solid #34476b !important;
        border-radius: 10px !important;
        min-height: 46px;
    }

    [data-testid="stTextInput"] input:focus {
        border-color: #22d3ee !important;
        box-shadow: 0 0 0 2px #22d3ee30 !important;
    }

    .stFormSubmitButton > button {
        background: linear-gradient(100deg, #0891b2, #4f70ee, #6366f1);
        background-size: 200% 200%;
        color: white !important;
        border: 1px solid #67e8f955 !important;
        border-radius: 12px !important;
        min-height: 49px;
        font-weight: 750;
        transition: all 0.25s ease;
        box-shadow: 0 5px 22px #4f46e533;
    }

    .stFormSubmitButton > button:hover {
        background-position: 100% 50%;
        transform: translateY(-2px);
        box-shadow: 0 8px 28px #22d3ee55;
        border-color: #67e8f9 !important;
    }

    .skillora-footer {
        text-align: center;
        color: #8493b0;
        font-size: 12px;
        line-height: 1.9;
        border-top: 1px solid #263858;
        margin-top: 45px;
        padding-top: 20px;
    }

    .skillora-footer span {
        display: block;
        color: #67e8f9;
        font-size: 16px;
        font-weight: 800;
    }

    @media (prefers-reduced-motion: reduce) {
        .skillora-cap, .skillora-title, .skillora-header {
            animation: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- HEADER ----------
    st.markdown("""
    <div class="skillora-header">
        <div class="skillora-cap">🎓</div>
        <div class="skillora-title">
            SkillOra<span>AI</span>
        </div>
        <div class="skillora-tagline">
            Your Future. Your Skills. Your Success.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- LOGIN FORM ----------
    with st.form("student_login_form"):
        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password"
        )

        login_submit = st.form_submit_button(
            "Login",
            use_container_width=True
        )
        # ---------- SHARED DEMO LOGIN ----------
    demo_login = st.button(
        "Try Demo Login",
        use_container_width=True,
    )

    if demo_login:
        st.session_state.student = {
            "id": -1,
            "full_name": "SkillOraAI Demo User",
            "email": "demo@skilloraai.local",
            "is_demo": True,
        }
        st.session_state.pop(
            "skillora_progress_loaded_for", None
        )
        st.rerun()

    # ---------- LOGIN SECURITY & AUTHENTICATION ----------
    if login_submit:
        clean_email = email.strip()

        if not clean_email or not password:
            st.warning("Please enter your email and password.")

        elif len(clean_email) > 254 or "\n" in clean_email:
            st.error("Please enter a valid email address.")

        else:
            try:
                student = authenticate_student(clean_email, password)

                if student:
                    st.session_state.student = student
                    st.session_state.pop(
                        "skillora_progress_loaded_for", None
                    )
                    st.rerun()
                else:
                    st.error("Invalid email or password.")

            except Exception as error:
                st.error("Login failed. Please try again.")
                print(f"SkillOraAI login error: {error}")

    # ---------- FOOTER ----------
    st.markdown("""
    <div class="skillora-footer">
        Created with ❤️ by
        <span>Roshan Jadhao</span>
        SkillOraAI · Learn Smarter. Build Your Future.
    </div>
    """, unsafe_allow_html=True)

    st.stop()

# =========================================================
# YOUR EXISTING DASHBOARD CODE CONTINUES BELOW
# =========================================================

# ---------- STUDENT LOGOUT ----------

st.markdown("""
<style>
/* Professional SkillOraAI Logout Button */
[data-testid="stSidebar"] .stButton > button {
    background: linear-gradient(90deg, #6278ff, #925cff) !important;
    color: #ffffff !important;
    border: 1px solid #8290ff !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    min-height: 44px !important;
    transition: all 0.25s ease !important;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: linear-gradient(90deg, #4f63ed, #7c45e8) !important;
    border-color: #b3bdff !important;
    box-shadow: 0 4px 14px rgba(98, 120, 255, 0.35) !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

student = st.session_state.get("student")

if student:
    with st.sidebar:
        st.write(f"Welcome, {student['full_name']}")

        if st.button("Logout", use_container_width=True):
            st.session_state.student = None

            st.session_state.pop(
                "skillora_progress_loaded_for", None
            )

            st.session_state.pop(
                "skillora_completed_steps", None
            )

            st.rerun()
# ---------- END STUDENT LOGOUT ----------


if st.session_state.student is None:
    st.markdown(
        "<h1 style='text-align:center;color:#67e8f9;'>"
        "Skillora AI</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<p style='text-align:center;'>"
        "Your Personal Career Intelligence Platform</p>",
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 1.2, 1])

    with center:
        st.markdown("### Welcome to Skillora AI")

        auth_mode = st.radio(
            "Choose an option",
            ["Login", "Sign Up"],
            horizontal=True,
            key="auth_mode",
        )

        if auth_mode == "Login":
            with st.form("student_login_form"):
                email = st.text_input("Email address")
                password = st.text_input(
                    "Password",
                    type="password",
                )

                submitted = st.form_submit_button(
                    "Login",
                    type="primary",
                    use_container_width=True,
                )
            if st.button(
                "🚀 Try Demo Login",
                use_container_width=True,
                type="secondary",
                key="demo_login_button",
            ):
                st.session_state.student = {
                    "id": -1,
                    "full_name": "SkillOraAI Demo User",
                    "email": "demo@skilloraai.local",
                    "is_demo": True,
                }
                st.rerun()

            if submitted:
                if not email.strip() or not password:
                    st.warning(
                        "Please enter your email and password."
                    )
                else:
                    student = authenticate_student(
                        email.strip(),
                        password,
                    )

                    if student:
                        st.session_state.student = student
                        st.rerun()
                    else:
                        st.error("Invalid email or password.")

        else:
            with st.form("student_signup_form"):
                full_name = st.text_input("Full name")
                email = st.text_input("Email address")

                password = st.text_input(
                    "Create password",
                    type="password",
                    help="Use 10–128 characters.",
                )

                confirm_password = st.text_input(
                    "Confirm password",
                    type="password",
                )

                submitted = st.form_submit_button(
                    "Create Account",
                    type="primary",
                    use_container_width=True,
                )

            if submitted:
                if password != confirm_password:
                    st.error("Passwords do not match.")
                else:
                    success, message = create_student(
                        full_name,
                        email.strip(),
                        password,
                    )

                    if success:
                        st.success(
                            "Account created! "
                            "Select Login to continue."
                        )
                    else:
                        st.error(message)

    st.stop()


# Default session state for existing features
st.session_state.setdefault("skillora_chat_history", [])
st.session_state.setdefault("skillora_analysis", None)
st.session_state.setdefault("skillora_completed_steps", [])

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
    page = st.radio(
    "Choose a page",
    [
        "My Profile",
        "Explore Skills",
        "Skill Gap Analysis",
        "Learning Roadmap",
        "Learning Resources",
        "AI Career Assistant",
        "DSA Practice",
        "Aptitude Practice",
    ],
    label_visibility="collapsed",
    key="skillora_navigation",
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

    
# =========================================================
# DSA AND APTITUDE PAGE ROUTING
# =========================================================

if page in ("DSA Practice", "Aptitude Practice"):
    current_student = st.session_state.get("student")

    if not current_student:
        st.warning("Please log in first.")
        st.stop()

    if page == "DSA Practice":
        render_dsa_page(current_student)
    else:
        render_aptitude_page(current_student)

    st.stop()


# =========================================================
# PROFESSIONAL MY PROFILE
# =========================================================

import base64
import html

if page == "My Profile":
    student = st.session_state.get("student")

    if not student:
        st.warning("Please log in to view your profile.")
        st.stop()

    is_demo = student.get("is_demo", False)

if is_demo:
    profile = {}
    st.info(
        "Demo Mode: Profile changes are temporary "
        "and will not be saved to a student account."
    )
else:
    profile = load_student_profile(student["id"]) or {}

    st.title("👤 My Professional Profile")
    st.caption("Manage your personal details, education, skills and achievements.")

    # Profile photo storage in session state
    photo_key = f"profile_photo_{student['id']}"

    st.markdown(
        """
        <style>
        .profile-card {
            background: linear-gradient(135deg, #17274a, #171638, #102d3c);
            border: 1px solid #30416a;
            border-radius: 22px;
            padding: 28px;
            margin-bottom: 20px;
        }
        .profile-name {
            font-size: 28px;
            font-weight: 800;
            color: #ffffff;
        }
        .profile-subtitle {
            color: #cbd5e1;
            font-size: 14px;
            margin-top: 8px;
        }
        .profile-tag {
            display: inline-block;
            background: #24345a;
            border: 1px solid #5268a0;
            border-radius: 20px;
            padding: 6px 12px;
            margin-top: 12px;
            color: #a5f3fc;
            font-size: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Photo upload
    left, right = st.columns([1, 2.5], gap="large")

    with left:
        st.markdown("### Profile Photo")

        uploaded_photo = st.file_uploader(
            "Upload a photo",
            type=["png", "jpg", "jpeg"],
            key=f"profile_upload_{student['id']}",
            help="Choose a clear JPG or PNG photo.",
        )

        if uploaded_photo:
            photo_bytes = uploaded_photo.getvalue()

            if len(photo_bytes) > 5 * 1024 * 1024:
                st.error("Photo must be smaller than 5 MB.")
            else:
                st.session_state[photo_key] = photo_bytes

        current_photo = st.session_state.get(photo_key)

        if current_photo:
            st.image(
                current_photo,
                width=170,
                caption="Your profile photo",
            )
        else:
            initials = "".join(
                part[0].upper()
                for part in student["full_name"].split()
                if part
            )[:2] or "ST"

            st.markdown(
                f"""
                <div style="
                    width:150px;height:150px;border-radius:50%;
                    background:linear-gradient(135deg,#6278ff,#925cff);
                    display:flex;align-items:center;justify-content:center;
                    color:white;font-size:42px;font-weight:800;
                    border:4px solid #5268a0;margin:10px auto;">
                    {html.escape(initials)}
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.caption("Your photo is shown in this session. Persistent photo storage requires a database change.")

    with right:
        safe_name = html.escape(str(student.get("full_name", "Student")))
        safe_email = html.escape(str(student.get("email", "")))
        safe_course = html.escape(
            str(profile.get("course") or "Add your course below")
        )
        safe_college = html.escape(
            str(profile.get("college") or "Add your college below")
        )

        st.markdown(
            f"""
            <div class="profile-card">
                <div style="color:#67e8f9;font-size:12px;
                            font-weight:800;letter-spacing:2px;">
                    STUDENT PROFILE
                </div>
                <div class="profile-name">{safe_name}</div>
                <div class="profile-subtitle">{safe_email}</div>
                <div class="profile-subtitle">{safe_course}</div>
                <div class="profile-subtitle">{safe_college}</div>
                <div class="profile-tag">SKILLORAAI LEARNER</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.subheader("✏️ Edit Your Information")

    with st.form("professional_student_profile_form"):
        phone = st.text_input(
            "Phone Number",
            value=profile.get("phone", ""),
            placeholder="Enter your phone number",
        )

        location = st.text_input(
            "City / Location",
            value=profile.get("location", ""),
            placeholder="Example: Pune, Maharashtra",
        )

        college = st.text_input(
            "College Name",
            value=profile.get("college", ""),
            placeholder="Enter your college name",
        )

        course = st.text_input(
            "Course / Branch / Year",
            value=profile.get("course", ""),
            placeholder="Example: B.Tech Mechanical Engineering, Third Year",
        )

        skills = st.text_area(
            "Technical Skills",
            value=profile.get("skills", ""),
            placeholder="Python, SQL, Machine Learning, Streamlit",
            height=100,
        )

        achievements = st.text_area(
            "Achievements & Certificates",
            value=profile.get("achievements", ""),
            placeholder="Add your real awards, certificates and projects.",
            height=100,
        )

        bio = st.text_area(
            "Professional About Me",
            value=profile.get("bio", ""),
            placeholder="Write a short introduction about your interests and career goals.",
            height=120,
        )

        save_clicked = st.form_submit_button(
            "💾 Save Profile",
            type="primary",
            use_container_width=True,
        )

    
    if save_clicked:
        if student.get("is_demo", False):
            st.warning(
                "Demo Mode: Profile changes cannot be saved. "
                "Create a student account to save your profile."
            )
        else:
            try:
                save_student_profile(
                    student["id"],
                    phone,
                    college,
                    course,
                    skills,
                    bio,
                )

                if location.strip() or achievements.strip():
                    st.warning(
                        "Your main profile was saved. Location and "
                        "achievements require database schema support."
                    )
                else:
                    st.success("Profile saved successfully!")

                st.rerun()

            except Exception:
                st.error(
                    "Unable to save your profile. "
                    "Please check student_auth.py."
                )

    checklist = [
        ("Profile photo", bool(st.session_state.get(photo_key))),
        ("College details", bool(profile.get("college"))),
        ("Course / branch", bool(profile.get("course"))),
        ("Technical skills", bool(profile.get("skills"))),
        ("About me", bool(profile.get("bio"))),
        ("Achievements", bool(profile.get("achievements"))),
    ]

    completed = sum(done for _, done in checklist)
    st.progress(completed / len(checklist))
    st.caption(f"{completed} of {len(checklist)} profile items completed")

    for label, done in checklist:
        st.write(f"{'✅' if done else '⬜'} {label}")

    st.stop()

# =========================================================
# END PROFESSIONAL MY PROFILE
# =========================================================

    
# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">AI-POWERED CAREER INTELLIGENCE</div>
    <div class="hero-title">Build Your Future with Skillora AI</div>
    <div class="hero-description">
        Discover career opportunities, identify skill gaps,
        create a learning roadmap, and prepare for your next
        career milestone — all in one place.
    </div>
</div>
""", unsafe_allow_html=True)



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
st.header("📚 Learning Resources")

resource_topics = get_all_skills()

resource_topic = st.selectbox(
    "Select a learning topic",
    options=resource_topics,
    key="skillora_learning_resource_topic",
)

if st.button(
    "🔎 Find Learning Resources",
    key="find_resources",
    type="primary",
):
    try:
        resource_results = get_learning_resources(resource_topic)

        if resource_results:
            st.success(
                f"Found {len(resource_results)} resource(s) "
                f"for {resource_topic}."
            )

            for index, resource in enumerate(
                resource_results, start=1
            ):
                title = resource.get(
                    "title", "Learning Resource"
                )
                url = resource.get("url", "")

                # Support both old and new resource formats.
                provider = resource.get(
                    "provider",
                    resource.get("type", "Learning Resource")
                )
                level = resource.get("level", "All levels")

                with st.container(border=True):
                    st.markdown(f"### {index}. {title}")
                    st.caption(f"Provider / Type: {provider}")
                    st.caption(f"Level: {level}")

                    if url:
                        st.markdown(
                            f"[📖 Open Learning Resource]({url})"
                        )
                    else:
                        st.info(
                            "No link is available for this resource."
                        )

        else:
            st.info(
                f"No resources found for {resource_topic}. "
                "Please select another topic."
            )

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

# =========================================================
# APP FOOTER — CREATOR CREDIT
# =========================================================

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 18px 10px;
        margin-top: 35px;
        border-top: 1px solid #293858;
        color: #aab8d4;
        font-size: 13px;
    ">
        Built with ❤️ using AI
        <br>
        <span style="
            color: #67e8f9;
            font-weight: 700;
            font-size: 15px;
        ">
            Created by Roshan Jadhao
        </span>
        <br>
        <span style="font-size: 11px;">
            SkillOraAI · Career Intelligence Platform
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

