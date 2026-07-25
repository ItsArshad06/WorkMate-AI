from fastapi import APIRouter

router = APIRouter()

profile = {
    "employee_id": "EMP001",
    "full_name": "John Smith",
    "email": "john.smith@workmate.ai",
    "phone": "+91 9876543210",
    "department": "Engineering",
    "role": "Software Engineer",
    "joining_date": "2024-01-15",
    "status": "Active",
    "attendance": "94%",
    "leave_balance": 12,
    "performance": "Excellent",
    "avatar": "https://i.pravatar.cc/250?img=12"
}


@router.get("/profile")
def get_profile():
    return profile


@router.put("/profile")
def update_profile(updated_profile: dict):
    profile.update(updated_profile)
    return {
        "message": "Profile updated successfully",
        "profile": profile
    }