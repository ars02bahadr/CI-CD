from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Merhaba ArgoCd,Github Actions,Docker,Kubernetes!"}
