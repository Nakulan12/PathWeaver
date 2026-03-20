SKILL_GRAPH = {
    "machine learning": ["python", "statistics"],
    "data analysis": ["python", "excel"],
    "react": ["javascript"],
    "node": ["javascript"],
    "cloud": ["networking"]
}


def skill_gap(resume_skills, jd_skills):
    missing = list(set(jd_skills) - set(resume_skills))
    matched = list(set(jd_skills).intersection(set(resume_skills)))

    return matched, missing


def calculate_readiness(matched, jd_skills):
    if len(jd_skills) == 0:
        return 0
    score = (len(matched) / len(jd_skills)) * 100
    return round(score, 2)


def generate_reasoned_path(missing_skills, resume_skills):
    path = []
    added = set()

    # Step 1: Add prerequisites (foundation first)
    for skill in missing_skills:
        if skill in SKILL_GRAPH:
            for prereq in SKILL_GRAPH[skill]:
                if prereq not in resume_skills and prereq not in added:
                    path.append({
                        "skill": prereq,
                        "reason": f"{skill} requires understanding of {prereq} for effective implementation",
                        "is_prerequisite": True
                    })
                    added.add(prereq)

    # Step 2: Add missing skills (main goals)
    for skill in missing_skills:
        if skill not in added:
            path.append({
                "skill": skill,
                "reason": f"Required for target role and not found in current skill set. This is a core competency needed for the position.",
                "is_prerequisite": False
            })
            added.add(skill)

    return path
