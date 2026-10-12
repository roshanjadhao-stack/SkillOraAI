from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DATA_PATH = Path(__file__).parent / "careers.csv"


def load_careers():
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


def recommend_careers(user_skills):
    careers = load_careers()

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

    documents = (
        careers["description"].fillna("").astype(str)
        + " "
        + careers["skills"].fillna("").str.replace(";", " ", regex=False)
    ).tolist()

    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
    )

    career_vectors = vectorizer.fit_transform(documents)
    user_vector = vectorizer.transform([" ".join(skills)])

    scores = cosine_similarity(
        user_vector, career_vectors
    ).flatten()

    careers["match_score"] = scores * 100

    careers = careers.sort_values(
        [
            "exact_skill_matches",
            "skill_coverage",
            "match_score",
        ],
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
