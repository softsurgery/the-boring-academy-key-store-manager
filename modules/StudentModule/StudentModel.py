from pydantic import BaseModel, EmailStr, Field, StringConstraints, validator
from typing_extensions import Annotated
from .StudentConstants import regions

class CreateStudentDto(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, pattern="^[A-Za-z]+$")] = Field(...)
    surname: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, pattern="^[A-Za-z]+$")] = Field(...)
    email: EmailStr = Field(...)
    phone: Annotated[str, StringConstraints(strip_whitespace=True, min_length=12, max_length=12, pattern=r"^\+216[0-9]{8}$")] = Field(...)
    region: str = Field(...)

    @validator('region')
    def validate_region(cls, v):
        acceptable_regions = regions
        if v not in acceptable_regions:
            raise ValueError(f'Region must be one of {acceptable_regions}')
        return v

    class Config:
        str_strip_whitespace = True
        str_min_length = 1
        use_enum_values = True