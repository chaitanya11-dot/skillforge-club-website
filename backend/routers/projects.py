from fastapi import APIRouter, HTTPException
from models import ProjectModel
from database import supabase

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/submit")
async def submit_project(data: ProjectModel):
    try:
        res = supabase.table("projects").insert({
            "title": data.title,
            "description": data.description,
            "domain": data.domain,
            "team_size": data.team_size,
            "timeline": data.timeline,
            "status": "pending"
        }).execute()
        return {"message": "Project submitted successfully!", "data": res.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/all")
async def get_all_projects():
    try:
        res = supabase.table("projects").select("*").execute()
        return {"projects": res.data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{project_id}/status")
async def update_status(project_id: str, status: str):
    try:
        res = supabase.table("projects").update({"status": status}).eq("id", project_id).execute()
        return {"message": f"Project status updated to {status}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))