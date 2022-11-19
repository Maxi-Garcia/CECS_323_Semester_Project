from sqlalchemy import Column, Integer, Sequence, Identity
from sqlalchemy.orm import relationship

import DoorHook
import Door
from main import Base
from DoorHook import DoorHook


class Hook(Base):
    __tablename__ = "hooks"
    id = Column("id", Integer, Identity(start=0, cycle=True), nullable=False, primary_key=True)

    door_list: [DoorHook] = relationship("DoorHook", back_populates="hook", viewonly=False, lazy="subquery")

    def __init__(self, id_: int):
        self.id = id_
        self.door_list = list()

    def add_door(self, door: Door):
        for door_hook in self.door_list:
            if door_hook == door:
                return

        door_hook = DoorHook(self, door)
        door.hook_list.append(door_hook)
        self.door_list.append(door_hook)

    def __str__(self):
        return f"Hook {self.id} opens {self.door_list}"

    def __repr__(self):
        return self.__str__()
