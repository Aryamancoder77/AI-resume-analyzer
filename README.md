# AI-resume-analyzer
# AI Resume Analyzer

An AI-powered web application that analyzes resumes using NLP and provides:
- Skill extraction
- Resume scoring
- Improvement suggestions

## Tech Stack
- Frontend: React.js
- Backend: Node.js, Express
- AI: Python (FastAPI, NLP)
- ML: TF-IDF, Cosine Similarity

## Features
- Upload resume (PDF)
- Extract skills automatically
- Score resume based on job description
- Suggest improvements

## Installation

1. Clone repo
2. Install dependencies:
   cd client && npm install
   cd server && npm install
   cd ai-service && pip install -r requirements.txt

3. Run services:
   uvicorn main:app --reload
   node index.js
   npm start

## Future Improvements
- BERT-based semantic analysis
- Resume ranking system
- ATS compatibility checker
