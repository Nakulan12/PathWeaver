import React from "react";
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <main>
      <div className="container hero-container">
        <div className="hero">
          <h1>PathWeaver</h1>
          <p className="hero-subtitle">Adaptive AI Onboarding Engine</p>

          <p className="hero-description">
            Transform your onboarding experience with AI-powered skill analysis
            and personalized learning paths
          </p>

          <button
            className="primary-btn"
            onClick={() => navigate("/dashboard")}
          >
            Get Started
          </button>
        </div>
      </div>

      <div className="container">
        <section className="section">
          <h2>Key Features</h2>

          <div className="grid">
            <div className="card">
              <div className="card-icon">📊</div>
              <h3>Skill Gap Analysis</h3>
              <p>
                Identify missing and existing skills using intelligent parsing.
              </p>
            </div>

            <div className="card">
              <div className="card-icon">🎯</div>
              <h3>Adaptive Learning Paths</h3>
              <p>
                Personalized learning roadmap based on your skill gaps.
              </p>
            </div>

            <div className="card">
              <div className="card-icon">🧠</div>
              <h3>AI Reasoning Engine</h3>
              <p>
                Uses NLP + ML embeddings + dependency graph logic.
              </p>
            </div>
          </div>
        </section>

        <section className="section">
          <h2>How It Works</h2>

          <div className="steps">
            <div className="step">
              <div className="step-number">1</div>
              <h4>Upload Resume</h4>
              <p>Upload resume and job description</p>
            </div>

            <div className="step">
              <div className="step-number">2</div>
              <h4>AI Analysis</h4>
              <p>Skill extraction + gap detection</p>
            </div>

            <div className="step">
              <div className="step-number">3</div>
              <h4>Get Roadmap</h4>
              <p>Receive structured learning path</p>
            </div>
          </div>
        </section>
      </div>

      <footer className="footer">
        <p>© PathWeaver AI</p>
      </footer>
    </main>
  );
}

export default Home;