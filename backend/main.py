from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from parser import extract_text
from skills import extract_skills
from logic import skill_gap, generate_reasoned_path, calculate_readiness

app = FastAPI()

# ✅ CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (safe for hackathon)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "PathForge AI Running"}


@app.post("/roadmap/")
async def roadmap(resume: UploadFile = File(...), jd: UploadFile = File(...)):
    resume_text = await extract_text(resume)
    jd_text = await extract_text(jd)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched, missing = skill_gap(resume_skills, jd_skills)

    path = generate_reasoned_path(missing, resume_skills)

    readiness = calculate_readiness(matched, jd_skills)

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched": matched,
        "missing": missing,
        "readiness_score": readiness,
        "learning_path": path
    }
