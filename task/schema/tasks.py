from pydoc import text

from pydantic import BaseModel, validator

# schema
class book_info(BaseModel):
    title :str=None
    author :str=None
    publication_year :str=None


class get_book_info(BaseModel):
    author :str=None
    publication_year :int=None

class review_info(BaseModel):
    rating :int=0
    text_review: text = None

    # data validation using pydantic models
    @validator("rating")
    def ratings_validation(cls,rating:int):
        if rating > 5:
            raise ValueError('Ratings must between 0-5')


