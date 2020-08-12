from pydantic import BaseModel, Field


class Timezone(BaseModel):
    name: str = Field(None, example="America/Managua")


class TimezoneInput(BaseModel):
    latitude: float
    longitude: float
