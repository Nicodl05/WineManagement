# src/main.py
from fastapi import FastAPI
from src.schemas import WineCreate
from src.crud import add_wine, get_wine, update_wine_quantity, delete_wine,list_inventory, load_inventory_from_json
from src.exceptions import InvalidWineDataException

app = FastAPI()
load_inventory_from_json()

@app.post("/wines/")
def create_wine(wine: WineCreate):
    if wine.quantity < 0: 
        raise InvalidWineDataException("Quantity cannot be negative")
    return add_wine(wine)

@app.get("/wines/{wine_name}")
def read_wine(wine_name: str):
    return get_wine(wine_name) 

@app.put("/wines/{wine_name}")
def update_wine(wine_name: str, quantity: int):
    if quantity < 0:
        raise InvalidWineDataException("Quantity cannot be negative")
    return update_wine_quantity(wine_name, quantity)

@app.delete("/wines/{wine_name}")
def delete_wine_entry(wine_name: str):
    return delete_wine(wine_name)

@app.get("/wines/")
def get_inventory():
    return list_inventory()