from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy_serializer import SerializerMixin

from Project.data.db_session import SqlAlchemyBase


class Profession(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('professions_categories.id'))

    professions_categories = orm.relation('ProfessionsCategories')