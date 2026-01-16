from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    # set default values
    name : str = 'Aadrish'
    
    # set optional values, meaning -> if value given then take it, else None
    age : Optional[int] = None
    
    # built-in email validation
    email : EmailStr
    
    # add constraints,default values and descriptions using Field function
    cgpa : float = Field(default=1.0,gt=0,lt=10,description="A decimal value representing your overall academic performance.")
    
new_student = {'email' : 'aadrishsen@gmail.com'}

student = Student(**new_student)

# convert to dict
student_dict = student.model_dump()
print(type(student_dict))

# convert to json
student_json = student.model_dump_json()
print(type(student_json))