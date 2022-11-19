import logging

from sqla_util import *

import ClassHandling


def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    # Create Tables for Entity Classes
    metadata.create_all(bind=engine)

    building = ClassHandling.addBuilding("CECS")
    room = ClassHandling.addRoom(building, 303)
    door_name = ClassHandling.addDoorName("Front")
    door = ClassHandling.addDoor(building, room, door_name)
    print(f"\t{door_name.location} in Room {building.type} {room.number} with ID {door.id}")


if __name__ == '__main__':
    main()
