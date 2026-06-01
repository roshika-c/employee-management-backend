from pydantic import BaseModel,Field
class Employee(BaseModel):
    id:int
    name:str
    age:int=Field(gt=18)
    gender:str