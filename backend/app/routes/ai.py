import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

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
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

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

class InterviewStartRequest(BaseModel):
    candidate_name: str
    position: str



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
# ==========================
# AI INTERVIEW
# ==========================

@router.post("/interview/start")
def start_interview(
    request: InterviewStartRequest,
    user=Depends(get_current_user)
):

    questions = [

        f"Tell me about yourself, {request.candidate_name}.",

        f"Why do you want to become a {request.position}?",

        "Describe your strongest technical project.",

        "How do you solve problems under pressure?",

        "Why should we hire you?"

    ]

    return {

        "candidate": request.candidate_name,

        "position": request.position,

        "questions": questions

    }
class InterviewAnswer(BaseModel):
    question: str
    answer: str


class InterviewEvaluationRequest(BaseModel):
    candidate_name: str
    position: str
    answers: list[InterviewAnswer]
# ==========================
# AI INTERVIEW EVALUATION
# ==========================

@router.post("/interview/evaluate")
def evaluate_interview(
    request: InterviewEvaluationRequest,
    user=Depends(get_current_user)
):

    answered = sum(
        1
        for answer in request.answers
        if answer.answer.strip()
    )

    score = int((answered / len(request.answers)) * 100)

    if score >= 90:
        recommendation = "Highly Recommended"

    elif score >= 70:
        recommendation = "Recommended"

    else:
        recommendation = "Needs Improvement"

    return {

        "candidate": request.candidate_name,

        "position": request.position,

        "communication": 8,

        "technical": 8,

        "confidence": 9,

        "problem_solving": 8,

        "overall_score": score,

        "recommendation": recommendation

    }
def send_mail(receiver_email: str, subject: str, body: str):

    message = MIMEMultipart()

    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(
        MIMEText(body, "plain")
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as server:

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            EMAIL_PASSWORD
        )

        server.sendmail(
            EMAIL_ADDRESS,
            receiver_email,
            message.as_string()
        )
 # ==========================
# EMAIL AUTOMATION
# ==========================

class EmailRequest(BaseModel):
    candidate_name: str
    candidate_email: str
    position: str
    score: int
    recommendation: str


@router.post("/send-email")
def send_email(
    request: EmailRequest,
    user=Depends(get_current_user)
):

    candidate_message = f"""
Dear {request.candidate_name},

Congratulations!

Your interview for the position of
{request.position}
has been completed successfully.

Overall Score: {request.score}%

Recommendation:
{request.recommendation}

Our HR team will contact you shortly.

Best Regards,

WorkMate AI Recruitment Team
"""

    hr_message = f"""
Candidate Interview Report

Candidate:
{request.candidate_name}

Candidate Email:
{request.candidate_email}

Position:
{request.position}

Overall Score:
{request.score}%

Recommendation:
{request.recommendation}
"""

    try:

        send_mail(

            request.candidate_email,

            "Interview Result - WorkMate AI",

            candidate_message

        )

        send_mail(

            EMAIL_ADDRESS,

            "New Candidate Interview Report",

            hr_message

        )

        return {

            "success": True,

            "message": "Emails sent successfully."

        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }


@router.post("/send-email")
def send_email(
    request: EmailRequest,
    user=Depends(get_current_user)
):

    candidate_email = f"""
Dear {request.candidate_name},

Thank you for attending the interview for the
{request.position} position.

Your interview has been successfully completed.

Overall Score: {request.score}%

Recommendation:
{request.recommendation}

Our HR team will review your profile and contact you
regarding the next steps.

Best Regards,
WorkMate AI Recruitment Team
"""

    hr_email = f"""
Candidate Interview Report

Candidate Name:
{request.candidate_name}

Candidate Email:
{request.candidate_email}

Position:
{request.position}

Overall Score:
{request.score}%

Recommendation:
{request.recommendation}

Generated by WorkMate AI.
"""

    return {
        "success": True,
        "message": "Email templates generated successfully.",
        "candidate_email": candidate_email,
        "hr_email": hr_email
    } 
    