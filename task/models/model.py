import datetime

from sqlalchemy import Column, Text, Integer, String, DateTime, func, Boolean, ForeignKey

from task.config.db import DB_BASE

# models
# Book model
class Book(DB_BASE):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, default=False)
    author = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    publication_year = Column(Integer, nullable=False)

# Review model
# review rating : which is by default is 0 or range from 0-5
class Review(DB_BASE):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer, nullable=False,default=0)
    created_at = Column(DateTime, default=func.now())
    book_id = Column(Integer, ForeignKey('book.id'))
    text_review = Column(Text, nullable=False, default=False)

