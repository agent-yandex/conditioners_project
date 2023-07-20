from sqlalchemy import orm, Column, Integer, String
from .db_session import SqlAlchemyBase
import datetime


class Status(SqlAlchemyBase):
    __tablename__ = "Statuses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)

    request = orm.relation("Request", back_populates="status")
