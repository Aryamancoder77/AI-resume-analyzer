from fastapi import FastAPI
from pydantic import BaseModel
import fitz  # PyMuPDF
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

class RequestData(BaseModel):
    file_path: str

# Predefined skills database
SKILLS_DB = ["python", "java", "machine learning", "data analysis", "react", "node"]

JOB_DESC = "Looking for a Python developer with ML and React experience"

def extract_text(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.lower()

def extract_skills(text):
    found = []
    for skill in SKILLS_DB:
        if skill in text:
            found.append(skill)
    return found

def compute_score(resume_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, JOB_DESC])
    similarity = cosine_similarity(vectors[0], vectors[1])
    return round(similarity[0][0] * 100, 2)

def generate_suggestions(skills):
    suggestions = []
    if "python" not in skills:
        suggestions.append("Add Python skills")
    if "machine learning" not in skills:
        suggestions.append("Include ML experience")
    if len(skills) < 3:
        suggestions.append("Add more technical skills")
    return suggestions

@app.post("/analyze")
def analyze(data: RequestData):
    text = extract_text(data.file_path)
    skills = extract_skills(text)
    score = compute_score(text)
    suggestions = generate_suggestions(skills)

    return {
        "score": score,
        "skills": skills,
        "suggestions": suggestions
    }
