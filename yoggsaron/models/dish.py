# coding: utf-8

from yoggsaron.ext import db
from yoggsaron.utils import parse_price
from .base import Base


class Dish(Base):

    __tablename__ = 'dish'

    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False, default=0)
    rid = db.Column(db.Integer, nullable=False, index=True)
    status = db.Column(db.Integer, nullable=False, index=True, default=0)

    @classmethod
    def create(cls, name, price, rid):
        dish = cls(name=name, price=parse_price(price), rid=rid)
        db.session.add(dish)
        db.session.commit()
        return dish
