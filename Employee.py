from sqlalchemy import Integer, Sequence, Column, String
from sqlalchemy.orm import relationship

import Request
from main import Base


class Employee(Base):
    __tablename__ = "employees"
    id = Column("id", Integer, Sequence("employee_id_seq"), nullable=False, primary_key=True)
    name = Column("name", String(40), nullable=False, primary_key=False)

    room_list: [Request] = relationship("Request", back_populates="room", viewonly=False)

    def __int__(self, id: int, name: str):
        self.id = id
        self.name = name
