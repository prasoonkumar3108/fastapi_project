from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from routes.period_routes import router

import models
import schemas
import uuid

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "FastAPI SQLite Working"}


@app.post("/period")
def create_period(data: schemas.PeriodRequest):

    db: Session = SessionLocal()

    new_period = models.Period(
        user_id=str(uuid.uuid4()),
        last_period_start_date=data.last_period_start_date,
        period_end_date=data.period_end_date,
        selected_dates=str(data.selected_dates),
        has_no_idea=data.has_no_idea,
        cycle_length_days=data.cycle_length_days,
        period_length_days=data.period_length_days,
        pre_period_days=data.pre_period_days,
        post_period_days=data.post_period_days,
        ovulation_start_day=data.ovulation_start_day,
        ovulation_window_days=data.ovulation_window_days,
        notes=data.notes
    )

    db.add(new_period)
    db.commit()
    db.refresh(new_period)

    return {
        "message": "Data saved successfully",
        "data": {
            "id": new_period.id,
            "user_id": new_period.user_id,
            "notes": new_period.notes
        }
    }