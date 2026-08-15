from fastapi import FastAPI


app = FastAPI()



@app.get("/welcome", tags=['General'])
def welcome():
    return{
        "message":"Welcome to our APP"
    }
