from pathlib import Path

path = Path("app.py")
text = path.read_text(encoding="utf-8")

text = text.replace(
    "use_container_width=True",
    'width="stretch"'
)
text = text.replace(
    "use_container_width=False",
    'width="content"'
)

path.write_text(text, encoding="utf-8")
print("Streamlit width warnings fixed in app.py")
