from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

Base = declarative_base()

class Reader(Base):
    __tablename__ = "readers"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    borrowings = relationship("Borrowing", back_populates="reader")


class Book(Base):
    __tablename__ = "books"
    ISBN = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(DateTime, nullable=False)
    category = Column(String, nullable=False)

    copies = relationship("Copy", back_populates="book")


class Copy(Base):
    __tablename__ = "copies"
    id = Column(Integer, primary_key=True, index=True)
    ISBN = Column(Integer, ForeignKey("books.ISBN"), nullable=False)

    book = relationship("Book", back_populates="copies")
    borrowings = relationship("Borrowing", back_populates="copy")


class Borrowing(Base):
    __tablename__ = "borrowings"
    copy_id = Column(Integer, ForeignKey("copies.id"), primary_key=True)
    reader_id = Column(Integer, ForeignKey("readers.id"), primary_key=True)
    borrow_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)

    reader = relationship("Reader", back_populates="borrowings")
    copy = relationship("Copy", back_populates="borrowings")
