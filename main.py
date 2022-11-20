import logging

from Request import Request
from RequestStatus import RequestStatus
from sqla_util import *

import ClassHandling


def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    building = ClassHandling.addBuilding("CECS")
    room = ClassHandling.addRoom(building, 303)
    print("DEBUG ROOM:", room)
    door_name = ClassHandling.addDoorName("Front")
    door = ClassHandling.addDoor(building, room, door_name)
    print(f"\t{door_name.location} in Room {building.type} {room.number} with ID {door.id}")
    employees = ClassHandling.getEmployees("Jared")
    print(employees)
    employee = ClassHandling.addEmployee("Jared Seville")
    print(ClassHandling.getEmployees("Jared"))
    hook = ClassHandling.getHook(1)
    print(hook)
    hook = ClassHandling.addHook(1, [door])
    print(hook)
    key = ClassHandling.getKey(1)
    print(key)
    key = ClassHandling.addKey(1, 1)
    print(key)

    print("EMPLOYEE DEBUG:", employees[0])
    request = ClassHandling.makeRequest(employees[0], building, room)
    print("REQUEST DEBUG:", request)
    jared_request: [Request] = ClassHandling.getRequests(employees[0])
    print(f"Jared's Requests: {jared_request}")
    for x in jared_request:
        if ClassHandling.getRequestStatus(x) == RequestStatus.OUT:
            ClassHandling.updateStatus(x, RequestStatus.LOST)
    print()


if __name__ == '__main__':
    main()
