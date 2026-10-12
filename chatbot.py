
def get_career_guidance(
    question,
    user_skills=None,
    career=None,
    missing_skills=None,
):
    question = (question or "").strip().lower()
    user_skills = user_skills or []
    missing_skills = missing_skills or []

    if not question:
        return "Please type a career or learning question."

    skills = ", ".join(user_skills) or "Not provided"
    gaps = ", ".join(missing_skills) or "None listed"
    selected_career = career or "Not selected"

    if question in ["hello", "hi", "hey", "namaste", "hello there", "hi there"]:
        return (
            "Hello! 👋 Welcome to Skillora AI Career Assistant.\n\n"
            "I can help you with career guidance, Python, AI/ML, "
            "skill gaps, projects, interviews, and learning roadmaps.\n\n"
            "Try asking: What should I learn next?"
        )

    if any(word in question for word in ["my skills", "my skill", "skills do i have"]):
        return (
            f"### Your Skills\n{skills}\n\n"
            f"**Selected career:** {selected_career}"
        )

    if any(word in question for word in ["missing skill", "skill gap", "learn next"]):
        return (
            f"### Your Skill Gap Guidance\n\n"
            f"**Career:** {selected_career}\n\n"
            f"**Skills to consider learning:** {gaps}\n\n"
            "Start with one skill. Learn the basics, practise with "
            "small exercises, and then build a mini-project."
        )

    if any(word in question for word in ["machine learning", "ml engineer", "artificial intelligence"]):
        return (
            "### AI and Machine Learning Roadmap\n\n"
            "1. Learn Python fundamentals.\n"
            "2. Practise NumPy and Pandas.\n"
            "3. Understand basic statistics and linear algebra.\n"
            "4. Learn regression and classification.\n"
            "5. Practise model evaluation with scikit-learn.\n"
            "6. Build a beginner ML project.\n"
            "7. Create a portfolio and explain your project clearly.\n\n"
            "**Project idea:** Student marks prediction using sample data."
        )

    if any(word in question for word in ["python", "learn coding"]):
        return (
            "### Python Beginner Roadmap\n\n"
            "1. Variables and data types.\n"
            "2. Conditions and loops.\n"
            "3. Lists, dictionaries, and sets.\n"
            "4. Functions and modules.\n"
            "5. File handling and exceptions.\n"
            "6. Practise small programs.\n"
            "7. Build a mini-project."
        )

    if any(word in question for word in ["interview", "resume", "placement"]):
        return (
            "### Interview Preparation\n\n"
            "1. Prepare your self-introduction.\n"
            "2. Revise skills relevant to the role.\n"
            "3. Practise explaining one project.\n"
            "4. Review basic technical questions.\n"
            "5. Practise speaking clearly and confidently.\n\n"
            "Tip: Use real examples from your own experience."
        )

    if any(word in question for word in ["roadmap", "study plan", "learning plan"]):
        first_gap = (
            missing_skills[0]
            if missing_skills
            else "a core skill for your target career"
        )
        return (
            f"### Your Starter Learning Plan\n\n"
            f"**Target career:** {selected_career}\n\n"
            f"**First skill to consider:** {first_gap}\n\n"
            "1. Learn the basics.\n"
            "2. Follow a beginner tutorial.\n"
            "3. Practise with exercises.\n"
            "4. Build a small project.\n"
            "5. Review your progress."
        )

    return (
        "### Skillora AI Career Assistant\n\n"
        "I can help with Python, AI/ML, career options, skill gaps, "
        "learning roadmaps, projects, and interviews.\n\n"
        f"**Current career:** {selected_career}\n\n"
        f"**Your skills:** {skills}\n\n"
        f"**Skills to consider learning:** {gaps}\n\n"
        "Try asking: 'Explain Machine Learning' or "
        "'Create a learning roadmap'."
    )
