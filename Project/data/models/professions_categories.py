from sqlalchemy import Integer, Column, String, orm
from sqlalchemy_serializer import SerializerMixin

from Project.data.db_session import SqlAlchemyBase


class ProfessionsCategories(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'professions_categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)

    professions = orm.relation('Profession', back_populates='professions_categories')