from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

class Category(BaseModel):
    name: str= Field(
        ...,
        min_length=3,
        max_length=30,
        description="Category name",
        examples=["Study"]
    )
    color: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Category color",
        examples=["blue"]
    )

class Todo(BaseModel):
    title: str= Field(
        ...,
        min_length=3,
        max_length=50,
        description="Title of the Todo",
        examples=["Maths"]
    )
    description: str= Field(
        ...,
        min_length=5,
        max_length=200,
        description="Description of the Todo",
        examples=["Solve integration problem"]
    )
    completed: bool= Field(
        False,
        description="Status of the Todo",
        examples=[False]
    )
    category: Optional[Category] = Field(
        None,
        description="Category of the Todo",
        examples=[{"name": "Study", "color": "blue"}]
    )
    @field_validator("title")
    def title_must_have_not_numbers(cls, value):
        if any(char.isdigit() for char in value):
            raise ValueError("Title must not contain numbers!")
        return value

    @model_validator(mode="after")
    def check_completed_description(self):
        if self.completed == True:
            if "completed" not in self.description.lower():
                raise ValueError("If todo is completed, description must contain word 'completed'!")
        return self   

    

# TODO  field validator (Done)
# TODO model  validator (Done)