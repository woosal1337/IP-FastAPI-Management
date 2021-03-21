from collections import Counter
import pandas as pd
import numpy as np

df = pd.read_csv("main.csv")

def addIp(ip, userVote):
    if ip not in df.iloc[:, 0].values:
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
        return "You have already voted!"

def checkIp(ip):
    if ip not in df.iloc[:, 0].values:
        print()
        return f"{ip} has not voted yet!"

def votesPaster():
    unique, counts = np.unique(df.iloc[:, 1].values, return_counts=True)
    print(dict(zip(unique, counts)))
    print(dict(zip(unique, counts)) + dict(zip(unique, counts)))
    return(dict(zip(unique, counts)))

votesPaster()