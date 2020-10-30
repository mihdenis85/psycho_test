from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ..db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    country = Column(String)
    city = Column(String)
    email = Column(String, index=True, unique=True)
    age = Column(Integer)
    test1_results = Column(String)
    test2_results = Column(String)
    hashed_password = Column(String)


    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)