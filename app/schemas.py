# sourcery skip: avoid-builtin-shadow
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional

'''Schema for post request'''
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UpdatePost(PostBase):
    pass


class CreatePost(PostBase):
    pass

class UserOut(BaseModel):
    id:int
    email: EmailStr
    created_at: datetime
    
    #Stops 'not a valid dict error'
    class Config:
        orm_mode = True
        
        
#Response format
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    #Prevent the not a valid dict error
    class Config:
        orm_mode = True

    
class Vote(BaseModel):
    post_id: int 
    dir: conint(le=1) #less than 1, allows negative, need checking 

#make the first letter P of 'Post' capital as below to 
#prevent this error: 'field required (type=value_error.missing)'   
class PostOut(BaseModel):
    Post: Post
    votes: int
    
    #Prevent the 'value is not a valid dic (type=type_error.dict)'
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str 
    

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    


     


    

