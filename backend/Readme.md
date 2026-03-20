# ⚙️ PathWeaver Backend - Execution Logic

This backend handles skill extraction, gap analysis, and adaptive learning path generation.

---

## 🔄 End-to-End Flow

```text
Upload Resume + JD
        ↓
Extract Text (PDF)
        ↓
Extract Skills
        ↓
Compare Skills
        ↓
Generate Learning Path
        ↓
Return JSON Response
```

---

## 🧠 Skill Extraction

The system identifies skills using:

* Keyword matching (reliable detection)
* Embedding similarity (semantic understanding)

👉 Combines both for better accuracy

---

## 📊 Skill Gap Logic

```text
Matched = Resume ∩ JD
Missing = JD - Resume
```

---

## 🧭 Learning Path Logic

Uses a **dependency-based approach**:

Example:

```python
"machine learning": ["python", "statistics"]
```

### Steps:

1. Add prerequisites first
2. Add missing skills
3. Maintain correct order
4. Remove duplicates

---

## 🧠 Reasoning

Each step includes a reason:

* Prerequisite dependency
* Required for role

---

## 📈 Readiness Score

```text
Readiness = (Matched / JD Skills) × 100
```

---

## 📦 API

### POST `/roadmap/`

**Input:**

* Resume (PDF)
* Job Description (PDF)

**Output:**

```json
{
  "matched": [],
  "missing": [],
  "readiness_score": 0,
  "learning_path": []
}
```

---

## 🎯 Key Idea

The backend is designed to be:

* Simple
* Explainable
* Deterministic
* Adaptive

---

## 📌 Summary

PathWeaver converts raw documents into a structured learning roadmap using:

* Skill detection
* Gap analysis
* Dependency-based sequencing
