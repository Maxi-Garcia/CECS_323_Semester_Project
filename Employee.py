from sqlalchemy import Integer, Sequence, Column, String, Identity
from sqlalchemy.orm import relationship

import Request
from main import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column("id", Integer, Identity(start=0, cycle=True), nullable=False, primary_key=True)
    name = Column("name", String(40), nullable=False, primary_key=False)

    room_list: [Request] = relationship("Request")

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name} (ID: {self.id})"

    def __repr__(self):
        return self.__str__()
