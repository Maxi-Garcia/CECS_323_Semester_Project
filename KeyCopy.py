from sqlalchemy import Column, Integer, Sequence, ForeignKey

from main import Base


class KeyCopy(Base):
    __tablename__ = "key_copies"
    key_id = Column("key_id", Integer, Sequence('key_id_seq'), nullable=False, primary_key=True)
    hooks_id = Column("key_id", Integer, ForeignKey("hooks.id"), nullable=False, primary_key=False)

    def __init__(self, key_id: int, hooks_id: int):
        self.key_id = key_id
        self.hooks_id = hooks_id
