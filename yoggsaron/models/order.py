# coding: utf-8

from datetime import datetime

from yoggsaron.ext import db
from .dish import Dish
from .base import Base


class OrderDish(db.Model):

    order_id = db.Column(db.ForeignKey('order.id'), primary_key=True)
    dish_id = db.Column(db.ForeignKey('dish.id'), primary_key=True)
    created = db.Column(db.DateTime, default=datetime.now)


class Order(Base):

    __tablename__ = 'order'

    time = db.Column(db.DateTime, default=datetime.now, index=True)
    owner_id = db.Column(db.Integer, nullable=False, index=True)
    dishes = db.relationship(Dish, secondary=OrderDish.__table__)

    def add_dish(self, dish):
        self.dishes.append(dish)
        db.session.add(self)
        db.session.commit()
