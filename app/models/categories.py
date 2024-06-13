from pydantic import field_validator
import re
from app.models.base import CustomBaseModel

class Category(CustomBaseModel):
    name: str
    slug: str
    
    @field_validator('slug')
    def validate_slug(cls, value):
        # if not re.match('^([a-z]-|_)+$', value):
        if not re.match('^[a-z-_]+$', value):            
            raise ValueError('Invalid Slug')
        return value

# from pydantic import BaseModel, Field, field_validator
# import re

# class Category(BaseModel):
#     name: str
#     slug: str
    
#     @field_validator('slug')
#     def validate_slug(cls, value):
#         if not re.match('^([a-z]|_)+$', value):
#             raise ValueError('Invalid Slug')
#         return value
