from sqlalchemy import String, Column

from main import Base


class DoorName(Base):
    __tablename__ = "door_names"
    location = Column("location", String(40), nullable=False, primary_key=True)

    def __init__(self, location: str):
        self.location = location
