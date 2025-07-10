from pydantic import BaseModel, field_validator, ValidationError


class User(BaseModel):
    name: str
    surname: str
    age: int

    @field_validator("name", "surname")
    @classmethod
    def must_be_alpha(cls, value: str) -> str:
        if not value.isalpha():
            raise ValidationError("Name must be alpha")

        return value.capitalize()

    @field_validator("age")
    @classmethod
    def must_be_positive(cls, value: int) -> int:
        if value <= 0:
            raise ValidationError("Age must be positive")

        return value

    def to_row(self):
        return f"{self.name}|{self.surname}|{self.age}\n"

    def __str__(self):
        return f"Name: {self.name} Surname: {self.surname} ({self.age} y.o.)"
