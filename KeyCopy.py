from sqlalchemy import Column, Integer, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from main import Base


class KeyCopy(Base):
    __tablename__ = "key_copies"
    key_id = Column("key_id", Integer, Sequence('key_id_seq'), nullable=False, primary_key=True)
    hooks_id = Column("hooks_id", Integer, ForeignKey("hooks.id"), nullable=False, primary_key=False)

    hook = relationship("Hook", back_populates="keys")

    def __init__(self, key_id: int, hooks_id: int):
        self.key_id = key_id
        self.hooks_id = hooks_id

    def __str__(self):
        return f"Key {self.key_id} (Hook {self.hooks_id})"

    def __repr__(self):
        return self.__str__()
