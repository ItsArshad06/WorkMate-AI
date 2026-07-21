from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import dashboard, employees, attendance, leaves, analytics


app = FastAPI(
    title="WorkMate AI API",
    description="Enterprise HR Intelligence Backend",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(dashboard.router)
app.include_router(employees.router)
app.include_router(attendance.router)
app.include_router(leaves.router)
app.include_router(analytics.router)


@app.get("/")
def root():
    return {
        "message": "WorkMate AI Backend is running 🚀"
    }