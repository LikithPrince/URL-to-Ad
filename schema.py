from pydantic import BaseModel

# Define input model
class AdInput(BaseModel):
    language: str
    writing_for: str
    website_or_landingPageURl: str