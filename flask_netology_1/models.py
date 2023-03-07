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
