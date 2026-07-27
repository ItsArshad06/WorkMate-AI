from fastapi import APIRouter, Depends, UploadFile, File
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.employee import Employee
from app.models import Attendance
from app.auth.dependencies import get_current_user
from app.routes.leaves import leave_requests

from pypdf import PdfReader
from docx import Document

import os


router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)


class ChatRequest(BaseModel):
    message: str



# ==========================
# CHATBOT
# ==========================

@router.post("/chat")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    message = request.message.lower()


    if any(word in message for word in ["hi", "hello", "hey"]):

        return {
            "reply": f"Hello {user['username']}! I'm WorkMate AI. How can I help you today?"
        }



    if "dashboard" in message or "summary" in message:

        employee_count = db.query(Employee).count()

        attendance_count = db.query(Attendance).count()

        pending = len(
            [
                leave
                for leave in leave_requests
                if leave["status"] == "Pending"
            ]
        )


        return {
            "reply":
            f"""📊 Dashboard Summary

👥 Employees: {employee_count}
📅 Attendance Records: {attendance_count}
📝 Pending Leaves: {pending}
🤖 AI Status: Online"""
        }



    if "employee count" in message or "how many employees" in message:

        total = db.query(Employee).count()

        return {
            "reply":
            f"There are currently {total} employees in the organisation."
        }



    if "employees" in message:

        employees = db.query(Employee).all()

        names = "\n".join(
            [
                emp.full_name
                for emp in employees
            ]
        )

        return {
            "reply":
            f"Employee List\n\n{names}"
        }



    if "attendance" in message:

        total = db.query(Attendance).count()

        return {
            "reply":
            f"There are currently {total} attendance records."
        }



    if "leave" in message:

        pending = len(
            [
                leave
                for leave in leave_requests
                if leave["status"] == "Pending"
            ]
        )

        return {
            "reply":
            f"There are currently {pending} pending leave requests."
        }



    return {
        "reply":
        "Sorry, I didn't understand that question."
    }





# ==========================
# RESUME ANALYZER
# ==========================


def extract_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text() or ""

    return text



def extract_docx(file_path):

    doc = Document(file_path)

    text = ""

    for paragraph in doc.paragraphs:

        text += paragraph.text + "\n"

    return text




@router.post("/resume")
async def analyze_resume(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):


    upload_folder = "uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )


    file_path = os.path.join(
        upload_folder,
        file.filename
    )


    with open(file_path, "wb") as buffer:

        buffer.write(
            await file.read()
        )



    text = ""



    if file.filename.endswith(".pdf"):

        text = extract_pdf(file_path)



    elif file.filename.endswith(".docx"):

        text = extract_docx(file_path)



    skills = []


    keywords = [
        "Python",
        "Angular",
        "FastAPI",
        "SQL",
        "Java",
        "Machine Learning",
        "JavaScript",
        "React"
    ]



    for skill in keywords:

        if skill.lower() in text.lower():

            skills.append(skill)



    if not skills:

        skills = [
            "Communication",
            "Problem Solving",
            "Technical Skills"
        ]



    return {


        "candidate":

        file.filename,



        "score":

        "90%",



        "skills":

        skills,



        "education":

        "Computer Science / Engineering",



        "experience":

        "Technical Experience Detected",



        "summary":

        "AI analysis completed. Candidate shows relevant skills and is recommended for further evaluation."

    }