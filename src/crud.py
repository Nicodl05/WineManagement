# src/crud.py
import json

from fastapi import HTTPException
from src.exceptions import WineNotFoundException
from src.models import Wine, WineRegion

inventory = []  

def load_inventory_from_json(file_path="src/initial_inventory.json"):
    global inventory
    with open(file_path, "r") as file:
        data = json.load(file)
        for item in data:
            region_data = item["region"]
            region = WineRegion(name=region_data["name"], sub_regions=region_data["sub_regions"])
            wine = Wine(
                name=item["name"],
                vintage=item["vintage"],
                region=region,
                sub_region=item["sub_region"], 
                quantity=item["quantity"]
            )
            inventory.append(wine)

def add_wine(wine_data):
    wine = Wine(**wine_data.model_dump())
    inventory.append(wine)
    return wine

def get_wine(wine_name):
    return next((wine for wine in inventory if wine.name == wine_name), None)

def update_wine_quantity(wine_name, quantity):
    wine = get_wine(wine_name)
    if wine:
        wine.quantity = quantity
        return wine
    return None


def delete_wine(wine_name):
    global inventory
    new_inventory = [wine for wine in inventory if wine.name != wine_name]
    if len(new_inventory) < len(inventory):
        inventory = new_inventory  
        return {"detail": "Wine deleted"}
    else:
        raise WineNotFoundException(status_code=404, detail="Wine not found")

def list_inventory():
    return inventory
