from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep
from server_reg import ServerReg

# http://0.0.0.0:8081/pong

app = FastAPI()
otherAdress = []
brokerAddr = ""

me = ServerReg(name="alone2", adress="host.docker.internal:8081")


@app.on_event("startup")
async def startup_event():
    global brokerAddr
    # r.get("http://host.docker.internal:25565/otherServ/{}".format(me.adress))
    print(me.dict())
    resp = r.post("http://host.docker.internal:25565/register/", json=me.dict())
    print(resp.text)
    while brokerAddr == "":
        sleep(0.5)
        addrList = r.get("http://host.docker.internal:25565/otherServ/{}".format(me.name))
        addrList = addrList.json()["list"]
        for server in addrList:
            if server["name"] == "broker0":
                brokerAddr = server["adress"]


def send_ping():
    resp = r.get("http://" + brokerAddr + "/sendMsg/to/alone1")
    print(resp.text)

@app.get("/pingpong")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_ping)
    sleep(0.5)
    return {"Ping"}
