from sqlalchemy import Column, String, Integer, Boolean
from database import Base
import uuid


class Period(Base):
    __tablename__ = "periods"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String)
    last_period_start_date = Column(String)
    period_end_date = Column(String)
    selected_dates = Column(String)
    has_no_idea = Column(Boolean)
    cycle_length_days = Column(Integer)
    period_length_days = Column(Integer)
    pre_period_days = Column(Integer)
    post_period_days = Column(Integer)
    ovulation_start_day = Column(Integer)
    ovulation_window_days = Column(Integer)
    notes = Column(String)