# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)


class TBusinessTradeOrder(Base):
    __tablename__ = 't_business_trade_order'

    id = Column(Integer, primary_key=True)
    business_order_id = Column(Integer)
    business_order_code = Column(String(50))
    business_order_type = Column(Integer)
    trade_order_no = Column(String(32))
    trade_order_type = Column(Integer)
    price = Column(Numeric(13, 2))
    pay_voucher_url = Column(String(200))
    trade_time = Column(DateTime)
    submit_time = Column(DateTime)
    status = Column(Integer)
    account_type = Column(String(32))
    is_tally = Column(Integer)
    create_user_id = Column(Integer)
    create_time = Column(DateTime)
    update_user_id = Column(Integer)
    update_time = Column(DateTime)
    remark = Column(String(500))


class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True)
    role_id = Column(ForeignKey(u'roles.id'), index=True)

    role = relationship(u'Role')
