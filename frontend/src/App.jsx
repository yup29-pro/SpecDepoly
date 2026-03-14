import './App.css';
import { useState } from "react";
import axios from "axios";

export default function App() {
  const [feature, setFeature] = useState("");
  const [status, setStatus] = useState("idle");
  const [result, setResult] = useState(null);
  const [currentStep, setCurrentStep] = useState(0);

  const steps = [
    { label: "Writing Spec..." },
    { label: "Scaffolding Code..." },
    { label: "Writing Tests..." },
    { label: "Building Pipeline..." },
    { label: "Opening PR..." },
  ];

  const handleGenerate = async () => {
    if (!feature.trim()) return;
    setStatus("loading");
    setCurrentStep(0);
    setResult(null);

    let interval;
    interval = setInterval(() => {
      setCurrentStep((prev) => {
        if (prev >= steps.length - 1) {
          clearInterval(interval);
          return prev;
        }
        return prev + 1;
      });
    }, 3000);

    try {
      const response = await axios.post("http://127.0.0.1:8000/generate", {
        feature: feature,
      });
      clearInterval(interval);
      setCurrentStep(steps.length - 1);
      setResult(response.data);
      setStatus("success");
    } catch (error) {
      clearInterval(interval);
      setStatus("error");
    }
  };

  return (
    <div className="app-container">
      <div className="content">

        <h1 className="title">SpecDeploy</h1>
        <p className="subtitle">Natural Language to Production Pipeline</p>

        <div className="card">
          <label className="label">DESCRIBE YOUR FEATURE</label>
          <textarea
            value={feature}
            onChange={(e) => setFeature(e.target.value)}
            placeholder="e.g. Add Google OAuth login with session management..."
            disabled={status === "loading"}
            className="textarea"
          />
          <button
            onClick={handleGenerate}
            disabled={status === "loading" || !feature.trim()}
            className="button"
          >
            {status === "loading" ? "Generating..." : "Generate and Deploy"}
          </button>
        </div>

        {status === "loading" && (
          <div className="card">
            <p className="progress-title">PIPELINE PROGRESS</p>
            {steps.map((step, i) => (
              <div key={i} className="progress-row">
                <span className={i < currentStep ? "done" : i === currentStep ? "running" : "waiting"}>
                  {step.label}
                </span>
                <span className={i < currentStep ? "done" : i === currentStep ? "running" : "waiting"}>
                  {i < currentStep ? "done" : i === currentStep ? "running" : "waiting"}
                </span>
              </div>
            ))}
          </div>
        )}

        {status === "success" && result && (
          <div className="success-card">
            <h2>Pipeline Complete!</h2>
            <a href={result.pr_url} target="_blank" rel="noreferrer" className="button">
              View Pull Request on GitHub
            </a>
            <p className="progress-title">FILES GENERATED</p>
            {result.files_generated.map((file, i) => (
              <div key={i} className="file">{file}</div>
            ))}
            <button onClick={() => { setStatus("idle"); setFeature(""); setResult(null); }} className="reset">
              Try Another Feature
            </button>
          </div>
        )}

        {status === "error" && (
          <div className="error">
            Something went wrong. Make sure the backend is running!
          </div>
        )}

      </div>
    </div>
  );
}