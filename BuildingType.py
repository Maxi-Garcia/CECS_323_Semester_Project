from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

import Room
from main import Base


class BuildingType(Base):
    __tablename__ = "building_types"
    type = Column("type", String(40), nullable=False, primary_key=True)

    rooms: [Room] = relationship("Room", back_populates="type", viewonly=False)

    def __init__(self, type: str):
        self.type = type
