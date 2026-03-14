import os
from dotenv import load_dotenv
from agents.spec_writer import write_spec
from agents.code_scaffolder import scaffold_code
from agents.test_writer import write_tests
from agents.pipeline_builder import build_pipeline

load_dotenv()

def run_pipeline(feature_request: str) -> dict:
    # sourcery skip: merge-list-append
    print("\n🚀 SpecDeploy Pipeline Starting...")
    print(f"📝 Feature: {feature_request}\n")

    # Agent 1 - Spec Writer
    print("=" * 50)
    print("STEP 1/4: Writing Spec...")
    spec = write_spec(feature_request)

    # Agent 2 - Code Scaffolder
    print("=" * 50)
    print("STEP 2/4: Scaffolding Code...")
    code_files = scaffold_code(spec)

    # Agent 3 - Test Writer
    print("=" * 50)
    print("STEP 3/4: Writing Tests...")
    test_files = write_tests(code_files)

    # Agent 4 - Pipeline Builder
    print("=" * 50)
    print("STEP 4/4: Building CI/CD Pipeline...")
    pipeline = build_pipeline(spec, code_files)

    # Combine everything
    all_files = []
    all_files.append({
        "filename": "SPEC.md",
        "content": spec
    })
    all_files.extend(code_files["files"])
    all_files.extend(test_files["files"])
    all_files.append({
        "filename": ".github/workflows/ci.yml",
        "content": pipeline
    })

    print("\n" + "=" * 50)
    print(f"✅ Pipeline Complete! Generated {len(all_files)} files")
    for f in all_files:
        print(f"  📄 {f['filename']}")

    return {
        "feature": feature_request,
        "spec": spec,
        "files": all_files
    }

if __name__ == "__main__":
    result = run_pipeline("Add Google OAuth login")