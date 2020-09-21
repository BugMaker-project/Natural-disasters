import json
from Engine.Until.object_init import FontLoad
fontSetting="./Resources/fontsSetting.json"
fontSetting=json.load(open(fontSetting,encoding="utf-8"))
imageSetting="./Resources/imageSetting.json"
fontSetting=json.load(open(fontSetting,encoding="utf-8"))
class FontsSetting():
    NormalText=+fontSetting["Text"]
