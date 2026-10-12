from pathlib import Path
import re
import math

import pandas as pd


DATA_PATH = Path(__file__).parent / "careers.csv"


def load_careers():
    """Load and validate the career dataset."""
    df = pd.read_csv(DATA_PATH)

    required = {
        "career",
        "description",
        "skills",
        "level",
        "learning_resources",
    }

    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")

    if df.empty or df["career"].isna().any():
        raise ValueError("Career dataset is empty or invalid.")

    if df["career"].duplicated().any():
        raise ValueError("Career names must be unique.")

    df["skill_list"] = df["skills"].fillna("").apply(
        lambda value: list(
            dict.fromkeys(
                skill.strip().lower()
                for skill in str(value).split(";")
                if skill.strip()
            )
        )
    )

    return df


def _tokenize(text):
    """Convert text into simple lowercase word tokens."""
    return re.findall(r"\b[a-zA-Z0-9+#.]+\b", str(text).lower())


def _text_similarity(user_text, career_text):
    """Calculate a lightweight token-based cosine similarity without sklearn."""
    user_tokens = _tokenize(user_text)
    career_tokens = _tokenize(career_text)

    if not user_tokens or not career_tokens:
        return 0.0

    user_counts = {}
    career_counts = {}

    for token in user_tokens:
        user_counts[token] = user_counts.get(token, 0) + 1

    for token in career_tokens:
        career_counts[token] = career_counts.get(token, 0) + 1

    common = set(user_counts).intersection(career_counts)
    dot_product = sum(user_counts[token] * career_counts[token] for token in common)

    user_norm = math.sqrt(sum(count * count for count in user_counts.values()))
    career_norm = math.sqrt(sum(count * count for count in career_counts.values()))

    if user_norm == 0 or career_norm == 0:
        return 0.0

    return dot_product / (user_norm * career_norm)


def recommend_careers(user_skills):
    """Rank careers using exact skill matches, skill coverage, and text similarity."""
    careers = load_careers()

    if isinstance(user_skills, str):
        user_skills = [user_skills]

    skills = list(
        dict.fromkeys(
            skill.strip().lower()
            for skill in user_skills
            if isinstance(skill, str) and skill.strip()
        )
    )

    if not skills:
        raise ValueError("Please enter at least one skill.")

    user_skill_set = set(skills)

    careers["exact_skill_matches"] = careers["skill_list"].apply(
        lambda required: len(user_skill_set.intersection(required))
    )

    careers["matched_skills"] = careers["skill_list"].apply(
        lambda required: sorted(user_skill_set.intersection(required))
    )

    careers["missing_skills"] = careers["skill_list"].apply(
        lambda required: sorted(set(required) - user_skill_set)
    )

    careers["skill_coverage"] = careers["skill_list"].apply(
        lambda required: (
            100 * len(user_skill_set.intersection(required)) / len(required)
            if required else 0.0
        )
    )

    user_text = " ".join(skills)
    documents = (
        careers["description"].fillna("").astype(str)
        + " "
        + careers["skills"].fillna("").str.replace(";", " ", regex=False)
    ).tolist()

    careers["match_score"] = [
        _text_similarity(user_text, document) * 100
        for document in documents
    ]

    careers = careers.sort_values(
        ["exact_skill_matches", "skill_coverage", "match_score"],
        ascending=[False, False, False],
        kind="stable",
    ).reset_index(drop=True)

    return careers


def create_learning_roadmap(career_row):
    """Create roadmap steps from the selected career's missing skills."""
    missing_skills = career_row.get("missing_skills", [])

    if not isinstance(missing_skills, (list, tuple)):
        missing_skills = []

    roadmap = []

    for step_number, skill in enumerate(missing_skills, start=1):
        cleaned_skill = str(skill).strip()
        if cleaned_skill:
            roadmap.append(
                {
                    "step": step_number,
                    "skill": cleaned_skill.title(),
                    "status": "Not Started",
                }
            )

    return roadmap
