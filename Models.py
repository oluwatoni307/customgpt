from pydantic import BaseModel, Field


class semantic_range(BaseModel):
    index: int = Field(description="the range of sematic meaning")
    
    

class content(BaseModel):
    metadata: str = Field(description="the metadata of the content")
    content: str = Field(description="the content of the message")