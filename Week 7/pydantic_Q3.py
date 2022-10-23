from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float