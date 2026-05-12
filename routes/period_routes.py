from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal
import models

router = APIRouter()


@router.get("/periods")
def get_periods():

    db: Session = SessionLocal()

    periods = db.query(models.Period).all()

    return periods