# ⚡ SpecDeploy

> **Natural Language → Production Pipeline**
> Type a feature in plain English. Get a full GitHub PR in seconds.

## 🎯 What is SpecDeploy?

SpecDeploy is an AI-powered agentic DevOps tool that transforms a plain English feature request into a complete, production-ready GitHub Pull Request — automatically.

No manual spec writing. No boilerplate code. No pipeline setup.
Just describe what you want. SpecDeploy does the rest.

---

## 🚀 Demo

**Input:**
```
Add Google OAuth login with session management
```

**Output (in ~60 seconds):**
- ✅ Full feature specification (SPEC.md)
- ✅ Implementation code files
- ✅ Unit + integration tests
- ✅ CI/CD pipeline (.github/workflows/ci.yml)
- ✅ Real GitHub Pull Request — automatically opened

---

## 🤖 How It Works

SpecDeploy uses a **multi-agent pipeline** powered by Groq (Llama 3.3 70B):
```
User Input (plain English)
         │
         ▼
┌─────────────────────┐
│   Orchestrator      │
└──────┬──────────────┘
       │
       ├──► Agent 1: Spec Writer
       │         Writes full PRD + user stories + acceptance criteria
       │
       ├──► Agent 2: Code Scaffolder  
       │         Generates implementation code files
       │
       ├──► Agent 3: Test Writer
       │         Writes unit + integration tests
       │
       ├──► Agent 4: Pipeline Builder
       │         Creates GitHub Actions CI/CD config
       │
       └──► GitHub PR Agent
                 Opens a real Pull Request with all files
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React + Vite |
| Backend | Python + FastAPI |
| AI Brain | Groq API (Llama 3.3 70B) |
| Repo Automation | PyGitHub |
| CI/CD | GitHub Actions |
| Agent Orchestration | Custom Python Pipeline |

---

## 📦 Project Structure
```
specdeploy/
├── frontend/                 # React UI
│   └── src/
│       ├── App.jsx           # Main interface
│       └── App.css           # Styles
│
├── backend/                  # Python agents
│   ├── agents/
│   │   ├── spec_writer.py    # Agent 1
│   │   ├── code_scaffolder.py # Agent 2
│   │   ├── test_writer.py    # Agent 3
│   │   └── pipeline_builder.py # Agent 4
│   ├── orchestrator.py       # Coordinates agents
│   ├── github_agent.py       # Opens PRs
│   └── main.py               # FastAPI server
│
└── .github/
    └── workflows/
        └── ci.yml            # CI/CD pipeline
```

---

## ⚙️ Setup & Run

### Prerequisites
- Python 3.11+
- Node.js 18+
- GitHub Account
- Groq API Key (free at console.groq.com)

### 1. Clone the repo
```bash
git clone https://github.com/yup29-pro/SpecDepoly.git
cd SpecDepoly
```

### 2. Setup backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn pygithub python-dotenv requests groq
```

### 3. Configure environment
Create `.env` file in root:
```
GITHUB_TOKEN=your_github_token
GITHUB_REPO_OWNER=your_username
GITHUB_REPO_NAME=your_repo
GROQ_API_KEY=your_groq_key
```

### 4. Run backend
```bash
cd backend
uvicorn main:app --reload
```

### 5. Run frontend
```bash
cd frontend
npm install
npm run dev
```

### 6. Open browser
```
http://localhost:5173
```

---

## 🏆 Hackathon Challenge

Built for **"Automate and Optimize Software Delivery — Leverage Agentic DevOps Principles"**

SpecDeploy demonstrates:
- **Agentic CI/CD** — AI agents that autonomously create production pipelines
- **Intelligent code generation** — From spec to implementation automatically  
- **Self-organizing workflows** — Multi-agent orchestration without human intervention
- **Real DevOps automation** — Actual GitHub PRs, not just mock outputs

---

## 👨‍💻 Built By

**yup29-pro** — Built with Groq, FastAPI, React, and GitHub Actions

---

*From idea to PR in under 60 seconds. That's SpecDeploy.*