from pydantic import BaseModel, Field

class StudentSchema(BaseModel):
    rollno : int = Field(...)
    fullname: str = Field(...)
    gender: str = Field(...)
    language : str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "rollno": 1,
                "fullname": "John Doe",
                "gender": "male",
                "language": "English" 
            }
        }
    
class UpdateStudentModel(BaseModel):
    fullname: str = Field(...)
    gender: str = Field(...)
    language : str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "fullname": "kohn Doe",
                "gender": "male",
                "language": "Hindi" 
            }
        }
    