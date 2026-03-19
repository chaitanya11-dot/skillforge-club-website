from fastapi import APIRouter, HTTPException
from models import EventRegisterModel
from database import supabase

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/all")
async def get_events():
    try:
        res = supabase.table("events").select("*").execute()
        return {"events": res.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/register")
async def register_event(data: EventRegisterModel):
    try:
        res = supabase.table("event_registrations").insert({
            "event_id": data.event_id,
            "name": data.name,
            "email": data.email,
            "department": data.department
        }).execute()
        return {"message": "Registered for event successfully!"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))