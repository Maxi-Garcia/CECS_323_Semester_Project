from sqlalchemy import Column, Integer, Sequence
from sqlalchemy.orm import relationship

import DoorHook
import Door
from main import Base
from DoorHook import DoorHook


class Hook(Base):
    __tablename__ = "hooks"
    id = Column("id", Integer, Sequence('hook_id_seq'), nullable=False, primary_key=True)

    door_list: [DoorHook] = relationship("DoorHook", back_populates="hook", viewonly=False)

    def __init__(self, id: int):
        self.id = id
        self.door_hook_list = []

    def add_door(self, door: Door):
        for door_hook in self.door_hook_list:
            if door_hook == door:
                return

        door_hook = DoorHook(self, door)
        door.door_list.append(door_hook)
        self.hook_list.append(door_hook)
