# src/exceptions.py
from fastapi import HTTPException, status

class WineNotFoundException(HTTPException):
    def __init__(self, wine_name: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=f"Wine '{wine_name}' not found")

class InvalidWineDataException(HTTPException):
    def __init__(self, message: str = "Invalid wine data provided"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)
