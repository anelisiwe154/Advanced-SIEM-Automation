from fastapi import APIRouter, HTTPException
from services.user_service import UserService, UserNotFoundException
from code_implem.repositories.inmemory.inmemory_user_repository import InMemoryUserRepository
from code_implem.src.user import User
from api.schemas import UserSchema

router = APIRouter(prefix="/api/users", tags=["Users"])
user_service = UserService(InMemoryUserRepository())

@router.get("/", response_model=list[UserSchema])
def get_all_users():
    return user_service.user_repo.find_all()

@router.post("/", response_model=UserSchema)
def register_user(user: UserSchema):
    try:
        return user_service.register_user(User(**user.dict()))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{user_id}/deactivate", response_model=UserSchema)
def deactivate_user(user_id: str):
    try:
        return user_service.deactivate_user(user_id)
    except UserNotFoundException:
        raise HTTPException(status_code=404, detail="User not found")
