from sqlalchemy import orm, Column, Integer, String
from .db_session import SqlAlchemyBase
import datetime


class Problem(SqlAlchemyBase):
    __tablename__ = "Problems"

    id = Column(Integer, primary_key=True, autoincrement=True)
    problem = Column(String, nullable=False)

    request = orm.relation("Request", back_populates="problem")
