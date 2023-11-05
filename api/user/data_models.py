from typing import List, Optional

from pydantic import BaseModel, Field


class DactylBaseDataModel(BaseModel):
    def to_strawberry(self, strawberry_type):
        # Get the names of the fields defined in the Strawberry type
        strawberry_fields = {
            field.name for field in strawberry_type.__strawberry_definition__.fields
        }

        # Collect field values from the Pydantic model instance,
        # but only for fields present in the Strawberry type
        field_values = {
            name: value
            for name, value in self.model_dump().items()
            if name in strawberry_fields
        }

        return strawberry_type(**field_values)

    class Config:
        from_attributes = True


class UserDataModel(DactylBaseDataModel):
    email: str = Field(..., example="username")
    password: str = Field(..., example="password")


class LoginUserDataModel(DactylBaseDataModel):
    email: str = Field(..., example="username")
    password: str = Field(..., example="password")


class UserPayloadDataModel(DactylBaseDataModel):
    user: Optional[UserDataModel] = None
    errors: List[str] = []
