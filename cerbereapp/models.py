# -*- coding: utf-8 -*-
#!/usr/bin/env python

from sqlalchemy import Column, Integer, String, Date, Binary\
                    , PrimaryKeyConstraint, ForeignKeyConstraint, ForeignKey
from cerbereapp.database import Base


## Models
## ==================================================

class User(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(50), nullable=False)
    account_type = Column(Integer, ForeignKey("account_types.id"), nullable=False)
    username = Column(String(50), unique=True)
    def __init__(self, name=None, password=None):
        self.username = username
        self.password = password


class AccountType(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'account_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Employee(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    profile_id = Column(Integer, nullable=False)


class Profile(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    profile_name = Column(String(50), nullable=False)


class DocumentModel(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'document_models'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    document_model_name = Column(String(50), nullable=False)
    warning_days = Column(Integer, nullable=False)
    critical_days = Column(Integer, nullable=False)


class Document(Base):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    expiration_date = Column(Date, nullable=False)
    document_scan = Column(Binary)
