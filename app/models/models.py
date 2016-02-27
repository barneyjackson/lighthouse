import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class QuestionAnswer(Base):
    __tablename__ = "questionanswers"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)

    question = Column(String)
    answer = Column(String)

class PendingQuestion(Base):
    __tablename__ = "pendingquestions"

    id = Column(Integer, primary_key=True)

    question_answer_id = Column(Integer, ForeignKey("questionanswers.id"))
    created_at = Column(DateTime, default=datetime.datetime.now)
    answered = Column(Boolean, default=False)
