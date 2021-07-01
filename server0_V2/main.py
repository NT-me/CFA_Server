from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep

onoff = True

app = FastAPI()

def send_ping():
    if onoff :
        resp = r.get("http://0.0.0.0:8081/pong")
        print(resp.text)

@app.get("/ping")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_ping)
    sleep(0.5)
    return {"Pong"}
