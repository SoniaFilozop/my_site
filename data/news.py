import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    plos = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    num_kom = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    etag = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    etag_home = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    living = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    kitchen = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    remont = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type_home = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pass_lifts = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    gruz_lifts = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    height = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    pandus = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    parking = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    categories = orm.relation("Category",
                              secondary="association",
                              backref="news")