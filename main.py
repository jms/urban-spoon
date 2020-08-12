from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session

from timezone_utils import schemas, models, utils
from timezone_utils.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

tags_metadata = [
    {
        "name": "timezone",
        "description": "Find timezone"
    }
]

app = FastAPI(
    title="Timezone Lookup",
    description="Find timezone name using latitude and longitude",
    version="0.0.1",
    openapi_tags=tags_metadata
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/timezone", response_model=schemas.Timezone, tags=["timezone"])
async def get_timezone(
        latitude: float = Query(gt=-85, lt=85, default=0, example=12),
        longitude: float = Query(gt=-180, lt=180, default=0, example=-86),
        db: Session = Depends(get_db)
):
    point = schemas.TimezoneInput(latitude=latitude, longitude=longitude)
    return utils.get_timezone(db, point)
