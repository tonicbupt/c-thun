# coding: utf-8

from yoggsaron.ext import db
from .base import Base


class Restaurant(Base):

    __tablename__ = 'restaurant'

    name = db.Column(db.String(50), nullable=False)
    addr = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(50), nullable=False)
