from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from main import Base


class DoorName(Base):
    __tablename__ = "door_names"
    location = Column("location", String(40), nullable=False, primary_key=True)

    door = relationship("Door")

    def __init__(self, location: str):
        self.location = location
