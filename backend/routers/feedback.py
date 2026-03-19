from fastapi import APIRouter, HTTPException
from models import FeedbackModel
from database import supabase

router = APIRouter(prefix="/feedback", tags=["Feedback"])

@router.post("/submit")
async def submit_feedback(data: FeedbackModel):
    try:
        res = supabase.table("feedback").insert({
            "rating": data.rating,
            "feedback_type": data.feedback_type,
            "message": data.message,
            "name": data.name
        }).execute()
        return {"message": "Feedback submitted! Thank you."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all")
async def get_feedback():
    try:
        res = supabase.table("feedback").select("*").execute()
        return {"feedback": res.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))