from BuildingType import BuildingType
from Room import Room
from main import Session
from sqlalchemy import exc


def test_building():
    with Session() as sess:
        building = BuildingType("CECS")
        room = Room(building, 303)
        sess.add(building)
        sess.add(room)
        sess.commit()


def addBuilding(name: str) -> BuildingType or None:
    building = BuildingType(name)
    try:
        with Session() as sess:
            sess.add(building)
            sess.commit()
        return building
    except exc.SQLAlchemyError as error:
        print("Add Building Failed:", error)
        return None


def addRoom(building: BuildingType, number: int):
    try:
        with Session() as sess:
            Room(building.type, number)
            sess.commit()
        return building
    except exc.SQLAlchemyError as error:
        print("Add Building Failed:", error)
        return None
