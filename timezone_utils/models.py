from sqlalchemy import Column, UnicodeText, Integer

from .database import Base


class Timezones(Base):
    __tablename__ = "timezones"
    gid = Column(Integer, primary_key=True)
    tzid = Column(UnicodeText)
    geom = Column(UnicodeText)
