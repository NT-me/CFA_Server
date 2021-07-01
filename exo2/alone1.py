from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep

# http://0.0.0.0:8081/pong

app = FastAPI()
myAdress = "0.0.0.0:8080"

otherAdress = ""


def send_ping():
    global otherAdress
    global myAdress
    if otherAdress != "":
        resp = r.get("http://"+otherAdress.replace("\"","").replace("[", "").replace("]", "")+"/pingpong")
        print(resp.text)
    else:
        reqAdrr = r.get("http://0.0.0.0:25565/otherServ/{}".format(myAdress))
        otherAdress = reqAdrr.text
        print(reqAdrr.text)

@app.get("/pingpong")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_ping)
    sleep(0.5)
    return {"Pong"}