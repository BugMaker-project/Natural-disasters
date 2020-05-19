from script.items import *


def create_world(save):
    create_land(save)

def save_land(save):
    land = []
    block = create_land()

def create_land():
    block = Grass_land(0,0,canvas)
    return block