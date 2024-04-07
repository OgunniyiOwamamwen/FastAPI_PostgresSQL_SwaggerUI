import os
import sys
from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

from database import Base

# Base  = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)

class Choices(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
