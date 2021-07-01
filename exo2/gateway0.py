from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep

# http://0.0.0.0:8081/pong

app = FastAPI()
myAdress = "0.0.0.0:25565"

otherAdress = ""

addrList = ["0.0.0.0:8080", "0.0.0.0:8081"]


@app.get("/otherServ/{askerIP}")
async def giveIP(askerIP):
    _addrList = addrList.copy()
    _addrList.remove(askerIP.replace("%3A",":"))
    return _addrList
