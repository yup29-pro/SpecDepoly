import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def build_pipeline(spec: str, code_files: dict) -> str:
    print("🤖 Pipeline Builder Agent started...")

    filenames = [f["filename"] for f in code_files["files"]]

    prompt = f"""
You are a senior DevOps engineer.
Create a GitHub Actions CI/CD pipeline for this feature.

Feature Spec Summary:
{spec[:500]}

Files generated:
{filenames}

Generate a complete .github/workflows/ci.yml file that:
1. Triggers on pull_request
2. Sets up Python environment
3. Installs dependencies
4. Runs tests
5. Runs linting

Return ONLY the raw YAML content, no explanation, no markdown backticks.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert DevOps engineer. Return only raw YAML."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000,
        temperature=0.2
    )

    pipeline = response.choices[0].message.content
    print("✅ Pipeline Builder completed!")
    return pipeline
