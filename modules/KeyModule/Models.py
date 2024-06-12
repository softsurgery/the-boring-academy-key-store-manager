from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class ActivationKeyDto(BaseModel):
    expires_at: Optional[datetime]
    is_active: bool = True
    user_id: int
    course_ids: List[int]