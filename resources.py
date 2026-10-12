from urllib.parse import quote_plus


RESOURCE_CATALOG = {
    "Python": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Python Basics and Variables",
            "Data Types and Operators",
            "Conditions and Loops",
            "Functions and Modules",
            "Lists, Tuples, Sets and Dictionaries",
            "File Handling and Exceptions",
            "OOP and Projects",
            "NumPy, Pandas and Matplotlib",
        ],
        "courses": [
            {
                "title": "Python for Everybody",
                "url": "https://www.py4e.com/",
            },
            {
                "title": "Official Python Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
            },
        ],
        "books": [
            {
                "title": "Think Python - Free Online Book",
                "url": "https://allendowney.github.io/ThinkPython/",
            },
            {
                "title": "Official Python Documentation",
                "url": "https://docs.python.org/3/",
            },
        ],
    },
    "Machine Learning": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Python and NumPy",
            "Pandas and Data Visualization",
            "Basic Statistics and Probability",
            "Linear Regression",
            "Logistic Regression",
            "Decision Trees and Random Forest",
            "Model Evaluation and Feature Engineering",
            "Clustering and Unsupervised Learning",
            "End-to-End ML Projects",
        ],
        "courses": [
            {
                "title": "Google Machine Learning Crash Course",
                "url": "https://developers.google.com/machine-learning/crash-course",
            },
            {
                "title": "Scikit-learn Tutorials",
                "url": "https://scikit-learn.org/stable/tutorial/index.html",
            },
        ],
        "books": [
            {
                "title": "An Introduction to Statistical Learning",
                "url": "https://www.statlearning.com/",
            },
            {
                "title": "Scikit-learn User Guide",
                "url": "https://scikit-learn.org/stable/user_guide.html",
            },
        ],
    },
    "Artificial Intelligence": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Python Programming",
            "Math and Probability Basics",
            "Search Algorithms",
            "Knowledge Representation",
            "Machine Learning Fundamentals",
            "Neural Networks",
            "Natural Language Processing",
            "AI Applications and Projects",
        ],
        "courses": [
            {
                "title": "Elements of AI",
                "url": "https://www.elementsofai.com/",
            },
            {
                "title": "CS50 Introduction to AI with Python",
                "url": "https://cs50.harvard.edu/ai/",
            },
        ],
        "books": [
            {
                "title": "Artificial Intelligence: A Modern Approach",
                "url": "https://aima.cs.berkeley.edu/",
            },
        ],
    },
    "Generative AI": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Python and API Basics",
            "Neural Network Fundamentals",
            "Transformers and Attention",
            "Large Language Models",
            "Prompt Engineering",
            "Embeddings and Vector Search",
            "RAG Applications",
            "LLM Evaluation and Safety",
            "Build a Generative AI Project",
        ],
        "courses": [
            {
                "title": "Hugging Face Learn",
                "url": "https://huggingface.co/learn",
            },
            {
                "title": "Google Generative AI Learning",
                "url": "https://ai.google.dev/",
            },
        ],
        "books": [
            {
                "title": "Hugging Face NLP Course",
                "url": "https://huggingface.co/learn/llm-course/",
            },
            {
                "title": "Dive into Deep Learning",
                "url": "https://d2l.ai/",
            },
        ],
    },
    "RAG": {
        "level": "Intermediate to Advanced",
        "roadmap": [
            "Python and API Basics",
            "LLM Fundamentals",
            "Text Loading and Document Parsing",
            "Text Chunking",
            "Embeddings",
            "Vector Databases",
            "Retrieval and Similarity Search",
            "RAG Pipeline",
            "Evaluation and Hallucination Reduction",
            "Build a PDF Question-Answering App",
        ],
        "courses": [
            {
                "title": "LangChain Documentation",
                "url": "https://python.langchain.com/docs/",
            },
            {
                "title": "LlamaIndex Documentation",
                "url": "https://docs.llamaindex.ai/",
            },
        ],
        "books": [
            {
                "title": "Hugging Face LLM Course",
                "url": "https://huggingface.co/learn/llm-course/",
            },
            {
                "title": "Sentence Transformers Documentation",
                "url": "https://www.sbert.net/",
            },
        ],
    },
    "Agentic AI": {
        "level": "Intermediate to Advanced",
        "roadmap": [
            "Python and API Basics",
            "LLM and Prompt Engineering",
            "Tool Calling",
            "Structured Outputs",
            "Agent Planning and Execution",
            "Memory and Context",
            "Multi-Agent Concepts",
            "Human Approval and Safety",
            "Build and Evaluate an AI Agent",
        ],
        "courses": [
            {
                "title": "Hugging Face Agents Course",
                "url": "https://huggingface.co/learn/agents-course/",
            },
            {
                "title": "OpenAI Platform Documentation",
                "url": "https://platform.openai.com/docs/",
            },
        ],
        "books": [
            {
                "title": "LangGraph Documentation",
                "url": "https://docs.langchain.com/oss/python/langgraph/overview",
            },
            {
                "title": "AutoGen Documentation",
                "url": "https://microsoft.github.io/autogen/",
            },
        ],
    },
    "Data Analytics": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Excel Fundamentals",
            "SQL Queries",
            "Python Basics",
            "NumPy and Pandas",
            "Data Cleaning",
            "Exploratory Data Analysis",
            "Statistics and Visualization",
            "Power BI Dashboards",
            "Portfolio Analytics Projects",
        ],
        "courses": [
            {
                "title": "Kaggle Learn",
                "url": "https://www.kaggle.com/learn",
            },
            {
                "title": "Microsoft Learn - Power BI",
                "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/",
            },
        ],
        "books": [
            {
                "title": "Python Data Science Handbook",
                "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
            },
            {
                "title": "Pandas Documentation",
                "url": "https://pandas.pydata.org/docs/",
            },
        ],
    },
    "SQL": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Database Fundamentals",
            "SELECT and WHERE",
            "Sorting and Filtering",
            "Aggregate Functions",
            "GROUP BY and HAVING",
            "Joins and Subqueries",
            "CTEs and Window Functions",
            "Database Design",
            "SQL Projects",
        ],
        "courses": [
            {
                "title": "SQLBolt Interactive Lessons",
                "url": "https://sqlbolt.com/",
            },
            {
                "title": "PostgreSQL Tutorial",
                "url": "https://www.postgresql.org/docs/current/tutorial.html",
            },
        ],
        "books": [
            {
                "title": "PostgreSQL Documentation",
                "url": "https://www.postgresql.org/docs/",
            },
        ],
    },
    "Web Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "HTML",
            "CSS and Responsive Design",
            "JavaScript Fundamentals",
            "DOM and Browser APIs",
            "Git and GitHub",
            "React Fundamentals",
            "APIs and Backend Basics",
            "Database Integration",
            "Deployment and Projects",
        ],
        "courses": [
            {
                "title": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/",
            },
            {
                "title": "MDN Web Development",
                "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development",
            },
        ],
        "books": [
            {
                "title": "Eloquent JavaScript - Free Online Book",
                "url": "https://eloquentjavascript.net/",
            },
            {
                "title": "MDN Documentation",
                "url": "https://developer.mozilla.org/",
            },
        ],
    },
    "Power BI": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Power BI Interface",
            "Importing Data",
            "Data Cleaning with Power Query",
            "Data Modeling and Relationships",
            "DAX Fundamentals",
            "Charts and Dashboards",
            "Filters and Slicers",
            "Publishing Reports",
            "Build a Business Dashboard",
        ],
        "courses": [
            {
                "title": "Microsoft Learn Power BI",
                "url": "https://learn.microsoft.com/en-us/training/powerplatform/power-bi/",
            },
        ],
        "books": [
            {
                "title": "Power BI Documentation",
                "url": "https://learn.microsoft.com/en-us/power-bi/",
            },
        ],
    },
        "AWS Cloud Computing": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Cloud Computing Fundamentals",
            "AWS Global Infrastructure",
            "IAM and Permissions",
            "EC2 Virtual Servers",
            "S3 Storage",
            "VPC and Networking",
            "RDS Databases",
            "AWS Lambda",
            "CloudWatch Monitoring",
            "Security and Cost Management",
            "Deploy a Web Application on AWS",
        ],
        "courses": [
            {
                "title": "AWS Skill Builder",
                "url": "https://skillbuilder.aws/",
            },
            {
                "title": "AWS Getting Started",
                "url": "https://aws.amazon.com/getting-started/",
            },
        ],
        "books": [
            {
                "title": "AWS Documentation",
                "url": "https://docs.aws.amazon.com/",
            },
            {
                "title": "AWS Well-Architected Framework",
                "url": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
            },
        ],
    },

    "Full Stack Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "HTML Fundamentals",
            "CSS and Responsive Design",
            "JavaScript",
            "Git and GitHub",
            "React",
            "REST APIs",
            "Node.js and Express",
            "SQL or MongoDB",
            "Authentication",
            "Testing and Security",
            "Deployment",
            "Full Stack Project",
        ],
        "courses": [
            {
                "title": "The Odin Project",
                "url": "https://www.theodinproject.com/",
            },
            {
                "title": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/",
            },
        ],
        "books": [
            {
                "title": "Eloquent JavaScript",
                "url": "https://eloquentjavascript.net/",
            },
            {
                "title": "MDN Web Docs",
                "url": "https://developer.mozilla.org/",
            },
        ],
    },

    "Frontend Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "HTML",
            "CSS",
            "Responsive Web Design",
            "JavaScript ES6+",
            "DOM Manipulation",
            "Git and GitHub",
            "React",
            "React Hooks",
            "API Integration",
            "Testing and Accessibility",
            "Deployment",
            "Portfolio Project",
        ],
        "courses": [
            {
                "title": "React Learn",
                "url": "https://react.dev/learn",
            },
            {
                "title": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/",
            },
        ],
        "books": [
            {
                "title": "Eloquent JavaScript",
                "url": "https://eloquentjavascript.net/",
            },
            {
                "title": "MDN Web Development",
                "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development",
            },
        ],
    },

    "Backend Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Programming Fundamentals",
            "HTTP and REST APIs",
            "Python or Node.js",
            "Backend Framework",
            "SQL and Database Design",
            "Authentication",
            "API Validation",
            "Testing",
            "Security",
            "Deployment",
            "Backend Project",
        ],
        "courses": [
            {
                "title": "Node.js Learning",
                "url": "https://nodejs.org/en/learn",
            },
            {
                "title": "FastAPI Tutorial",
                "url": "https://fastapi.tiangolo.com/tutorial/",
            },
        ],
        "books": [
            {
                "title": "FastAPI Documentation",
                "url": "https://fastapi.tiangolo.com/",
            },
        ],
    },

    "DevOps": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Linux Fundamentals",
            "Git and GitHub",
            "Networking Basics",
            "Shell Scripting",
            "Docker",
            "CI/CD Fundamentals",
            "GitHub Actions",
            "Cloud Computing",
            "Infrastructure as Code",
            "Monitoring",
            "Kubernetes Fundamentals",
            "Deployment Project",
        ],
        "courses": [
            {
                "title": "Docker Get Started",
                "url": "https://docs.docker.com/get-started/",
            },
            {
                "title": "GitHub Actions",
                "url": "https://docs.github.com/en/actions",
            },
        ],
        "books": [
            {
                "title": "Pro Git - Free Online Book",
                "url": "https://git-scm.com/book/en/v2",
            },
            {
                "title": "Kubernetes Documentation",
                "url": "https://kubernetes.io/docs/home/",
            },
        ],
    },
    "Cybersecurity": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Computer and Network Fundamentals",
            "Linux Basics",
            "Security Principles",
            "Web Security Fundamentals",
            "Identity and Access Management",
            "Defensive Security and Logging",
            "Incident Response",
            "Practice in Legal Labs",
        ],
    },    
    "Full Stack Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "HTML Fundamentals",
            "CSS, Flexbox, Grid and Responsive Design",
            "JavaScript Fundamentals",
            "Git and GitHub",
            "React and Component Design",
            "API Integration and Fetch",
            "Node.js and Express",
            "SQL or MongoDB",
            "Authentication and Authorization",
            "Testing and Security Basics",
            "Deployment and CI/CD",
            "Build a Complete Full Stack Project",
        ],
        "courses": [
            {
                "title": "The Odin Project",
                "url": "https://www.theodinproject.com/",
            },
            {
                "title": "freeCodeCamp",
                "url": "https://www.freecodecamp.org/learn/",
            },
        ],
        "books": [
            {
                "title": "Eloquent JavaScript",
                "url": "https://eloquentjavascript.net/",
            },
            {
                "title": "MDN Web Docs",
                "url": "https://developer.mozilla.org/",
            },
        ],
    },

    "Frontend Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "HTML and Semantic Markup",
            "CSS Fundamentals",
            "Responsive Web Design",
            "JavaScript ES6+",
            "DOM and Browser APIs",
            "Git and GitHub",
            "React Fundamentals",
            "React Hooks and Routing",
            "API Integration",
            "Accessibility and Testing",
            "Frontend Deployment",
            "Build a Portfolio Website",
        ],
        "courses": [
            {
                "title": "freeCodeCamp Frontend Learning",
                "url": "https://www.freecodecamp.org/learn/",
            },
            {
                "title": "React Official Learn Guide",
                "url": "https://react.dev/learn",
            },
        ],
        "books": [
            {
                "title": "Eloquent JavaScript",
                "url": "https://eloquentjavascript.net/",
            },
            {
                "title": "MDN HTML, CSS and JavaScript",
                "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development",
            },
        ],
    },

    "Backend Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Programming Fundamentals",
            "HTTP and REST APIs",
            "Node.js or Python",
            "Backend Frameworks",
            "SQL and Database Design",
            "Authentication and Authorization",
            "API Validation and Error Handling",
            "Testing and Logging",
            "Security Fundamentals",
            "Deployment and Monitoring",
            "Build a REST API Project",
        ],
        "courses": [
            {
                "title": "Node.js Official Guides",
                "url": "https://nodejs.org/en/learn",
            },
            {
                "title": "FastAPI Tutorial",
                "url": "https://fastapi.tiangolo.com/tutorial/",
            },
        ],
        "books": [
            {
                "title": "MDN Server-side Website Programming",
                "url": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side",
            },
            {
                "title": "FastAPI Documentation",
                "url": "https://fastapi.tiangolo.com/",
            },
        ],
    },

    "AWS Cloud Computing": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Cloud Computing Fundamentals",
            "AWS Global Infrastructure",
            "IAM Users, Roles and Permissions",
            "EC2 and Virtual Servers",
            "S3 Storage and Bucket Permissions",
            "VPC and Networking Basics",
            "RDS and Database Services",
            "Lambda and Serverless Computing",
            "CloudWatch Monitoring",
            "Security and Cost Management",
            "Deploy a Web Application on AWS",
            "Prepare for an AWS Certification",
        ],
        "courses": [
            {
                "title": "AWS Skill Builder",
                "url": "https://skillbuilder.aws/",
            },
            {
                "title": "AWS Getting Started",
                "url": "https://aws.amazon.com/getting-started/",
            },
        ],
        "books": [
            {
                "title": "AWS Documentation",
                "url": "https://docs.aws.amazon.com/",
            },
            {
                "title": "AWS Well-Architected Framework",
                "url": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
            },
        ],
    },

    "DevOps": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Linux and Command Line",
            "Git and GitHub",
            "Networking Fundamentals",
            "Python or Shell Scripting",
            "Docker Containers",
            "CI/CD Fundamentals",
            "GitHub Actions",
            "Cloud Fundamentals",
            "Infrastructure as Code",
            "Monitoring and Logging",
            "Kubernetes Fundamentals",
            "Build a CI/CD Deployment Project",
        ],
        "courses": [
            {
                "title": "Docker Get Started",
                "url": "https://docs.docker.com/get-started/",
            },
            {
                "title": "GitHub Actions Documentation",
                "url": "https://docs.github.com/en/actions",
            },
        ],
        "books": [
            {
                "title": "Pro Git - Free Online Book",
                "url": "https://git-scm.com/book/en/v2",
            },
            {
                "title": "Kubernetes Documentation",
                "url": "https://kubernetes.io/docs/home/",
            },
        ],
    },

    "Data Science": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Python Fundamentals",
            "NumPy and Pandas",
            "Statistics and Probability",
            "Data Cleaning",
            "Exploratory Data Analysis",
            "Data Visualization",
            "Feature Engineering",
            "Machine Learning",
            "Model Evaluation",
            "Experiment Tracking",
            "Deploy a Data Science Project",
        ],
        "courses": [
            {
                "title": "Kaggle Learn",
                "url": "https://www.kaggle.com/learn",
            },
            {
                "title": "IBM SkillsBuild",
                "url": "https://skillsbuild.org/",
            },
        ],
        "books": [
            {
                "title": "Python Data Science Handbook",
                "url": "https://jakevdp.github.io/PythonDataScienceHandbook/",
            },
            {
                "title": "An Introduction to Statistical Learning",
                "url": "https://www.statlearning.com/",
            },
        ],
    },

    "Deep Learning": {
        "level": "Intermediate to Advanced",
        "roadmap": [
            "Python and NumPy",
            "Linear Algebra and Calculus Basics",
            "Probability and Statistics",
            "Neural Network Fundamentals",
            "Backpropagation and Optimization",
            "PyTorch or TensorFlow",
            "Convolutional Neural Networks",
            "Sequence Models and Transformers",
            "Transfer Learning",
            "Model Evaluation and Deployment",
            "Build a Deep Learning Project",
        ],
        "courses": [
            {
                "title": "PyTorch Tutorials",
                "url": "https://pytorch.org/tutorials/",
            },
            {
                "title": "TensorFlow Tutorials",
                "url": "https://www.tensorflow.org/tutorials",
            },
        ],
        "books": [
            {
                "title": "Dive into Deep Learning",
                "url": "https://d2l.ai/",
            },
            {
                "title": "Neural Networks and Deep Learning",
                "url": "http://neuralnetworksanddeeplearning.com/",
            },
        ],
    },

    "Computer Vision": {
        "level": "Intermediate to Advanced",
        "roadmap": [
            "Python and NumPy",
            "Image Representation and Color Spaces",
            "OpenCV Fundamentals",
            "Image Processing",
            "Feature Detection",
            "Convolutional Neural Networks",
            "Transfer Learning",
            "Object Detection",
            "Image Segmentation",
            "Build an Image Recognition Project",
        ],
        "courses": [
            {
                "title": "OpenCV Tutorials",
                "url": "https://docs.opencv.org/4.x/d9/df8/tutorial_root.html",
            },
            {
                "title": "PyTorch Tutorials",
                "url": "https://pytorch.org/tutorials/",
            },
        ],
        "books": [
            {
                "title": "Dive into Deep Learning",
                "url": "https://d2l.ai/",
            },
        ],
    },

    "Natural Language Processing": {
        "level": "Intermediate to Advanced",
        "roadmap": [
            "Python Fundamentals",
            "Text Cleaning and Tokenization",
            "Regular Expressions",
            "Text Vectorization",
            "Word Embeddings",
            "Text Classification",
            "Attention and Transformers",
            "Hugging Face Transformers",
            "Evaluation Metrics",
            "Build a Text Analysis Project",
        ],
        "courses": [
            {
                "title": "Hugging Face NLP Course",
                "url": "https://huggingface.co/learn/llm-course/",
            },
            {
                "title": "NLTK Book",
                "url": "https://www.nltk.org/book/",
            },
        ],
        "books": [
            {
                "title": "NLTK Book - Free Online",
                "url": "https://www.nltk.org/book/",
            },
            {
                "title": "spaCy Documentation",
                "url": "https://spacy.io/usage",
            },
        ],
    },

    "Java Programming": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Java Setup and Syntax",
            "Variables and Data Types",
            "Conditions and Loops",
            "Methods and Arrays",
            "Object-Oriented Programming",
            "Collections Framework",
            "Exception Handling",
            "File Handling",
            "Generics and Streams",
            "Unit Testing",
            "Build a Java Project",
        ],
        "courses": [
            {
                "title": "University of Helsinki Java MOOC",
                "url": "https://java-programming.mooc.fi/",
            },
            {
                "title": "Dev.java Learning",
                "url": "https://dev.java/learn/",
            },
        ],
        "books": [
            {
                "title": "Dev.java Documentation",
                "url": "https://dev.java/",
            },
        ],
    },

    "C++ Programming": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "C++ Syntax and Variables",
            "Conditions and Loops",
            "Functions",
            "Arrays and Strings",
            "Pointers and References",
            "Object-Oriented Programming",
            "STL Containers",
            "Algorithms and Complexity",
            "Memory Management",
            "Data Structures and Algorithms",
            "Build a C++ Project",
        ],
        "courses": [
            {
                "title": "LearnCpp",
                "url": "https://www.learncpp.com/",
            },
            {
                "title": "C++ Reference",
                "url": "https://en.cppreference.com/",
            },
        ],
        "books": [
            {
                "title": "LearnCpp Online Tutorial",
                "url": "https://www.learncpp.com/",
            },
        ],
    },

    "Android Development": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Kotlin Fundamentals",
            "Android Studio Setup",
            "Layouts and UI Components",
            "Activities and App Lifecycle",
            "Navigation",
            "Local Data Storage",
            "Networking and APIs",
            "Jetpack Compose",
            "Testing and Debugging",
            "Build and Publish a Demo App",
        ],
        "courses": [
            {
                "title": "Android Developers Training",
                "url": "https://developer.android.com/courses",
            },
            {
                "title": "Kotlin Documentation",
                "url": "https://kotlinlang.org/docs/home.html",
            },
        ],
        "books": [
            {
                "title": "Android Developers Documentation",
                "url": "https://developer.android.com/docs",
            },
        ],
    },



    "Cybersecurity": {
        "level": "Beginner to Advanced",
        "roadmap": [
            "Computer and Network Fundamentals",
            "Linux Basics",
            "Security Principles",
            "Web Security Fundamentals",
            "Identity and Access Management",
            "Defensive Security and Logging",
            "Incident Response",
            "Practice in Legal Labs",
        ],
        "courses": [
            {
                "title": "Cisco Networking Academy",
                "url": "https://www.netacad.com/",
            },
            {
                "title": "PortSwigger Web Security Academy",
                "url": "https://portswigger.net/web-security",
            },
        ],
        "books": [
            {
                "title": "OWASP Web Security Testing Guide",
                "url": "https://owasp.org/www-project-web-security-testing-guide/",
            },
        ],
    },
}
def get_learning_resources(skill):
    """Return learning links for a skill."""

    if not isinstance(skill, str) or not skill.strip():
        return []

    requested = skill.strip().lower()

    for name, details in RESOURCE_CATALOG.items():
        if requested == name.lower():
            resources = []

            for item in details.get("courses", []):
                resources.append({
                    "title": item.get("title", "Free Course"),
                    "url": item.get("url", ""),
                    "type": "Course",
                })

            for item in details.get("books", []):
                resources.append({
                    "title": item.get("title", "Documentation"),
                    "url": item.get("url", ""),
                    "type": "Book / Documentation",
                })

            youtube_url = (
                "https://www.youtube.com/results?search_query="
                + quote_plus(name + " full course tutorial")
            )

            resources.append({
                "title": f"{name} YouTube Tutorials",
                "url": youtube_url,
                "type": "YouTube",
            })

            return resources

    youtube_url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(skill.strip() + " full course tutorial")
    )

    return [{
        "title": f"{skill.strip()} YouTube Tutorials",
        "url": youtube_url,
        "type": "YouTube",
    }]


def get_learning_roadmap(skill):
    """Return an ordered roadmap for the selected skill."""

    if not isinstance(skill, str) or not skill.strip():
        return []

    requested = skill.strip().lower()

    for name, details in RESOURCE_CATALOG.items():
        if requested == name.lower():
            return list(details.get("roadmap", []))

    return []


def get_all_skills():
    """Return all skills available in the learning catalog."""

    return sorted(RESOURCE_CATALOG.keys(), key=str.lower)

