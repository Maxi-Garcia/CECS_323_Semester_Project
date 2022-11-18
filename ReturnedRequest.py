import datetime

from sqlalchemy import Integer, ForeignKey, Column, DateTime
from sqlalchemy.orm import relationship

from main import Base


class ReturnedRequest(Base):
    __tablename__ = "returned_requests"
    requests_id = Column("requests_id", Integer, ForeignKey("requests.requests_id"), nullable=False, primary_key=True)
    return_date = Column("return_date", DateTime, nullable=False, primary_key=False)

    request_relationship = relationship("Request")

    def __init__(self, requests_id: int, return_date: datetime):
        self.requests_id = requests_id
        self.return_date = return_date
