from pathlib import Path

path = Path("app.py")
text = path.read_text(encoding="utf-8")

replacements = {
    "ðŸŽ¯": "🎯",
    "ðŸ§": "🧭",
    "ðŸ› ï¸": "🛠️",
    "ðŸš€": "🚀",
    "ðŸ“Š": "📊",
    "â€¢": "•",
    "â€”": "—",
    "âœ¨": "✨",
    "ðŸ“ˆ": "📈",
    "ðŸ“„": "📄",
    "â¬‡ï¸": "⬇️",
    "ðŸ‘‹": "👋",
}

for old, new in replacements.items():
    text = text.replace(old, new)

path.write_text(text, encoding="utf-8")
print("Encoding cleanup completed.")
