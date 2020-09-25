import json
fontSetting = "./Resources/fontsSetting.json"
fontSetting = json.load(open(fontSetting, encoding="utf-8"))
imageSetting = "./Resources/imageSetting.json"
imageSetting = json.load(open(imageSetting, encoding="utf-8"))


class FontsSetting():
    TitleText = fontSetting["Title"]


class ImageSetting():
    background = imageSetting["background"]
    texture = imageSetting["texture"]
    title = imageSetting["title"]
