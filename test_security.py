from app.database.password import get_password_hash
from app.security.security import verify_password

password_hash = get_password_hash("EMP-101")

print(password_hash)

print(
    verify_password(
        "Welcome123",
        password_hash
    )
)