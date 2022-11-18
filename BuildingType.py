from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from main import Base


class BuildingType(Base):
    __tablename__ = "building_types"
    type = Column("type", String(40), nullable=False, primary_key=True)

    rooms = relationship("Room")

    def __init__(self, type: str):
        self.type = type
