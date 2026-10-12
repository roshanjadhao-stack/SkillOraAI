
"""Skill catalog for SkillOra AI."""

from student_auth import get_connection


SKILLS = [
    ("AI & Machine Learning", "Python for AI", "Beginner", "Python syntax, functions, files, virtual environments and packages.", "Build a command-line study planner."),
    ("AI & Machine Learning", "Machine Learning", "Intermediate", "Supervised learning, preprocessing, train/test split and model evaluation.", "Build a student-score prediction model."),
    ("AI & Machine Learning", "Deep Learning", "Advanced", "Neural networks, training loops, CNNs and model evaluation.", "Classify images with a small dataset."),
    ("AI & Machine Learning", "Generative AI, LLM & RAG", "Intermediate", "Prompting, embeddings, retrieval, chunking, vector search and grounded answers.", "Build a document Q&A prototype."),
    ("AI & Machine Learning", "Data Science & Analytics", "Beginner", "Pandas, visualization, statistics, SQL and communicating insights.", "Create an exploratory data analysis report."),
    ("Full Stack & Web Development", "HTML & CSS", "Beginner", "Semantic HTML, responsive layouts, accessibility and modern CSS.", "Build a responsive personal portfolio."),
    ("Full Stack & Web Development", "JavaScript", "Beginner", "Variables, functions, DOM, async code and browser APIs.", "Build a task tracker."),
    ("Full Stack & Web Development", "React", "Intermediate", "Components, props, state, hooks, routing and forms.", "Build a searchable learning dashboard."),
    ("Full Stack & Web Development", "Node.js & Express", "Intermediate", "HTTP, routing, middleware, validation and REST APIs.", "Create a CRUD API for learning resources."),
    ("Full Stack & Web Development", "Databases & SQL", "Beginner", "Tables, keys, joins, indexes, constraints and safe queries.", "Design a course catalogue database."),
    ("IT & Computer Science", "C & C++", "Beginner", "Programming basics, functions, arrays, pointers and OOP.", "Build a console-based inventory app."),
    ("IT & Computer Science", "Java", "Beginner", "OOP, collections, exceptions, file handling and testing.", "Build a library management prototype."),
    ("IT & Computer Science", "DSA", "Intermediate", "Arrays, linked lists, stacks, queues, trees, graphs and complexity.", "Implement and test common data structures."),
    ("IT & Computer Science", "Git & GitHub", "Beginner", "Commits, branches, pull requests, README files and collaboration.", "Publish a project with a clear README."),
    ("Cloud & Cybersecurity", "Cloud Fundamentals", "Beginner", "Compute, storage, networking, IAM and deployment basics.", "Deploy a small static site."),
    ("Cloud & Cybersecurity", "Cybersecurity Fundamentals", "Beginner", "Security principles, authentication, threat awareness and safe labs.", "Create a personal security checklist."),
    ("Mechanical Engineering", "AutoCAD", "Beginner", "2D drafting, dimensions, layers, blocks and technical drawings.", "Prepare a dimensioned component drawing."),
    ("Mechanical Engineering", "SolidWorks / CAD", "Intermediate", "Part modelling, assemblies, drawings and design intent.", "Model a small mechanical assembly."),
    ("Mechanical Engineering", "CNC & Manufacturing", "Intermediate", "Manufacturing processes, tooling, tolerances and quality basics.", "Prepare a process-planning sheet."),
    ("Mechanical Engineering", "Thermodynamics & Fluid Mechanics", "Intermediate", "Core concepts, cycles, fluid properties and engineering calculations.", "Create a worked engineering calculation notebook."),
    ("Mechanical Engineering", "Robotics & Automation", "Intermediate", "Sensors, actuators, control basics and safe automation concepts.", "Prototype a simple sensor-based automation demo."),
    ("Civil Engineering", "AutoCAD Civil 3D", "Intermediate", "Drafting, site layouts, surfaces and basic civil workflows.", "Create a sample site layout."),
    ("Civil Engineering", "Revit & BIM", "Intermediate", "Building information modelling, families, views and schedules.", "Model a small building concept."),
    ("Civil Engineering", "Structural Analysis", "Intermediate", "Loads, supports, structural behaviour and analysis fundamentals.", "Prepare a clearly documented simple frame study."),
    ("Civil Engineering", "Estimation & Quantity Surveying", "Beginner", "Quantity take-off, BOQ, rate analysis and cost estimation.", "Create a sample bill of quantities."),
    ("Electrical & Electronics", "MATLAB & Simulink", "Intermediate", "Numerical computing, plotting, simulation and model blocks.", "Simulate a basic system response."),
    ("Electrical & Electronics", "PLC & Industrial Automation", "Intermediate", "Control logic, sensors, interlocks and industrial safety principles.", "Design a simulated conveyor logic flow."),
    ("Electrical & Electronics", "Embedded Systems & IoT", "Intermediate", "Microcontrollers, sensors, serial communication and connectivity.", "Build a sensor dashboard prototype."),
    ("Electrical & Electronics", "Electronics & PCB Basics", "Beginner", "Circuit fundamentals, components, schematics and PCB workflow.", "Design a simple low-voltage learning circuit."),
    ("Design & Creative", "UI/UX Design", "Beginner", "User research, flows, wireframes, prototypes and usability.", "Prototype a student resource app."),
    ("Design & Creative", "Graphic Design", "Beginner", "Layout, typography, hierarchy, colour and visual communication.", "Create a consistent event poster set."),
    ("Business & Non-Tech", "Digital Marketing", "Beginner", "Audience, content strategy, SEO basics and campaign measurement.", "Plan a one-week content calendar."),
    ("Business & Non-Tech", "Excel & Power BI", "Beginner", "Spreadsheets, cleaning, formulas, dashboards and data storytelling.", "Build a simple student progress dashboard."),
    ("Business & Non-Tech", "Communication & Spoken English", "Beginner", "Introductions, clear writing, speaking practice and interview answers.", "Record and review a short project introduction."),
    ("Business & Non-Tech", "Entrepreneurship & Product Management", "Intermediate", "Problem discovery, value proposition, user feedback and planning.", "Draft a one-page product concept."),
    ("Government Exams & Higher Studies", "GATE Preparation", "Intermediate", "Syllabus mapping, concept revision, practice questions and mock tests.", "Create a weekly subject revision plan."),
    ("Government Exams & Higher Studies", "MPSC / UPSC Foundation", "Beginner", "Understand the official syllabus, current affairs, foundational subjects and practice.", "Prepare a syllabus-based weekly study tracker."),
    ("Government Exams & Higher Studies", "Aptitude & Reasoning", "Beginner", "Quantitative aptitude, logical reasoning, accuracy and timed practice.", "Maintain a topic-wise practice log."),
    ("Career Readiness", "Resume & Interview Preparation", "Beginner", "ATS-friendly resume writing, project explanations and mock interviews.", "Prepare a project-focused resume draft."),
    ("Career Readiness", "Placement Coding Practice", "Intermediate", "Problem solving, complexity, core CS concepts and interview practice.", "Complete a topic-wise coding practice set."),
]


