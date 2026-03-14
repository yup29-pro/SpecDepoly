import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def write_tests(code_files: dict) -> dict:  # sourcery skip: use-join
    print("🤖 Test Writer Agent started...")

    files_content = ""
    for file in code_files["files"]:
        files_content += f"\n\n# File: {file['filename']}\n{file['content']}"

    prompt = f"""
You are a senior QA engineer and test automation expert.
Write comprehensive tests for the following code:

{files_content}

Generate pytest test files that cover:
1. Happy path (success cases)
2. Error cases
3. Edge cases

Return ONLY a JSON object like this:
{{
  "files": [
    {{
      "filename": "tests/test_auth.py",
      "content": "# full test code here"
    }}
  ]
}}

Return ONLY the JSON, no explanation, no markdown backticks.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert QA engineer. Always return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=2000,
        temperature=0.3
    )

    import json
    raw = response.choices[0].message.content

    try:
        result = json.loads(raw)
    except:
        result = {"files": [{"filename": "tests/test_output.py", "content": raw}]}

    print(f"✅ Test Writer completed! Generated {len(result['files'])} test files")
    return result
