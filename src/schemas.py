from pydantic import BaseModel
from typing import List

class WineRegionCreate(BaseModel):
    name: str
    sub_regions: List[str] = []

class WineCreate(BaseModel):
    name: str
    vintage: int
    region: WineRegionCreate 
    sub_region: str  
    quantity: int
