from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

import Request
from main import Base


class Room(Base):
    __tablename__ = "rooms"
    building_type = Column("building_type", String(40), ForeignKey("building_types.type"),
                           nullable=False, primary_key=True)
    number = Column("number", Integer, nullable=False, primary_key=True)

    employee_list: [Request] = relationship("Request")

    type = relationship("BuildingType", back_populates="rooms")

    def __init__(self, building_type: str, number: int):
        self.building_type = building_type
        self.number = number
