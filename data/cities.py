from sqlalchemy import orm, Column, Integer, String
from .db_session import SqlAlchemyBase
import datetime


class City(SqlAlchemyBase):
    __tablename__ = "Cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String, nullable=False)

    request = orm.relation("Request", back_populates="city")
