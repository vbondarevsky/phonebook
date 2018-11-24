from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from phonebook import config
from phonebook.db.models import Base


async def open_db(app):
    uri = f"sqlite:///{config.db.name}"
    engine = create_engine(uri)
    Base.metadata.create_all(engine)
    app["db"] = scoped_session(sessionmaker(bind=engine))


async def close_db(app):
    app["db"].remove()
