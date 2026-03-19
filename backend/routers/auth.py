from fastapi import APIRouter, HTTPException
from models import SignUpModel, LoginModel
from database import supabase

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup")
async def signup(data: SignUpModel):
    try:
        res = supabase.auth.sign_up({
            "email": data.email,
            "password": data.password,
            "options": {
                "data": {
                    "name": data.name,
                    "department": data.department,
                    "role": data.role
                }
            }
        })
        return {"message": "Signup successful! Check your email.", "user": res.user.email}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(data: LoginModel):
    try:
        res = supabase.auth.sign_in_with_password({
            "email": data.email,
            "password": data.password
        })
        return {
            "message": "Login successful!",
            "access_token": res.session.access_token,
            "user": {
                "email": res.user.email,
                "name": res.user.user_metadata.get("name"),
                "role": res.user.user_metadata.get("role"),
                "department": res.user.user_metadata.get("department")
            }
        }
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid email or password")