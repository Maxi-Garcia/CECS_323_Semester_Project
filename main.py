import logging

from sqla_util import *

import ClassHandling


def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    building = ClassHandling.addBuilding("CECS")
    room = ClassHandling.addRoom(building, 303)
    door_name = ClassHandling.addDoorName("Front")
    door = ClassHandling.addDoor(building, room, door_name)
    print(f"\t{door_name.location} in Room {building.type} {room.number} with ID {door.id}")
    employees = ClassHandling.getEmployees("Jared")
    print(employees)
    employee = ClassHandling.addEmployee("Jared Seville")
    print(employee)
    print(ClassHandling.getEmployees("Jared"))
    hook = ClassHandling.getHook(1)
    print(hook)
    hook = ClassHandling.addHook(1, [door])


if __name__ == '__main__':
    main()
