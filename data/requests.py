from sqlalchemy import orm, Column, Integer, String, DateTime, ForeignKey
from .db_session import SqlAlchemyBase
import datetime


class Request(SqlAlchemyBase):
    __tablename__ = "Requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status_id = Column(Integer, ForeignKey("Statuses.id"), nullable=False)
    user_name = Column(String, nullable=False)
    user_number = Column(Integer, nullable=False)
    city_id = Column(Integer, ForeignKey("Cities.id"))
    problem = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now().strftime("%d-%m-%Y %H"))

    city = orm.relation("City")
    status = orm.relation("Status")
