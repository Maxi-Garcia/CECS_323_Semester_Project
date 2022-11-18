import datetime

from sqlalchemy import Integer, ForeignKey, Column, DateTime, Sequence, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship

from main import Base


class Request(Base):
    __tablename__ = "requests"
    requests_id = Column("requests_id", Integer, Sequence("requests_id_seq"), nullable=False, primary_key=True)
    borrow_date = Column("loss_date", DateTime, nullable=False, primary_key=False)
    employees_id = Column("employees_id", Integer, ForeignKey("employees.id"), nullable=False, primary_key=False)
    rooms_number = Column("rooms_number", Integer, nullable=False, primary_key=False)
    building_type = Column("building_type", String(40), nullable=False, primary_key=False)
    key_id = Column("key_id", Integer, ForeignKey("key_copies.key_id"), nullable=False, primary_key=False)

    request_relationship = relationship("Request")

    table_args = (ForeignKeyConstraint((building_type, rooms_number),
                                       ["rooms.building_type", "rooms.number"]))

    employee = relationship("Employee", back_populates="request_list")
    room = relationship("Room", back_populates="employee_list")

    def __init__(self, requests_id: int, borrow_date: datetime, employees_id: int, rooms_number: int,
                 building_type: str, key_id: int):
        self.requests_id = requests_id
        self.borrow_date = borrow_date
        self.employees_id = employees_id
        self.rooms_number = rooms_number
        self.building_type = building_type
        self.key_id = key_id
