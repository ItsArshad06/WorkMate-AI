from app.api.routes.login import router as login_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.leave import router as leave_router
from app.api.routes.attendance import router as attendance_router
from fastapi import FastAPI

from app.api.routes.profile import router as profile_router

app = FastAPI(
    title="WorkMate AI API",
    version="1.0.0",
    description="HR Management Backend API",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to WorkMate AI API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "OK",
        "service": "WorkMate AI"
    }


app.include_router(profile_router)
app.include_router(attendance_router)
app.include_router(leave_router)
app.include_router(dashboard_router)
app.include_router(login_router)