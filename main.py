from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tesla Diagnostic API running"}

@app.get("/vehicle/{vehicle_id}/status")
def get_vehicle_status(vehicle_id: int):
    return {
        "vehicle_id": vehicle_id,
        "status": "OK",
        "firmware_version": "2025.1.0"
    }