from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Sequence
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DictMixin:
    def dict(self):
        return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())


class User(Base, DictMixin):
    __tablename__ = "user"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user = Column(String(150), nullable=False)
    password = Column(String(32), nullable=False)


class Blacklist(Base, DictMixin):
    __tablename__ = "blacklist"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user = Column(Integer, nullable=False)
    phone = Column(String(1024), nullable=False)

    def __init__(self, user, phone):
        self.user = user
        self.phone = phone

    def __repr__(self):
        return f"<Blacklist({self.id}, {self.user}, {self.phone})>"

    @staticmethod
    def add(db, items):
        for item in items:
            db.add(Blacklist(**item))
        db.commit()

    @staticmethod
    def list(db):
        return [item.dict() for item in db.query(Blacklist).all()]


class Contact(Base, DictMixin):
    __tablename__ = "contact"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user = Column(Integer, nullable=False)
    name = Column(String(150), nullable=False)
    phone = Column(String(1024), nullable=False)

    def __init__(self, user, phone, name):
        self.user = user
        self.phone = phone
        self.name = name

    def __repr__(self):
        return f"<Contact({self.id}, {self.user}, {self.phone}, {self.name})>"

    @staticmethod
    def add(db, items):
        for item in items:
            db.add(Contact(**item))
        db.commit()

    @staticmethod
    def list(db):
        return [contact.dict() for contact in db.query(Contact).all()]
