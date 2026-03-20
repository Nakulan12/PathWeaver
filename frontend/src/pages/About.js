import React from "react";

function About() {
  return (
    <main className="container">
      <div style={{ marginBottom: "60px" }}>
        <h1 style={{ fontSize: "36px", fontWeight: "800", marginBottom: "15px", color: "#1f2937" }}>
          About PathWeaver
        </h1>
        <p style={{ fontSize: "18px", color: "#667eea", fontWeight: "600" }}>
          Transforming how people onboard and develop skills
        </p>
      </div>

      <div className="grid" style={{ marginBottom: "60px" }}>
        <div className="card">
          <div className="card-icon">🚀</div>
          <h3>The Problem</h3>
          <p>
            Traditional onboarding approaches are one-size-fits-all and static. New team members struggle with unclear priorities, inefficient learning sequences, and wasted time on skills they already possess. This leads to longer ramp-up times and frustrated employees.
          </p>
        </div>

        <div className="card">
          <div className="card-icon">💡</div>
          <h3>Our Solution</h3>
          <p>
            PathWeaver uses advanced AI to analyze your current skills and the requirements of your target role. We create a personalized, adaptive learning roadmap that prioritizes the most impactful skills based on their dependencies and your learning goals.
          </p>
        </div>

        <div className="card">
          <div className="card-icon">🎯</div>
          <h3>Our Approach</h3>
          <p>
            We combine intelligent skill parsing, dependency graph analysis, and machine learning reasoning to understand exactly what you need to learn and in what order. Every recommendation is data-driven and tailored to your unique situation.
          </p>
        </div>
      </div>

      <div className="section">
        <h2>How PathWeaver Works</h2>
        <div className="grid-2">
          <div className="card">
            <h3>Step 1: Analysis</h3>
            <p>
              We parse your resume and the job description using advanced NLP techniques. This gives us a clear picture of what you know, what you're missing, and how each skill connects to others.
            </p>
          </div>

          <div className="card">
            <h3>Step 2: Intelligence</h3>
            <p>
              Our AI engine builds a dependency graph of skills, understanding which foundational skills are prerequisites for others. We calculate the optimal learning sequence.
            </p>
          </div>

          <div className="card">
            <h3>Step 3: Personalization</h3>
            <p>
              Based on your profile and the role requirements, we generate a personalized learning roadmap that prioritizes high-impact skills and respects skill dependencies.
            </p>
          </div>

          <div className="card">
            <h3>Step 4: Scoring</h3>
            <p>
              We calculate your readiness score - a percentage that shows how aligned your current skills are with the target role, based on both presence and importance of each skill.
            </p>
          </div>
        </div>
      </div>

      <div className="section" style={{ background: "linear-gradient(135deg, #f0f4ff 0%, #e8ebf8 100%)", padding: "60px 40px", borderRadius: "20px", marginLeft: "-40px", marginRight: "-40px" }}>
        <h2 style={{ marginBottom: "30px" }}>Why PathWeaver is Different</h2>
        <div className="grid">
          <div style={{ padding: 0, background: "transparent", boxShadow: "none", border: "none" }}>
            <h4 style={{ fontSize: "16px", fontWeight: "600", color: "#667eea", marginBottom: "10px" }}>
              🧠 Intelligent
            </h4>
            <p>
              Uses AI and machine learning to understand skill gaps and dependencies, not just keyword matching.
            </p>
          </div>

          <div style={{ padding: 0, background: "transparent", boxShadow: "none", border: "none" }}>
            <h4 style={{ fontSize: "16px", fontWeight: "600", color: "#667eea", marginBottom: "10px" }}>
              ⚡ Fast
            </h4>
            <p>
              Get your personalized roadmap in seconds, not weeks. Start your learning journey immediately.
            </p>
          </div>

          <div style={{ padding: 0, background: "transparent", boxShadow: "none", border: "none" }}>
            <h4 style={{ fontSize: "16px", fontWeight: "600", color: "#667eea", marginBottom: "10px" }}>
              🎯 Focused
            </h4>
            <p>
              Cut out the noise and focus only on skills that matter for your target role and your growth.
            </p>
          </div>

          <div style={{ padding: 0, background: "transparent", boxShadow: "none", border: "none" }}>
            <h4 style={{ fontSize: "16px", fontWeight: "600", color: "#667eea", marginBottom: "10px" }}>
              📊 Data-Driven
            </h4>
            <p>
              Every recommendation is backed by analysis of your specific profile and the role requirements.
            </p>
          </div>
        </div>
      </div>

      <div style={{ textAlign: "center", marginTop: "60px" }}>
        <h2 style={{ marginBottom: "20px" }}>Ready to optimize your learning path?</h2>
        <p style={{ color: "#6b7280", marginBottom: "30px", fontSize: "16px" }}>
          Upload your resume and start your personalized journey today
        </p>
      </div>
    </main>
  );
}

export default About;
