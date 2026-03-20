import React, { useState } from "react";
import axios from "axios";

function Dashboard() {
  const [resume, setResume] = useState(null);
  const [jd, setJd] = useState(null);
  const [resumeFileName, setResumeFileName] = useState("");
  const [jdFileName, setJdFileName] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [simulationSkill, setSimulationSkill] = useState(null);

  const handleResumeChange = (e) => {
    const file = e.target.files[0];
    setResume(file);
    setResumeFileName(file ? file.name : "");
  };

  const handleJdChange = (e) => {
    const file = e.target.files[0];
    setJd(file);
    setJdFileName(file ? file.name : "");
  };

  const handleSubmit = async () => {
    setError("");
    
    if (!resume || !jd) {
      setError("Please upload both resume and job description files");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("jd", jd);

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/roadmap/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      setResult(res.data);
      setSimulationSkill(null);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
        "Error processing files. Please check the backend connection."
      );
    } finally {
      setLoading(false);
    }
  };

  const getReadinessColor = (score) => {
    if (score >= 80) return "#10b981";
    if (score >= 50) return "#f59e0b";
    return "#ef4444";
  };

  const simulateSkillLearning = (skillToLearn) => {
    if (!result) return;
    setSimulationSkill(skillToLearn);
  };

  const getSimulatedScore = () => {
    if (!simulationSkill || !result) return result.readiness_score;
    const newMatched = result.matched.length + (result.missing.includes(simulationSkill) ? 1 : 0);
    return Math.round((newMatched / result.jd_skills.length) * 100);
  };

  return (
    <main style={{ background: "#f8fafc", minHeight: "100vh", padding: "0" }}>
      <div style={{ maxWidth: "1200px", margin: "0 auto", padding: "60px 40px" }}>
        
        {!result ? (
          <div>
            <div style={{ marginBottom: "60px" }}>
              <h2 style={{ fontSize: "32px", fontWeight: "700", marginBottom: "12px", color: "#1f2937" }}>
                Generate Your Learning Roadmap
              </h2>
              <p style={{ fontSize: "16px", color: "#666", marginBottom: "40px" }}>
                Upload your resume and job description to get a personalized learning plan
              </p>

              <div style={{
                background: "white",
                padding: "50px",
                borderRadius: "12px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
                maxWidth: "550px"
              }}>
                <div style={{ marginBottom: "30px" }}>
                  <label style={{ 
                    display: "block", 
                    fontSize: "14px", 
                    fontWeight: "600", 
                    marginBottom: "12px",
                    color: "#1f2937"
                  }}>
                    Resume / CV
                  </label>
                  <input
                    type="file"
                    onChange={handleResumeChange}
                    accept=".pdf,.doc,.docx,.txt"
                    style={{
                      width: "100%",
                      padding: "14px",
                      border: "2px dashed #d1d5db",
                      borderRadius: "8px",
                      cursor: "pointer",
                      fontSize: "14px",
                      fontFamily: "inherit"
                    }}
                  />
                  {resumeFileName && (
                    <p style={{ fontSize: "12px", color: "#10b981", marginTop: "8px", fontWeight: "500" }}>
                      ✓ {resumeFileName}
                    </p>
                  )}
                </div>

                <div style={{ marginBottom: "30px" }}>
                  <label style={{ 
                    display: "block", 
                    fontSize: "14px", 
                    fontWeight: "600", 
                    marginBottom: "12px",
                    color: "#1f2937"
                  }}>
                    Job Description
                  </label>
                  <input
                    type="file"
                    onChange={handleJdChange}
                    accept=".pdf,.doc,.docx,.txt"
                    style={{
                      width: "100%",
                      padding: "14px",
                      border: "2px dashed #d1d5db",
                      borderRadius: "8px",
                      cursor: "pointer",
                      fontSize: "14px",
                      fontFamily: "inherit"
                    }}
                  />
                  {jdFileName && (
                    <p style={{ fontSize: "12px", color: "#10b981", marginTop: "8px", fontWeight: "500" }}>
                      ✓ {jdFileName}
                    </p>
                  )}
                </div>

                {error && (
                  <div style={{
                    background: "#fee2e2",
                    color: "#991b1b",
                    padding: "14px",
                    borderRadius: "8px",
                    marginBottom: "24px",
                    fontSize: "14px",
                    borderLeft: "4px solid #ef4444"
                  }}>
                    {error}
                  </div>
                )}

                <button
                  onClick={handleSubmit}
                  disabled={loading || !resume || !jd}
                  style={{
                    width: "100%",
                    padding: "14px 24px",
                    fontSize: "15px",
                    fontWeight: "600",
                    background: loading || (!resume || !jd) ? "#d1d5db" : "#667eea",
                    color: "white",
                    border: "none",
                    borderRadius: "8px",
                    cursor: loading || (!resume || !jd) ? "not-allowed" : "pointer",
                    transition: "all 0.2s",
                    opacity: loading || (!resume || !jd) ? 0.6 : 1
                  }}
                  onMouseOver={(e) => {
                    if (!loading && resume && jd) {
                      e.target.style.background = "#5568d3";
                      e.target.style.transform = "translateY(-2px)";
                    }
                  }}
                  onMouseOut={(e) => {
                    e.target.style.background = "#667eea";
                    e.target.style.transform = "translateY(0)";
                  }}
                >
                  {loading ? "Processing..." : "Generate Roadmap"}
                </button>
              </div>
            </div>
          </div>
        ) : (
          <div>
            <h2 style={{ fontSize: "28px", fontWeight: "700", marginBottom: "40px", color: "#1f2937" }}>
              Your Readiness Profile
            </h2>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "24px", marginBottom: "30px" }}>
              {/* Readiness Score Card */}
              <div style={{
                background: "white",
                padding: "40px",
                borderRadius: "12px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
                textAlign: "center"
              }}>
                <div style={{ fontSize: "12px", fontWeight: "700", color: "#999", marginBottom: "20px", textTransform: "uppercase", letterSpacing: "0.5px" }}>
                  Readiness Score
                </div>
                <div style={{
                  fontSize: "72px",
                  fontWeight: "800",
                  color: getReadinessColor(simulationSkill ? getSimulatedScore() : result.readiness_score),
                  marginBottom: "20px",
                  lineHeight: "1"
                }}>
                  {simulationSkill ? getSimulatedScore() : result.readiness_score}%
                </div>
                <div style={{
                  width: "100%",
                  height: "8px",
                  background: "#e5e7eb",
                  borderRadius: "10px",
                  overflow: "hidden",
                  marginBottom: "15px"
                }}>
                  <div style={{
                    height: "100%",
                    width: `${simulationSkill ? getSimulatedScore() : result.readiness_score}%`,
                    background: getReadinessColor(simulationSkill ? getSimulatedScore() : result.readiness_score),
                    transition: "width 0.5s ease",
                    borderRadius: "10px"
                  }}></div>
                </div>
                {simulationSkill && (
                  <p style={{ fontSize: "12px", color: "#10b981", fontWeight: "600", marginBottom: "10px" }}>
                    Projected with {simulationSkill}
                  </p>
                )}
                <p style={{ fontSize: "11px", color: "#666", lineHeight: "1.5" }}>
                  This score represents how closely your current skills match the target role requirements.
                </p>
              </div>

              {/* Optimization Insight Card */}
              <div style={{
                background: "#eff6ff",
                border: "1px solid #bfdbfe",
                padding: "30px",
                borderRadius: "12px",
                boxShadow: "0 2px 8px rgba(59, 130, 246, 0.08)"
              }}>
                <div style={{ fontSize: "12px", fontWeight: "700", color: "#1e40af", marginBottom: "12px", textTransform: "uppercase", letterSpacing: "0.5px" }}>
                  Optimization Insight
                </div>
                <div style={{ fontSize: "14px", fontWeight: "600", color: "#1e40af", marginBottom: "12px" }}>
                  AI-Powered Impact Analysis
                </div>
                <p style={{ fontSize: "13px", color: "#1e40af", lineHeight: "1.6", marginBottom: "15px" }}>
                  Following this AI-generated learning path can improve your readiness by up to <strong>40%</strong> and reduce redundant training by focusing on high-impact skills.
                </p>
                <div style={{ paddingTop: "15px", borderTop: "1px solid #bfdbfe" }}>
                  <p style={{ fontSize: "12px", color: "#1e40af", fontWeight: "500" }}>
                    Key Benefits:
                  </p>
                  <ul style={{ fontSize: "12px", color: "#1e40af", marginLeft: "16px", marginTop: "8px" }}>
                    <li>Dependency-aware learning order</li>
                    <li>Prioritizes high-impact skills first</li>
                    <li>Saves time on non-critical skills</li>
                  </ul>
                </div>
              </div>
            </div>

            {/* Skills Badges */}
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "24px", marginBottom: "30px" }}>
              <div style={{
                background: "white",
                padding: "30px",
                borderRadius: "12px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
                transition: "box-shadow 0.2s"
              }}
              onMouseEnter={(e) => e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.1)"}
              onMouseLeave={(e) => e.currentTarget.style.boxShadow = "0 2px 8px rgba(0,0,0,0.06)"}
              >
                <h3 style={{ fontSize: "15px", fontWeight: "700", marginBottom: "20px", color: "#1f2937" }}>Your Current Skills</h3>
                <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
                  {result.matched && result.matched.length > 0 ? (
                    result.matched.map((skill, i) => (
                      <span key={i} style={{
                        display: "inline-block",
                        background: "#d1fae5",
                        color: "#065f46",
                        padding: "8px 14px",
                        borderRadius: "20px",
                        fontSize: "13px",
                        fontWeight: "500",
                        transition: "all 0.2s",
                        cursor: "default"
                      }}
                      onMouseEnter={(e) => e.target.style.transform = "scale(1.08)"}
                      onMouseLeave={(e) => e.target.style.transform = "scale(1)"}
                      >
                        ✓ {skill}
                      </span>
                    ))
                  ) : (
                    <p style={{ color: "#999", fontSize: "13px" }}>None identified</p>
                  )}
                </div>
              </div>

              <div style={{
                background: "white",
                padding: "30px",
                borderRadius: "12px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
              }}>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "20px" }}>
                  <h3 style={{ fontSize: "15px", fontWeight: "700", color: "#1f2937" }}>Skills to Develop</h3>
                  <span style={{ fontSize: "11px", fontWeight: "600", color: "#10b981", background: "#d1fae5", padding: "4px 10px", borderRadius: "12px" }}>
                    Simulate Skill Improvement
                  </span>
                </div>
                <p style={{ fontSize: "12px", color: "#999", marginBottom: "15px" }}>
                  Click any skill to see your projected readiness score
                </p>
                <div style={{ display: "flex", flexWrap: "wrap", gap: "10px" }}>
                  {result.missing && result.missing.length > 0 ? (
                    result.missing.map((skill, i) => (
                      <button
                        key={i}
                        onClick={() => simulateSkillLearning(skill)}
                        style={{
                          display: "inline-block",
                          background: simulationSkill === skill ? "#fca5a5" : "#fee2e2",
                          color: "#991b1b",
                          padding: "8px 14px",
                          borderRadius: "20px",
                          fontSize: "13px",
                          fontWeight: "500",
                          border: "none",
                          cursor: "pointer",
                          transition: "all 0.2s"
                        }}
                        onMouseOver={(e) => {
                          e.target.style.background = "#fca5a5";
                          e.target.style.transform = "scale(1.05)";
                        }}
                        onMouseOut={(e) => {
                          e.target.style.background = simulationSkill === skill ? "#fca5a5" : "#fee2e2";
                          e.target.style.transform = "scale(1)";
                        }}
                      >
                        {skill}
                      </button>
                    ))
                  ) : (
                    <p style={{ color: "#999", fontSize: "13px" }}>All skills matched!</p>
                  )}
                </div>
              </div>
            </div>

            {/* AI Reasoning Trace Section */}
            <div style={{
              background: "white",
              padding: "30px",
              borderRadius: "12px",
              boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
              marginBottom: "30px",
              borderLeft: "4px solid #667eea"
            }}>
              <h3 style={{ fontSize: "16px", fontWeight: "700", marginBottom: "8px", color: "#1f2937" }}>AI Reasoning Trace</h3>
              <p style={{ color: "#666", fontSize: "13px" }}>
                This path is generated based on skill dependencies and gap analysis
              </p>
            </div>

            {/* Learning Path */}
            <div style={{
              background: "white",
              padding: "30px",
              borderRadius: "12px",
              boxShadow: "0 2px 8px rgba(0,0,0,0.06)",
              marginBottom: "30px"
            }}>
              <h3 style={{ fontSize: "18px", fontWeight: "700", marginBottom: "8px", color: "#1f2937" }}>Recommended Learning Order</h3>
              <p style={{ color: "#999", fontSize: "12px", marginBottom: "25px" }}>
                Based on Skill Dependencies
              </p>

              {result.learning_path && result.learning_path.length > 0 ? (
                <div style={{ display: "grid", gap: "12px" }}>
                  {result.learning_path.map((item, i) => (
                    <div 
                      key={i} 
                      style={{
                        background: item.is_prerequisite ? "#fffbeb" : "#f0f4ff",
                        border: `1px solid ${item.is_prerequisite ? "#fde68a" : "#bfdbfe"}`,
                        borderLeft: `4px solid ${item.is_prerequisite ? "#f59e0b" : "#667eea"}`,
                        padding: "18px",
                        borderRadius: "10px",
                        display: "flex",
                        gap: "14px",
                        transition: "all 0.2s"
                      }}
                      onMouseEnter={(e) => {
                        e.currentTarget.style.boxShadow = "0 4px 12px rgba(0,0,0,0.08)";
                        e.currentTarget.style.transform = "translateX(4px)";
                      }}
                      onMouseLeave={(e) => {
                        e.currentTarget.style.boxShadow = "none";
                        e.currentTarget.style.transform = "translateX(0)";
                      }}
                    >
                      <div style={{
                        width: "38px",
                        height: "38px",
                        background: item.is_prerequisite ? "#fef3c7" : "#dbeafe",
                        border: `2px solid ${item.is_prerequisite ? "#f59e0b" : "#667eea"}`,
                        borderRadius: "50%",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        fontWeight: "700",
                        fontSize: "14px",
                        color: item.is_prerequisite ? "#b45309" : "#1e40af",
                        flexShrink: 0,
                        minWidth: "38px",
                        minHeight: "38px"
                      }}>
                        {i + 1}
                      </div>
                      <div style={{ flex: 1 }}>
                        <h4 style={{ fontSize: "14px", fontWeight: "700", marginBottom: "6px", color: "#1f2937" }}>
                          {item.skill}
                          {item.is_prerequisite && <span style={{ fontSize: "11px", color: "#f59e0b", fontWeight: "600", marginLeft: "8px", background: "#fef3c7", padding: "2px 8px", borderRadius: "4px" }}>Foundation Skill</span>}
                        </h4>
                        <p style={{ fontSize: "13px", color: "#666", lineHeight: "1.5" }}>
                          {item.reason}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <p style={{ color: "#999", fontSize: "13px" }}>No learning path available</p>
              )}
            </div>

            <div style={{ textAlign: "center" }}>
              <button
                onClick={() => {
                  setResult(null);
                  setResume(null);
                  setJd(null);
                  setResumeFileName("");
                  setJdFileName("");
                  setSimulationSkill(null);
                }}
                style={{
                  padding: "12px 32px",
                  fontSize: "14px",
                  fontWeight: "600",
                  background: "#6b7280",
                  color: "white",
                  border: "none",
                  borderRadius: "8px",
                  cursor: "pointer",
                  transition: "all 0.2s"
                }}
                onMouseOver={(e) => {
                  e.target.style.background = "#5a6370";
                  e.target.style.transform = "translateY(-2px)";
                }}
                onMouseOut={(e) => {
                  e.target.style.background = "#6b7280";
                  e.target.style.transform = "translateY(0)";
                }}
              >
                Generate Another Roadmap
              </button>
            </div>
          </div>
        )}
      </div>
    </main>
  );
}

export default Dashboard;
