from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class QuestionAnswer(Base):
    __tablename__ = "questionanswers"

    id = Column(Integer, primary_key=True)

    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, server_default=text("sysdate"))

class PendingQuestion(Base):
    __tablename__ = "pendingquestions"

    id = Column(Integer, primary_key=True)

    question_answer_id = Column(Integer, ForeignKey("questionanswers.id"))
    created_at = Column(DateTime, server_default=text("sysdate"))

