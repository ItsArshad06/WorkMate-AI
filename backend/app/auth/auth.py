from app.auth.security import (
    hash_password,
    verify_password
)


# ====================================
# DEMO USER
# ====================================

fake_user = {

    "username": "admin",

    "password": hash_password("admin123"),

    "full_name": "System Administrator",

    "role": "Admin"

}


# ====================================
# AUTHENTICATION
# ====================================

def authenticate_user(
    username: str,
    password: str
):

    if username != fake_user["username"]:

        return None

    if not verify_password(
        password,
        fake_user["password"]
    ):

        return None

    return fake_user