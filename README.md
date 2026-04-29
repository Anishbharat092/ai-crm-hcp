# AI-Powered CRM for Healthcare Professionals (HCP)

## Project Overview

This is a full-stack AI-driven CRM designed for the pharmaceutical industry. It uses a **Gemma-2-9b** model (via Groq) to parse unstructured notes from meetings with doctors into structured data, ensuring compliance with **Quality Management Systems (QMS)**.

## 🛠️ Tech Stack

- **Frontend:** React, Redux (State Management)
- **Backend:** FastAPI (Python), LangGraph (Agent Orchestration)
- **AI Model:** Gemma-2-9b via Groq API
- **Version Control:** Git & GitHub (Security-focused with .gitignore)

## Key Features

- **Intelligent Logging:** Parses "Natural Language" notes into structured fields like HCP Name, Sentiment, and Follow-ups.
- **Redux Integration:** Real-time UI updates across split-screen views.
- **QMS Compliance:** Built to facilitate Pharmacovigilance and Audit-readiness in Life Sciences.

## Setup Instructions

1. **Backend:**
   - `cd backend`
   - `pip install -r requirements.txt`
   - `uvicorn main:app --reload`
2. **Frontend:**
   - `cd frontend`
   - `npm install`
   - `npm start`

## Author

- **Anish Bharat** - Aspiring SDE & Cybersecurity Student
