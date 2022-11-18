from sqlalchemy import String, Column, ForeignKey, Integer, ForeignKeyConstraint, Sequence
from sqlalchemy.orm import relationship

import DoorHook
import Hook
from main import Base
from DoorHook import DoorHook


class Door(Base):
    __tablename__ = "doors"
    id = Column("id", Integer, Sequence("door_id_seq"), nullable=False, primary_key=True)
    building_type = Column("building_type", String(40), nullable=False, primary_key=False)
    room_number = Column("room_number", Integer(), nullable=False, primary_key=False)
    location = Column("location", String(40), ForeignKey("door_names.location"), nullable=False, primary_key=False)

    location_relationship = relationship("DoorName")

    table_args = (ForeignKeyConstraint((building_type, room_number),
                                       ["rooms.building_type", "rooms.number"]))

    hook_list: [DoorHook] = relationship("DoorHook", back_populates="door", viewonly=False)

    def __init__(self, id: int, building_type: str, number: int, location: str):
        self.id = id
        self.building_type = building_type
        self.number = number
        self.location = location
        self.door_hook_list = []

    def add_hook(self, hook: Hook):
        for door_hook in self.door_hook_list:
            if door_hook == hook:
                return

        door_hook = DoorHook(hook, self)
        hook.door_list.append(door_hook)
        self.hook_list.append(door_hook)
