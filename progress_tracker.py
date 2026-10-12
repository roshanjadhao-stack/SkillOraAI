
import json
from pathlib import Path

import streamlit as st

PROGRESS_FILE = Path(__file__).with_name("student_progress.json")

DEFAULT_SKILLS = [
    "Python",
    "SQL",
    "Pandas",
    "Data Analysis",
    "Machine Learning",
    "Data Visualization",
    "Git and GitHub",
    "Streamlit",
    "Communication",
    "Interview Preparation",
]


def load_progress():
    """Load progress saved in the local JSON file."""
    if not PROGRESS_FILE.exists():
        return {}

    try:
        with PROGRESS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_progress(progress):
    """Save progress to the local JSON file."""
    try:
        with PROGRESS_FILE.open("w", encoding="utf-8") as file:
            json.dump(progress, file, indent=4, ensure_ascii=False)
        return True
    except OSError as error:
        st.error(f"Could not save progress: {error}")
        return False


def render_progress_tracker(roadmap_skills=None):
    """Show a session-only tracker for demo users."""
    is_demo = (
        st.session_state.get("student") or {}
    ).get("is_demo", False)

    st.subheader("Student Progress Tracker")
    st.caption(
        "Track completed skills and continue learning at your own pace."
    )

    # Demo progress stays in this Streamlit session.
    if is_demo:
        if "demo_skill_progress" not in st.session_state:
            st.session_state["demo_skill_progress"] = {}

        saved_progress = st.session_state["demo_skill_progress"]
    else:
        saved_progress = load_progress()

    skills = list(DEFAULT_SKILLS)

    if roadmap_skills:
        for skill in roadmap_skills:
            if isinstance(skill, str) and skill.strip():
                cleaned = skill.strip()
                if cleaned not in skills:
                    skills.append(cleaned)

    if "custom_tracker_skills" not in st.session_state:
        st.session_state["custom_tracker_skills"] = []

    if "tracker_add_input" not in st.session_state:
        st.session_state["tracker_add_input"] = ""

    with st.form("add_tracker_skill_form"):
        new_skill = st.text_input(
            "Add your own skill",
            key="tracker_add_input",
            placeholder="Example: Deep Learning",
        )
        add_skill = st.form_submit_button("Add Skill")

    if add_skill:
        cleaned = new_skill.strip()
        existing = {
            skill.casefold()
            for skill in skills + st.session_state["custom_tracker_skills"]
        }

        if cleaned and cleaned.casefold() not in existing:
            st.session_state["custom_tracker_skills"].append(cleaned)
            st.rerun()
        elif not cleaned:
            st.warning("Please enter a skill name.")
        else:
            st.info("This skill is already in your tracker.")

    for skill in st.session_state["custom_tracker_skills"]:
        if skill not in skills:
            skills.append(skill)

    st.markdown("### Your Skills")

    with st.form("student_progress_form"):
        completed = {}

        for index, skill in enumerate(skills):
            completed[skill] = st.checkbox(
                skill,
                value=bool(saved_progress.get(skill, False)),
                key=f"progress_skill_{index}",
            )

        save_clicked = st.form_submit_button(
            "Save My Progress",
            type="primary",
            use_container_width=True,
        )

    if save_clicked:
        if is_demo:
            st.session_state["demo_skill_progress"] = completed
            st.success(
                "Demo progress saved for this session only."
            )
        elif save_progress(completed):
            st.success("Your learning progress has been saved!")

    # Read from the correct storage source.
    if is_demo:
        current_progress = st.session_state["demo_skill_progress"]
        st.info("Demo mode: progress is temporary and isn't saved to a student account.")
    else:
        current_progress = load_progress()

    total_skills = len(skills)
    completed_count = sum(
        bool(current_progress.get(skill, False))
        for skill in skills
    )

    percentage = (
        round(completed_count / total_skills * 100)
        if total_skills
        else 0
    )

    st.markdown("### Your Learning Summary")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Skills", total_skills)
    col2.metric("Completed", completed_count)
    col3.metric("Progress", f"{percentage}%")

    st.progress(percentage / 100)

    if percentage == 100:
        st.success("Excellent! You have completed every skill in this list.")
    elif completed_count == 0:
        st.info("Start by completing a skill you have already learned.")
    else:
        st.info(
            f"{total_skills - completed_count} skills remaining. "
            "Keep learning one step at a time!"
        )
