from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.routes import (
    dashboard,
    employees,
    attendance,
    leaves,
    analytics,
    profile,
    auth,
    ai
)

from app.routes.attendance import seed_attendance


# ==========================
# CREATE DATABASE TABLES
# ==========================

Base.metadata.create_all(bind=engine)


# ==========================
# FASTAPI APP
# ==========================

app = FastAPI(
    title="WorkMate AI API",
    description="Enterprise HR Intelligence Backend",
    version="1.0.0"
)


# ==========================
# CORS
# ==========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================
# ROUTERS
# ==========================

app.include_router(dashboard.router)
app.include_router(employees.router)
app.include_router(attendance.router)
app.include_router(leaves.router)
app.include_router(analytics.router)
app.include_router(profile.router)
app.include_router(auth.router)
app.include_router(ai.router)


# ==========================
# SEED DATABASE
# ==========================

seed_attendance()


# ==========================
# ROOT
# ==========================

@app.get("/")
def root():

    return {

        "message": "WorkMate AI Backend is running 🚀"

    }