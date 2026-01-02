from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
# from fastapi.params import Body
from random import randrange

app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":"title of post 1",
            "content":"content of post 1",
             "id": 1},
             {"title":"favourite foods",
              "content":"O like pizza",
              "id": 2}]



def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


@app.get("/")
def root():
    return {"message": "welcome to my APIs"}

@app.get("/posts")
def get_posts():
    return{"data":my_posts}

@app.post("/posts") 
# def create_post(payload: dict = Body(...)):
def create_post(post: Post):
    # print(post.title  )
    # print(post.content)
    # print(post.published)
    # print(post.rating)
    # print(post.dict())
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict }

    # print(payload)
    # return {"new_post": f
    # "title:{payload['title']}  content:{payload['content']}"} 

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    print(post)
    return {"post_detail": post}