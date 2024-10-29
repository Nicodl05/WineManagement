from pydantic import BaseModel
from typing import List, Optional

class ProducerCreate(BaseModel):
    name: str
    contact: str = None
    region: str = None

class WineRegionCreate(BaseModel):
    name: str
    sub_regions: List[str] = []

class WineCreate(BaseModel):
    name: str
    vintage: int
    region: WineRegionCreate
    sub_region: str
    quantity: int
    purchase_price: float
    current_value: float
    producer: ProducerCreate

class WineUpdate(BaseModel):
    quantity: Optional[int] = None
    current_value: Optional[float] = None