from sqlalchemy import orm, Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from .db_session import SqlAlchemyBase


class Admin(SqlAlchemyBase, UserMixin):
    __tablename__ = "Admins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
