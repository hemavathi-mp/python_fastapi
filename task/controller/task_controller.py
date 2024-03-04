import datetime
import logging
from http.client import HTTPException

from task.config.db import SessionLocal
from task.controller.email import sending_email

from task.models.model import Book, Review


class form:

    def add_book(params):
        data = params.dict()

        with SessionLocal() as session:
            result = Book(**data)
            session.add(result)
            session.commit()
            session.refresh(result)

            return {"book_id":result.id}



    def book_details(author_or_p_year):
        data = author_or_p_year.dict()
        with SessionLocal() as session:
            if data["auther"] is not None:
                db_user = session.query(Book).filter(Book.author == data["auther"]).all()
            else:
                db_user = session.query(Book).filter(Book.publication_year == data["publication_year"]).all()

            if not db_user:
                raise HTTPException(status_code=404, detail="Book not found")

            return db_user

    def book_reviews(book_name):
        with SessionLocal() as session:
            db_user = session.query(Book).get(book_name)
            if not db_user:
                raise HTTPException(status_code=404, detail="Book not found")

            query = session.query(Review).filter(Review.book_id == db_user.id).all()

            if not query:
                raise HTTPException(status_code=404, detail="Review not found")

            return db_user

    def add_review(info):
        data = info.dict()
        with SessionLocal() as session:
            result = Review(**data)
            session.add(result)
            session.commit()
            session.refresh(result)

            email_info = sending_email()

            return {"message":"Review added successfully","review_id":result.id, "email_info":email_info}

    def book_edit(book_id,update_book):
        with SessionLocal() as session:

            db_book = session.query(Book).get(book_id)
            if not db_book:
                raise HTTPException(status_code=404, detail="book not found")

            stored_data = update_book.dict()
            stored_model = Book(**stored_data)
            update_data = update_book.dict(exclude_unset=True)
            updated_data = stored_model.copy(update=update_data)
            post = jsonable_encoder(updated_data)

            return {"Book updated succussfully"}


    def review_edit(review_id,update_review):
        with SessionLocal() as session:

            db_book = session.query(Review).get(review_id)
            if not db_book:
                raise HTTPException(status_code=404, detail="Review not found")

            stored_data = update_review.dict()
            stored_model = Review(**stored_data)
            update_data = update_review.dict(exclude_unset=True)
            updated_data = stored_model.copy(update=update_data)
            post = jsonable_encoder(updated_data)

            return {"review updated succussfully"}


    def delete_book(book_id):
        with SessionLocal() as session:
            db_book = session.query(Book).get(book_id)
            if not db_book:
                raise HTTPException(status_code=404, detail="Book not found")

            session.delete(db_book)
            session.commit()
            return {"ok": True}


    def delete_review(review_id):
        with SessionLocal() as session:
            db_review= session.query(Review).get(review_id)
            if not db_review:
                raise HTTPException(status_code=404, detail="Review not found")

            session.delete(db_review)
            session.commit()
            return {"ok": True}






