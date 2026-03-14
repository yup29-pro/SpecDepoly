import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from orchestrator import run_pipeline
from github_agent import create_pr

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class FeatureRequest(BaseModel):
    feature: str

@app.get("/")
def root():
    return {"status": "SpecDeploy is running! 🚀"}

@app.post("/generate")
async def generate(request: FeatureRequest):
    print(f"\n📥 Received: {request.feature}")
    
    # Run all 4 agents
    result = run_pipeline(request.feature)
    
    # Create PR on GitHub
    pr_url = create_pr(result)
    
    return {
        "success": True,
        "feature": request.feature,
        "pr_url": pr_url,
        "files_generated": [f["filename"] for f in result["files"]],
        "spec": result["spec"]
    }