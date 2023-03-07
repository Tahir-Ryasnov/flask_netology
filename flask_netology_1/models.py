import pydantic
from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:29072017svadba@127.0.0.1:5432/advert_flask")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class Advert(Base):

    __tablename__ = 'advertisements'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    owner = Column(String, nullable=False)
    creation_date = Column(DateTime, server_default=func.now())


Base.metadata.create_all(engine)


class CreateAdvert(pydantic.BaseModel):
    title: str
    description: str
    owner: str

    @pydantic.validator("title")
    def is_ascii_title(cls, value: str):
        if not value.isascii():
            raise ValueError('incorrect title')
        return value

    @pydantic.validator("description")
    def is_ascii_description(cls, value: str):
        if not value.isascii():
            raise ValueError('incorrect description')
        return value

    @pydantic.validator("owner")
    def is_ascii_owner(cls, value: str):
        if not value.isascii():
            raise ValueError('incorrect owner name')
        return value
