from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "welcome to my APIs"}

@app.get("/posts")
def get_posts():
    return{"data":"This is your posts"}
