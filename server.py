import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
import numpy as np
from collections import Counter

app = FastAPI()

TOKEN = "1337_1337_1337_1337_1337_1337_1337_1337"


def checkIp(ip):
    df = pd.read_csv("main.csv")

    if ip not in df.iloc[:, 0].values:
        return True
    else:
        return False


@app.get("/{token}={ip}")
def index(token: str, ip: str):
    df = pd.read_csv("main.csv")

    if token == TOKEN:
        return {
            "ip": ip
        }
    return "Wrong API Token!"


@app.get("/add/{token}={ip}={userVote}")
def addIp(ip: str, userVote: str, token: str):
    df = pd.read_csv("main.csv")

    if token == TOKEN:
        if checkIp(ip):
            file = open("main.csv", "a")
            if userVote.lower() == "paster":
                file.write(f"\n{ip},1,0")
                file.close()
                return f"{ip} has voted for {userVote}"
            else:
                file.write(f"\n{ip},0,1")
                file.close()
                return f"{ip} has voted for {userVote}"
        else:
            return "User has already voted!"
    else:
        return "Wrong Token"


@app.get("/get/paster")
def votesPaster():
    df = pd.read_csv("main.csv")

    unique, counts = np.unique(df.iloc[:, 1].values, return_counts=True)
    finalDict = dict(zip(unique, counts))
    return ({
        0: f"{finalDict[0]}",
        1: f"{finalDict[1]}"
    })


@app.get("/get/ruzgar")
def votesRuzgar():
    df = pd.read_csv("main.csv")

    unique, counts = np.unique(df.iloc[:, 2].values, return_counts=True)
    finalDict = dict(zip(unique, counts))
    return ({
        0: f"{finalDict[0]}",
        1: f"{finalDict[1]}"
    })


if __name__ == "__main__":
    uvicorn.run("server:app", port=1337, reload=True, access_log=False)
