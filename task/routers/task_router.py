import logging

from fastapi import APIRouter, Request, Depends

from task.controller.task_controller import form
from task.schema.tasks import book_info, review_info, get_book_info

router = APIRouter(
    prefix='/new_task',
    tags=["new_task API's"],
)


# Add book details
@router.post('/add')
async def add(data: book_info):
    result = form.add_book(data)
    return {"success": "OK", "message": "New book Information added successfully", "data": result}


# Retrieve all books with an option to filter by author or publication year
@router.get('/book_details')
async def book_information(author_or_p_year:get_book_info):
    result = form.book_details(author_or_p_year)
    return {"success": "OK", "message": "Book details", "data": result}

# Retrieve all reviews for a specific book
@router.get('/book_details/{book_name}')
async def reviews(book_name:str):
    result = form.book_reviews(book_name)
    return {"success": "OK", "message": "Reviews", "data": result}


# Add review
@router.post('/review')
async def review(info:review_info):
    result = form.add_review(info)
    return {"success": "OK", "message": "Review added successfully", "data": result}

# Edit book Information
@router.patch('/update_book/{book_id}')
async def edit(book_id: int,update_book:book_info):
    result = form.book_edit(book_id,update_book)
    return {"success": "OK", "message": "Data updated successfully", "data": result}


# Delete single book information
@router.delete("/book_delete/{book_id}")
def delete_book(book_id: int):
    result = form.delete_book(book_id)
    return {"success": "OK", "message": "Book is successfully deleted", "data": result}

# Edit review Information
@router.patch('/update_review/{review_id}')
async def edit_review(review_id: int,update_review:review_info):
    result = form.review_edit(review_id,update_review)
    return {"success": "OK", "message": "Review updated successfully", "data": result}


# Delete single Review information
@router.delete("/review_delete/{review_id}")
def delete_review(review_id: int):
    result = form.delete_review(review_id)
    return {"success": "OK", "message": "Review is successfully deleted", "data": result}


