from pydantic import BaseModel
from typing import List


class PeriodRequest(BaseModel):
    last_period_start_date: str
    period_end_date: str
    selected_dates: List[str]

    has_no_idea: bool

    cycle_length_days: int
    period_length_days: int

    pre_period_days: int
    post_period_days: int

    ovulation_start_day: int
    ovulation_window_days: int

    notes: str