from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime

class CreateActivationKeyDto(BaseModel):
    expires_at: Optional[datetime]
    is_active: bool = True
    user_id: int
    course_ids: List[int]

class UpdateActivationKeyDto(BaseModel):
    expires_at: Optional[datetime]
    is_active: Optional[bool]
    user_id: Optional[int]
    course_ids: Optional[List[int]]
    is_connected_once_desktop: Optional[bool]
    is_connected_once_mobile: Optional[bool]