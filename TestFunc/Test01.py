import json
with open(r"./Data/Info.json","r") as jn:
    str=jn.read()
print(json.loads(str)["Devlop Version"]["JDK-Version(lzhbhlrPython)"])