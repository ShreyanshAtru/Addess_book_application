from pydantic import BaseModel

class AddressSchemas(BaseModel):
    line1: str
    latitude: str
    longitude: str
