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
    name = Column(String(150), nullable=False)
    hash = Column(String(100), nullable=False)


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
    def add(db, user, items):
        for item in items:
            contact = db.query(Blacklist).filter_by(phone=item, user=user).first()
            if not contact:
                db.add(Blacklist(user, item))
        db.commit()

    @staticmethod
    def list(db, user):
        return [contact.phone for contact in db.query(Blacklist).filter_by(user=user).all()]

    @staticmethod
    def delete(db, user, phones):
        if phones:
            db.query(Blacklist).filter(Blacklist.user == user).filter(Blacklist.phone.in_(phones)).delete(
                synchronize_session=False)
        else:
            db.query(Blacklist).filter_by(user=user).delete(synchronize_session=False)
        db.commit()


class Contact(Base, DictMixin):
    __tablename__ = "contact"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user = Column(Integer, nullable=False)
    label = Column(String(150), nullable=False)
    phone = Column(String(1024), nullable=False)

    def __init__(self, user, phone, label):
        self.user = user
        self.phone = phone
        self.label = label

    def __repr__(self):
        return f"<Contact({self.id}, {self.user}, {self.phone}, {self.label})>"

    @staticmethod
    def add(db, user, items):
        for item in items:
            contact = db.query(Contact).filter_by(phone=item["phone"], user=user).first()
            if contact:
                contact.label = item["label"]
            else:
                item["user"] = user
                db.add(Contact(**item))
        db.commit()

    @staticmethod
    def list(db, user):
        return [{"label": contact.label, "phone": contact.phone}
                for contact in db.query(Contact).filter_by(user=user).all()]

    @staticmethod
    def delete(db, user, phones):
        if phones:
            db.query(Contact).filter(Contact.user == user).filter(Contact.phone.in_(phones)).delete(
                synchronize_session=False)
        else:
            db.query(Contact).filter_by(user=user).delete(synchronize_session=False)
        db.commit()
