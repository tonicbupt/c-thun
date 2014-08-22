# coding: utf-8

from sqlalchemy.inspection import inspect
from sqlalchemy.ext.declarative import declared_attr

from yoggsaron import db


class Base(db.Model):

    __abstract__ = True

    def __repr__(self):
        attrs = ('%s=%r' % (attr.key, attr.value) for attr in inspect(self).attrs)
        attrs_str = ', '.join(attrs)
        return '%s(%s)' % (self.__class__.__name__, attrs_str)

    @declared_attr
    def id(cls):
        return db.Column(db.Integer, primary_key=True, autoincrement=True, default=100000)

    @classmethod
    def get_or_create(cls, auto_commit=True, **data):
        exists = cls.query.filter_by(**data).first()
        if exists is None:
            exists = cls(**data)
            db.session.add(exists)
            if auto_commit:
                db.session.commit()
        return exists

    def delete(self):
        self._pre_deletion()
        db.session.delete(self)
        db.session.commit()
        self._post_deletion()

    def _pre_deletion(self):
        pass

    def _post_deletion(self):
        pass
