from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep

# http://0.0.0.0:8081/pong

app = FastAPI()
myAdress = "0.0.0.0:25565"

otherAdress = ""

addrList = []


@app.get("/otherServ/{askerIP}")
async def giveIP(askerIP):
    print(addrList)
    askerIP = askerIP.replace("%3A",":")
    if askerIP not in addrList:
        addrList.append(askerIP)
    else:
        _addrList = addrList.copy()
        _addrList.remove(askerIP)
        return _addrList


@app.get("/see")
async def see():
    print(addrList)
    return addrList
