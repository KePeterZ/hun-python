#!/usr/bin/env python3

import sys
import os
import json

fajlNev = sys.argv[1]
magyarFajl = open(fajlNev, "r")
magyarFajlLista = magyarFajl.readlines()

with open("magyarJson.json", "r") as hunCmdk:
    magyarParancsok = json.loads(hunCmdk.read())

magyarRunFajl = []
for magyarSor in magyarFajlLista: 
    magyarTempSor = magyarSor
    for parancs in magyarParancsok.keys():
        magyarTempSor = magyarTempSor.replace(parancs, magyarParancsok[parancs])
    magyarRunFajl.append(magyarTempSor)

with open("temp.py", "w") as szerkesztett:
    szerkesztett.writelines(magyarRunFajl)
