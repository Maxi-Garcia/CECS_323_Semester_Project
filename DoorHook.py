from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from main import Base


class DoorHook(Base):
    __tablename__ = "door_hook_junction"
    hook_id = Column("hook_id", Integer, nullable=False, primary_key=True)
    door_id = Column("door_id", Integer, nullable=False, primary_key=True)

    door = relationship("Door", back_populates="hook_list")
    hook = relationship("Hook", back_populates="door_list")

    def __init__(self, hook_id: int, door_id: int):
        self.hook_id = hook_id
        self.door_id = door_id
