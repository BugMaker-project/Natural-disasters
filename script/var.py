#定义ScriptVar类储存常用变量
class ScriptVars(object):
    def __str__(self):
        return "This class just a Father class for Var"
class PATHS(ScriptVars):
    KeysPaths="Data//Keys.xls"
    KeyWrite="Data//Keys.Key"
    CodesPaths="Data//Devlop_Codes.xls"
    land_sprite="image/land_sprite.png"
    backStart="image//HOME_Background.png"
    def __str__(self):
        return "PATHS(CLASS)"
class Controls(ScriptVars):
    ReturnsInXlsx=None
