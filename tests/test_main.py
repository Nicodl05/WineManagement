import sys
import os
from fastapi.testclient import TestClient
from src.main import app
from src.crud import load_inventory_from_json, inventory

sys.path.insert(0, os.path.abspath("src"))

client = TestClient(app)

def setup_module(module):
    inventory.clear()
    load_inventory_from_json()

def test_list_inventory():
    response = client.get("/wines/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 3
    wine_names = {wine["name"] for wine in data}
    assert "Macon Milly Lamartine" in wine_names
    assert "Saint-Veran" in wine_names
    assert "Pouilly-Fuisse" in wine_names

def test_create_wine():
    response = client.post("/wines/", json={
        "name": "Chablis",
        "vintage": 2020,
        "region": {
            "name": "Bourgogne",
            "sub_regions": ["Chablisien"]
        },
        "sub_region": "Chablisien",
        "quantity": 25,
        "purchase_price": 15.0,
        "current_value": 25.0,
        "producer": {
            "name": "Jean Dupont",
            "contact": "jean.dupont@example.com",
            "region": "Bourgogne"
        }
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Chablis"
    assert data["vintage"] == 2020
    assert data["region"]["name"] == "Bourgogne"
    assert data["sub_region"] == "Chablisien"
    assert data["quantity"] == 25
    assert data["purchase_price"] == 15.0
    assert data["current_value"] == 25.0
    assert data["producer"]["name"] == "Jean Dupont"

def test_get_wine():
    response = client.get("/wines/Macon Milly Lamartine")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Macon Milly Lamartine"
    assert data["vintage"] == 2018
    assert data["region"]["name"] == "Bourgogne"
    assert data["sub_region"] == "Macon"
    assert data["purchase_price"] == 15.5
    assert data["current_value"] == 25.0
    assert data["producer"]["name"] == "Auvigue"

def test_update_wine_quantity():
    response = client.put("/wines/Saint-Veran", json={"quantity": 25})
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 25


def test_update_wine_value():
    response = client.put("/wines/Saint-Veran", json={"current_value": 22.0})
    assert response.status_code == 200
    data = response.json()
    assert data["current_value"] == 22.0


def test_delete_wine():
    response = client.delete("/wines/Pouilly-Fuisse")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "Wine deleted"

    response = client.get("/wines/Pouilly-Fuisse")
    assert response.status_code == 404
