import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def scaffold_code(spec: str) -> dict:
    print("🤖 Code Scaffolder Agent started...")

    prompt = f"""
You are a senior software engineer.
Based on this feature specification, generate the actual implementation code.

SPEC:
{spec}

Generate a Python/JavaScript implementation with:
1. Main feature file (e.g., auth/google.py or auth/google.js)
2. Route/endpoint file
3. Config file if needed

Return ONLY a JSON object like this:
{{
  "files": [
    {{
      "filename": "auth/google.py",
      "content": "# full code here"
    }},
    {{
      "filename": "routes/auth.py", 
      "content": "# full code here"
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
                "content": "You are an expert software engineer. Always return valid JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=3000,
        temperature=0.3
    )

    import json
    raw = response.choices[0].message.content
    
    try:
        result = json.loads(raw)
    except:
        result = {"files": [{"filename": "output.py", "content": raw}]}

    print(f"✅ Code Scaffolder completed! Generated {len(result['files'])} files")
    return result
