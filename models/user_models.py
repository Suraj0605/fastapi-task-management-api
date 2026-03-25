from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    email: EmailStr= Field(
        ...,
        description= "Email of the user",
        examples= ["abc@gmail.com"]
    )
    password: str= Field(
        ...,
        min_length= 8,
        description= "Password of the user",
        examples= ["abc@123"]
    )