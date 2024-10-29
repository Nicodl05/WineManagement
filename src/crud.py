# src/crud.py
import json
from fastapi import HTTPException
from src.exceptions import WineNotFoundException
from src.models import Producer, Wine, WineRegion

inventory = []  

def load_inventory_from_json(file_path="src/initial_inventory.json"):
    global inventory
    inventory.clear()  
    with open(file_path, "r") as file:
        data = json.load(file)
        for item in data:
            region_data = item["region"]
            region = WineRegion(name=region_data["name"], sub_regions=region_data["sub_regions"])

            producer_data = item["producer"]
            producer = Producer(
                name=producer_data["name"],
                contact=producer_data.get("contact"),
                region=producer_data.get("region")
            )
            wine = Wine(
                name=item["name"],
                vintage=item["vintage"],
                region=region,
                sub_region=item["sub_region"],
                quantity=item["quantity"],
                purchase_price=item["purchase_price"],
                current_value=item["current_value"],
                producer=producer
            )
            inventory.append(wine)

def add_wine(wine_data):
    wine = Wine(**wine_data.model_dump())
    inventory.append(wine)
    return wine

def get_wine(wine_name: str):
    wine = next((wine for wine in inventory if wine.name == wine_name), None)
    if not wine:
        raise WineNotFoundException(wine_name)
    return wine

def update_wine_quantity(wine_name, quantity):
    wine = get_wine(wine_name)
    if wine:
        wine.quantity = quantity
        return wine
    return None

def update_wine_value(wine_name, new_value):
    wine = get_wine(wine_name)
    if wine:
        wine.current_value = new_value
        return wine
    return None



def delete_wine(wine_name: str):
    global inventory
    original_length = len(inventory)
    inventory = [wine for wine in inventory if wine.name != wine_name]
   
    if len(inventory) < original_length:
        return {"detail": "Wine deleted"}
    else:
        raise WineNotFoundException(status_code=404, detail="Wine not found")



def list_inventory():
    return inventory
