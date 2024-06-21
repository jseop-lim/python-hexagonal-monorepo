from zoneinfo import ZoneInfo
from sqlalchemy import Column, Integer
from datetime import datetime


metadata = MetaData()

loan_applications = Table(
    "loan_application",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
    ),
    Column(
        "created_at",
        DateTime,
        default=datetime.now(tz=ZoneInfo("UTC")),
    ),
    Column(
        "updated_at",
        DateTime,
        default=datetime.now(tz=ZoneInfo("UTC")),
        onupdate=datetime.now(tz=ZoneInfo("UTC")),
    ),
)
