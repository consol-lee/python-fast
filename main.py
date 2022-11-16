from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/test")
def timeout_api():
    return {"msg": "test"}

@app.get("/timeout")
def timeout_api():
    time.sleep(30)
    return {"msg": "timeout"}
