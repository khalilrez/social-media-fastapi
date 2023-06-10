from pydantic import BaseModel
from models.comment import Comment

class UserPostIn(BaseModel):
    name: str
    body: str
    user_id: int

class UserPost(UserPostIn):
    id: int

class UserPostWithComments(UserPost):
    comments: list[Comment]