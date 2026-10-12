
import pytest

from model import load_careers, recommend_careers


def test_dataset_is_valid():
    careers = load_careers()

    assert not careers.empty
    assert careers["career"].is_unique


def test_recommendations_are_ranked():
    results = recommend_careers(
        [
            "python",
            "machine learning",
            "scikit-learn",
            "model evaluation",
            "pandas",
            "numpy",
            "statistics",
            "sql",
        ]
    )

    assert not results.empty
    assert results["match_score"].between(0, 100).all()
    assert results.iloc[0]["career"] == "Machine Learning Engineer"


def test_skill_gap_columns_exist():
    results = recommend_careers(["python"])

    assert "matched_skills" in results.columns
    assert "missing_skills" in results.columns
    assert "skill_coverage" in results.columns


def test_empty_input_is_rejected():
    with pytest.raises(ValueError):
        recommend_careers([])


def test_unknown_skill_does_not_crash():
    results = recommend_careers(["an-unlisted-skill"])

    assert not results.empty

