from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep


app = FastAPI()


def send_pong():
    resp = r.get("http://0.0.0.0:8080/ping")
    print(resp.text)


@app.get("/pong")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_pong)
    sleep(0.5)
    return {"Ping"}
