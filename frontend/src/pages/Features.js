import React from "react";

function Features() {
  return (
    <main className="container">
      <div style={{ marginBottom: "60px", textAlign: "center" }}>
        <h1 style={{ fontSize: "36px", fontWeight: "800", marginBottom: "15px", color: "#1f2937" }}>
          Powerful Features
        </h1>
        <p style={{ fontSize: "18px", color: "#6b7280" }}>
          Everything you need for intelligent skill development planning
        </p>
      </div>

      <div className="grid">
        <div className="card">
          <div className="card-icon">📄</div>
          <h3>Intelligent Skill Parsing</h3>
          <p>
            Advanced natural language processing analyzes your resume and job description with precision. We identify specific technical skills, soft skills, experience levels, and domain knowledge automatically.
          </p>
          <ul style={{ marginTop: "15px", paddingLeft: "20px", color: "#6b7280", fontSize: "14px", lineHeight: "1.8" }}>
            <li>Extracts skills with context awareness</li>
            <li>Recognizes skill variations and synonyms</li>
            <li>Identifies proficiency levels automatically</li>
            <li>Captures certifications and specializations</li>
          </ul>
        </div>

        <div className="card">
          <div className="card-icon">🛣️</div>
          <h3>Adaptive Learning Paths</h3>
          <p>
            Generates personalized learning sequences that adapt to your specific skill gaps and learning goals. Each step is carefully ordered based on skill dependencies and priority.
          </p>
          <ul style={{ marginTop: "15px", paddingLeft: "20px", color: "#6b7280", fontSize: "14px", lineHeight: "1.8" }}>
            <li>Respects prerequisite relationships</li>
            <li>Prioritizes high-impact skills first</li>
            <li>Adapts to your learning pace</li>
            <li>Suggests learning resources by skill</li>
          </ul>
        </div>

        <div className="card">
          <div className="card-icon">🧭</div>
          <h3>Reasoning Trace</h3>
          <p>
            Every recommendation includes a reasoning explanation. Understand why each skill is important, how it connects to other skills, and what makes it a priority in your learning journey.
          </p>
          <ul style={{ marginTop: "15px", paddingLeft: "20px", color: "#6b7280", fontSize: "14px", lineHeight: "1.8" }}>
            <li>Clear explanation for each skill</li>
            <li>Shows dependency relationships</li>
            <li>Explains priority and impact</li>
            <li>Links skills to job requirements</li>
          </ul>
        </div>

        <div className="card">
          <div className="card-icon">📊</div>
          <h3>Readiness Scoring</h3>
          <p>
            Get a comprehensive readiness percentage that shows how well-aligned your current skills are with the target role. Understand your strengths and gaps at a glance.
          </p>
          <ul style={{ marginTop: "15px", paddingLeft: "20px", color: "#6b7280", fontSize: "14px", lineHeight: "1.8" }}>
            <li>Overall readiness percentage</li>
            <li>Weighted by skill importance</li>
            <li>Includes proficiency levels</li>
            <li>Visual progress tracking</li>
          </ul>
        </div>

        <div className="card">
          <div className="card-icon">🎯</div>
          <h3>Skill Gap Analysis</h3>
          <p>
            Clear categorization of your skills into what you have and what you need. Visual badges make it easy to understand your current position and target gaps.
          </p>
          <ul style={{ marginTop: "15px", paddingLeft: "20px", color: "#6b7280", fontSize: "14px", lineHeight: "1.8" }}>
            <li>Matched skills highlighting</li>
            <li>Missing skills identification</li>
            <li>Gap severity indicators</li>
            <li>Skill importance weighting</li>
          </ul>
        </div>

        <div className="card">
          <div className="card-icon">⚡</div>
          <h3>Real-Time Analysis</h3>
          <p>
            Get instant results without waiting. Our optimized AI engine processes your documents in seconds and delivers actionable insights immediately.
          </p>
          <ul style={{ marginTop: "15px", paddingLeft: "20px", color: "#6b7280", fontSize: "14px", lineHeight: "1.8" }}>
            <li>Fast file processing</li>
            <li>Instant roadmap generation</li>
            <li>No queues or delays</li>
            <li>Scalable infrastructure</li>
          </ul>
        </div>
      </div>

      <div className="section" style={{ marginTop: "60px", textAlign: "center" }}>
        <h2>How Features Work Together</h2>
        <p style={{ fontSize: "16px", color: "#6b7280", marginBottom: "40px", maxWidth: "700px", margin: "0 auto 40px" }}>
          PathWeaver combines all these features into one seamless experience that gives you clarity on your learning journey.
        </p>

        <div style={{ background: "linear-gradient(135deg, #f0f4ff 0%, #e8ebf8 100%)", padding: "40px", borderRadius: "15px", textAlign: "left" }}>
          <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
            <div style={{ flex: "0 0 40px" }}>
              <div style={{ fontSize: "24px" }}>1️⃣</div>
            </div>
            <div>
              <h4 style={{ fontWeight: "600", marginBottom: "5px" }}>Upload & Parse</h4>
              <p style={{ color: "#6b7280", fontSize: "14px" }}>Intelligent Skill Parsing extracts all relevant skills from your resume and target job</p>
            </div>
          </div>

          <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
            <div style={{ flex: "0 0 40px" }}>
              <div style={{ fontSize: "24px" }}>2️⃣</div>
            </div>
            <div>
              <h4 style={{ fontWeight: "600", marginBottom: "5px" }}>Analyze & Score</h4>
              <p style={{ color: "#6b7280", fontSize: "14px" }}>Skill Gap Analysis identifies what you have and need, while Readiness Scoring calculates your current alignment</p>
            </div>
          </div>

          <div style={{ display: "flex", gap: "20px" }}>
            <div style={{ flex: "0 0 40px" }}>
              <div style={{ fontSize: "24px" }}>3️⃣</div>
            </div>
            <div>
              <h4 style={{ fontWeight: "600", marginBottom: "5px" }}>Plan & Understand</h4>
              <p style={{ color: "#6b7280", fontSize: "14px" }}>Adaptive Learning Paths and Reasoning Trace give you a clear, understandable roadmap with explanations</p>
            </div>
          </div>
        </div>
      </div>

      <div style={{ textAlign: "center", marginTop: "60px", paddingBottom: "40px" }}>
        <h2 style={{ marginBottom: "20px" }}>Try All Features Now</h2>
        <p style={{ color: "#6b7280", marginBottom: "30px" }}>
          Experience the power of intelligent skill analysis in minutes
        </p>
      </div>
    </main>
  );
}

export default Features;
