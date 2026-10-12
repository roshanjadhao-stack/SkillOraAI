
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

try:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("ERROR: API key not found in .env")
    else:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            messages=[
                {
                    "role": "user",
                    "content": "Explain machine learning in one simple sentence."
                }
            ],
        )

        print("AI CONNECTION SUCCESSFUL!")
        print(response.choices[0].message.content)

except Exception as error:
    print("AI CONNECTION FAILED")
    print(type(error).__name__)
    print(error)
