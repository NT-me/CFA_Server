from fastapi import FastAPI, BackgroundTasks
import requests as r
from time import sleep
from server_reg import ServerReg

# http://0.0.0.0:8081/pong

app = FastAPI()
otherAdressMap = dict()

me = ServerReg(name="broker0", adress="host.docker.internal:25566")


@app.on_event("startup")
async def startup_event():
    # r.get("http://host.docker.internal:25565/otherServ/{}".format(me.adress))
    print(me.dict())
    resp = r.post("http://host.docker.internal:25565/register/", json=me.dict())
    print(resp.text)


@app.get("/sendMsg/to/{name}")
async def send_msg_to(name):
    resp_listAddr = r.get("http://host.docker.internal:25565/otherServ/{}".format(me.name))
    listAddr = resp_listAddr.json()
    receiver_addr = ""
    print("listAddr: "+listAddr["list"])
    for server in listAddr["list"]:
        if server["name"] == name:
            receiver_addr = server["adress"]
            resp = r.get("http://"+receiver_addr+"/pingpong")
            return resp.json()
    return {"Server not found !"}
