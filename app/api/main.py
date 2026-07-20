from app.database.db import initialize_database
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.profile import router as profile_router
from app.api.routes.attendance import router as attendance_router
from app.api.routes.leave import router as leave_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.login import router as login_router
from app.api.routes.employees import router as employees_router

app = FastAPI(
    title="WorkMate AI API",
    version="1.0.0",
    description="HR Management Backend API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:4200",
    "http://localhost:61244"
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Welcome to WorkMate AI API 🚀"}


@app.get("/health")
def health():
    return {
        "status": "OK",
        "service": "WorkMate AI",
    }


app.include_router(profile_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(dashboard_router)
app.include_router(login_router)
app.include_router(employees_router)