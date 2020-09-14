import json
from Engine.Until.object_init import FontLoad
fontSetting="./Resources/fontsSetting.json"
fontSetting=json.load(open(fontSetting,encoding="utf-8"))
class FontsSetting():
    NormalText=eval("FontLoad('"+fontSetting["Text"]+"',"+"20)")
    BoldText=eval("FontLoad('"+fontSetting["TextBold"]+"',"+"20)")