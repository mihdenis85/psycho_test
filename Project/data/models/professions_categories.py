from sqlalchemy import Integer, Column, String

from Project.data.db_session import SqlAlchemyBase


class ProfessionsCategories(SqlAlchemyBase):
    __tablename__ = 'professions_categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)