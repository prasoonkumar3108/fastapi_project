from fastapi import APIRouter
from database import SessionLocal
import models
import uuid

router = APIRouter()

# -------------------------
# POST API → /tracker
# -------------------------
@router.post("/tracker")
def create_tracker(data: dict):

    db = SessionLocal()

    new_record = models.Period(
        id=str(uuid.uuid4()),
        user_id=data.get("user_id"),
        period_start_date=data.get("period_start_date"),
        period_end_date=data.get("period_end_date"),
        selected_dates=str(data.get("selected_dates")),
        has_no_idea=data.get("has_no_idea"),
        cycle_length_days=data.get("cycle_length_days"),
        period_length_days=data.get("period_length_days"),
        notes=data.get("notes")
    )

    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return {
        "message": "Tracker saved successfully",
        "id": new_record.id
    }


# -------------------------
# GET API → /track
# -------------------------
@router.get("/track")
def get_track(limit: int = 50, offset: int = 0):

    db = SessionLocal()

    query = db.query(models.Period)

    data = query.offset(offset).limit(limit).all()

    result = []

    for item in data:
        result.append({
            "id": item.id,
            "user_id": item.user_id,
            "period_start_date": item.period_start_date,
            "period_end_date": item.period_end_date,
            "selected_dates": eval(item.selected_dates) if item.selected_dates else [],
            "has_no_idea": item.has_no_idea,
            "cycle_length_days": item.cycle_length_days,
            "period_length_days": item.period_length_days,
            "notes": item.notes,
            "created_at": str(item.created_at),
            "updated_at": str(item.updated_at)
        })

    return {
        "data": result,
        "meta": {
            "limit": limit,
            "offset": offset
        }
    }