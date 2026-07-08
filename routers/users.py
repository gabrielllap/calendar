from fastapi import APIRouter
from schemas.user import User

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    return {
        "message": "User created succsesfully!",
        "user": user
    }