def make_skill_id(category, name):
    """Create a stable ID for a skill."""
    return (
        category + "-" + name
    ).lower().replace(" & ", "-").replace(
        " / ", "-"
    ).replace(" ", "-")


def seed_skills():
    """Insert catalog skills without duplicating existing records."""
    with get_connection() as con:
        for category, name, level, description, project in SKILLS:
            skill_id = make_skill_id(category, name)

            con.execute(
                """
                INSERT OR IGNORE INTO skills
                    (id, category, name, level, description, project)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    skill_id,
                    category,
                    name,
                    level,
                    description,
                    project,
                ),
            )


def get_all_skills():
    """Return all catalog skills."""
    with get_connection() as con:
        return con.execute(
            """
            SELECT id, category, name, level, description, project
            FROM skills
            ORDER BY category, name
            """
        ).fetchall()


def get_skill_categories():
    """Return the available skill categories."""
    with get_connection() as con:
        rows = con.execute(
            """
            SELECT DISTINCT category
            FROM skills
            ORDER BY category
            """
        ).fetchall()

    return [row["category"] for row in rows]


def search_skills(query="", category="All", level="All"):
    """Search skills by name, category, description or project."""
    sql = """
        SELECT id, category, name, level, description, project
        FROM skills
        WHERE 1 = 1
    """
    params = []

    if query.strip():
        term = f"%{query.strip()}%"
        sql += """
            AND (
                name LIKE ?
                OR category LIKE ?
                OR description LIKE ?
                OR project LIKE ?
            )
        """
        params.extend([term, term, term, term])

    if category != "All":
        sql += " AND category = ?"
        params.append(category)

    if level != "All":
        sql += " AND level = ?"
        params.append(level)

    sql += " ORDER BY category, name"

    with get_connection() as con:
        return con.execute(sql, params).fetchall()


def get_learning_links(skill_name):
    """Generate useful YouTube and PDF search links."""
    from urllib.parse import quote_plus

    query = quote_plus(skill_name)

    return {
        "youtube": f"https://www.youtube.com/results?search_query={query}+tutorial",
        "pdf": f"https://www.google.com/search?q={query}+tutorial+filetype%3Apdf",
    }
