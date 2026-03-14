import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def write_spec(feature_request: str) -> str:
    print(f"🤖 Spec Writer Agent started for: {feature_request}")
    
    prompt = f"""
You are a senior product manager and software architect.
A developer has requested the following feature:

"{feature_request}"

Write a complete, professional feature specification in markdown format with these sections:

# Feature: [Feature Name]

## Overview
[2-3 sentence summary]

## User Stories
- As a [user], I want to [action] so that [benefit]
(write at least 3 user stories)

## Acceptance Criteria
- [ ] Criteria 1
- [ ] Criteria 2
(write at least 5 acceptance criteria)

## Technical Notes
[Key technical considerations, libraries to use, API integrations needed]

## Edge Cases
- Edge case 1
- Edge case 2
(write at least 4 edge cases)

## Estimated Complexity
[Low / Medium / High] - [reason why]

Be specific, detailed and professional.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system", 
                "content": "You are an expert product manager who writes clear, detailed feature specifications."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        max_tokens=2000,
        temperature=0.7
    )
    
    spec = response.choices[0].message.content
    print("✅ Spec Writer Agent completed!")
    return spec