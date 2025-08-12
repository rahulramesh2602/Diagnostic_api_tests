#Import FastAPI class
from fastapi import FastAPI

#Create an instance of the FastAPI class
app = FastAPI()

#Root Endpoint
@app.get("/")
def read_root():
    return {"Message": "Tesla Diagnostic API running"}

#Vehicle status endpoint
@app.get("/vehicle/{vehicle_id}/status")
def get_vehicle_status(vehicle_id: int):
    return {
        "vehicle_id" : vehicle_id,
        "status" : "OK",
        "firmware_version" : "2025.1.0"
    }