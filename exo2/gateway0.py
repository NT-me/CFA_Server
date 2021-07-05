from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep
from server_reg import ServerReg

# http://0.0.0.0:8081/pong

app = FastAPI()
myAdress = "0.0.0.0:25565"

otherAdress = ""

addrList = []


@app.get("/otherServ/{name}")
async def giveIP(name):
    print(addrList)
    # askerIP = askerIP.replace("%3A", ":")
    for item in addrList:
        if item.name == name:
            _addrList = addrList.copy()
            _addrList.remove(item)
            return {"list": _addrList}
    return {"Please register first"}


@app.get("/see")
async def see():
    print(addrList)
    return addrList


@app.post("/register/")
async def register_server(serv: ServerReg):
    if serv not in addrList:
        addrList.append(serv)
        return {"New server added !"}
    else:
        return {"Server aldready saved !"}
