from sqlalchemy import orm, Column, Integer, String, DateTime, ForeignKey
from .db_session import SqlAlchemyBase
import datetime


class Request(SqlAlchemyBase):
    __tablename__ = "Requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status_id = Column(Integer, ForeignKey("Statuses.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("Problems.id"), nullable=False)
    other_info = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.datetime.now().strftime("%d-%m-%Y %H"))

    status = orm.relation("Status")
    user = orm.relation("User")
    problem = orm.relation("Problem")
