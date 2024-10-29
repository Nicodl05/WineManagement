# src/main.py
from fastapi import FastAPI, HTTPException
from src.schemas import WineCreate, WineUpdate
from src.crud import add_wine, get_wine, update_wine_quantity, update_wine_value, delete_wine, list_inventory, load_inventory_from_json
from src.exceptions import InvalidWineDataException, WineNotFoundException

app = FastAPI()
load_inventory_from_json()

@app.get("/wines/")
def get_inventory():
    return list_inventory()

@app.post("/wines/")
def create_wine(wine: WineCreate):
    if wine.quantity < 0: 
        raise InvalidWineDataException("Quantity cannot be negative")
    return add_wine(wine)

@app.get("/wines/{wine_name}")
def read_wine(wine_name: str):
    return get_wine(wine_name) 


@app.put("/wines/{wine_name}")
def update_wine(wine_name: str, wine_update: WineUpdate):
    if wine_update.quantity is not None:
        updated_wine = update_wine_quantity(wine_name, wine_update.quantity)
    elif wine_update.current_value is not None:
        updated_wine = update_wine_value(wine_name, wine_update.current_value)
    else:
        raise InvalidWineDataException("No valid fields to update.")
    
    if not updated_wine:
        raise WineNotFoundException(wine_name)
    return updated_wine

@app.delete("/wines/{wine_name}")
def delete_wine_entry(wine_name: str):
    return delete_wine(wine_name)

