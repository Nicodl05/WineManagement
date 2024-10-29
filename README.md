# Wine Management API

Wine Management API is a FastAPI-based application designed to help manage a wine inventory. It allows users to track wines by region, sub-region, quantity, pricing, and producer details. The application includes features for adding, updating, retrieving, and deleting wines from inventory.

## Features

- Add a new wine with information such as name, vintage, region, sub-region, quantity, purchase price, current value, and producer.
- Retrieve details about a specific wine or list all wines in inventory.
- Update wine details including quantity and current value.
- Delete wines from the inventory.
- Error Handling for common issues like invalid data input and wine not found.

## Requirements

- Python 3.8+
- FastAPI for creating the API
- Pydantic for data validation
- pytest and coverage for testing

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/username/WineManagement.git
cd WineManagement
```

### 2. Set Up the Virtual Environment

On Windows:

```sh
python -m venv env
.\env\Scripts\activate
```

On macOS/Linux

```sh
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the Application

To start the FastAPI server, use:

```sh
uvicorn src.main:app --reload
```

The application will be available at http://127.0.0.1:8000.


### 5. Initialize Inventory Data

The initial inventory data is loaded from src/initial_inventory.json when the application starts.

### API Documentation

Once the server is running, you can access the interactive API documentation provided by FastAPI at:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Testing

To run unit tests and check coverage:

1. Run the tests with pytest:

```sh
pytest tests/test_main.py
```

2. Check test coverage:

```sh
coverage run -m pytest tests
coverage report -m
```