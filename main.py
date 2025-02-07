from fastapi import FastAPI, HTTPException
from typing import Dict, Optional
from pydantic import BaseModel

app = FastAPI(title="Age Lookup API",
             description="A simple API to look up a person's age by their name")

# Sample data - you can modify these names and ages
PEOPLE_DATA = {
    "john": {"name": "John Smith", "age": 28},
    "emma": {"name": "Emma Watson", "age": 32},
    "michael": {"name": "Michael Brown", "age": 45},
    "sarah": {"name": "Sarah Johnson", "age": 29},
    "david": {"name": "David Wilson", "age": 35}
}

class Person(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Age Lookup API! Use /age/{name} to look up someone's age"}

@app.get("/age/{name}")
def get_age(name: str):
    # Convert name to lowercase for case-insensitive lookup
    name_lower = name.lower()
    
    if name_lower not in PEOPLE_DATA:
        raise HTTPException(status_code=404, detail="Person not found")
    
    return PEOPLE_DATA[name_lower]

@app.get("/all")
def get_all_people():
    return {"people": list(PEOPLE_DATA.values())}

# For development testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)