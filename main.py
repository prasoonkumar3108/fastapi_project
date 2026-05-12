from fastapi import FastAPI
from database import engine, Base

# Import routes
from routes.period_routes import router as period_router
from routes.tracker_routes import router as tracker_router

# Import models (IMPORTANT: ensures tables are created)
import models




app = FastAPI(title="FastAPI Period Tracker API")

# ----------------------------
# DB TABLE CREATE
# ----------------------------
Base.metadata.create_all(bind=engine)


# ----------------------------
# ROUTES INCLUDE
# ----------------------------
app.include_router(period_router)

app.include_router(tracker_router)
# ----------------------------
# HEALTH CHECK API
# ----------------------------
@app.get("/")
def home():
    return {
        "message": "FastAPI is running successfully 🚀"
    }