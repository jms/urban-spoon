import sqlalchemy as sa
from sqlalchemy.orm import Session

from . import models, schemas


def get_timezone(db: Session, point: schemas.TimezoneInput) -> schemas.Timezone:
    name = db.query(models.Timezones.tzid).filter(
        sa.func.ST_Contains(
            models.Timezones.geom, sa.func.ST_MakePoint(
                point.longitude,
                point.latitude)
        )
    ).scalar()
    return schemas.Timezone(name=name)
