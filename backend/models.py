from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    name: str
    email: str
    password: str
    department: str
    role: str = "participant"

class LoginModel(BaseModel):
    email: str
    password: str

class ProjectModel(BaseModel):
    title: str
    description: str
    domain: str
    team_size: str
    timeline: str

class EventRegisterModel(BaseModel):
    event_id: str
    name: str
    email: str
    department: str

class FeedbackModel(BaseModel):
    rating: int
    feedback_type: str
    message: str
    name: Optional[str] = "Anonymous"