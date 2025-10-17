from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    return {"message": "Hello World!"}

@app.get("/")
def root():
    return {"message": "OK"}
