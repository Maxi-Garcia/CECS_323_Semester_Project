from BuildingType import BuildingType
from Door import Door
from DoorName import DoorName
from Room import Room
from main import Session
from sqlalchemy import exc, select


def getBuilding(name: str) -> BuildingType or None:
    """
    Checks for a match in the database and returns its Object.
    Since they can be uniquely identified this way, this method only returns one object.
    :param name: Building Name (Column: building_types.type)
    :return: Building if it exists, None otherwise.
    """
    with Session() as sess:
        statement = select(BuildingType).where(BuildingType.type == name)
        result = sess.execute(statement)
        for item in result.scalars():
            return item
    return None


def addBuilding(name: str) -> BuildingType or None:
    """
    Adds a building to the database if it does not exist.
    If the building already exists, return the building.
    This will return the first match.
    :param name: Building Name (Column: building_types.type)
    :return: Building if created or already exists, None if error thrown.
    """
    match = getBuilding(name)
    if match is not None:
        return match
    building = BuildingType(name)
    try:
        with Session() as sess:
            sess.add(building)
            sess.commit()
        return building
    except exc.SQLAlchemyError as error:
        print("Add Building Failed:", error)
        return None


def getRoom(building: str, number: int) -> Room or None:
    """
    Checks for a match in the database and returns its Object.
    Since they can be uniquely identified this way, this method only returns one object.
    :param building: Building Name (Column: building_types.type / rooms.building_type)
    :param number: Room Number (Column: rooms.number)
    :return: Room if it exists, None otherwise.
    """
    with Session() as sess:
        statement = select(Room).where(Room.building_type == building and Room.number == number)
        result = sess.execute(statement)
        for item in result.scalars():
            return item
    return None


def addRoom(building: BuildingType or str, number: int) -> Room or None:
    """
    Adds a room to the database if it does not exist.
    If the room already exists, return the room.
    This will return the first match.
    :param building: Building Name (Column: building_types.type / rooms.building_type)
    :param number: Room Number (Column: rooms.number)
    :return: Room if created or already exists, None if error thrown.
    """
    building: str = building.type if type(building) is BuildingType else building
    match = getRoom(building, number)
    if match is not None:
        return match
    room = Room(building, number)
    try:
        with Session() as sess:
            sess.add(room)
            sess.commit()
        return room
    except exc.SQLAlchemyError as error:
        print("Add Room Failed:", error)
        return None


def getDoorName(location: str) -> DoorName or None:
    with Session() as sess:
        statement = select(DoorName).where(DoorName.location == location)
        result = sess.execute(statement)
        for item in result.scalars():
            return item
    return None


def addDoorName(location: str) -> DoorName or None:
    match = getDoorName(location)
    if match is not None:
        return match
    doorName = DoorName(location)
    try:
        with Session() as sess:
            sess.add(doorName)
            sess.commit()
        return doorName
    except exc.SQLAlchemyError as error:
        print("Add DoorName Failed:", error)
        return None


def getDoor(building: BuildingType or Room or str, number: Room or int, location: DoorName or str) -> Door or None:
    """
    Checks for a match in the database and returns its Object.
    Since they can be uniquely identified this way, this method only returns one object.
    :param building: Building Name (Column: building_types.type / rooms.building_type)
    :param number: Room Number (Column: rooms.number)
    :param location: Door Location (Column: door_name.location)
    :return: Room if it exists, None otherwise.
    """
    building: str = building.type if type(building) is BuildingType else building.building_type if type(building) is Room else building
    number: int = Room.number if type(number) is Room else number
    location: str = DoorName.location if type(location) is DoorName else location
    with Session() as sess:
        statement = select(Door).filter(
            (Door.location == location) & (Door.room_number == number) & (Door.building_type == building)
        )
        print(statement)
        result = sess.execute(statement)
        print(result)
        for item in result.scalars():
            return item
    return None


def addDoor(building: BuildingType or Room or str, number: Room or int, location: DoorName or str) -> Door or None:
    match = getDoor(building, number, location)
    if match is not None:
        return match
    building: str = building.type if type(building) is BuildingType else building.building_type if type(building) is Room else building
    number: int = Room.number if type(number) is Room else number
    location: str = DoorName.location if type(location) is DoorName else location
    door = Door(building, number, location)
    try:
        with Session() as sess:
            sess.add(door)
            sess.commit()
        return door
    except exc.SQLAlchemyError as error:
        print("Add Door Failed:", error)
        return None
