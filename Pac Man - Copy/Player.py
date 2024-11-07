import time
import tkinter as tk
from tkinter import *
import keyboard

def Movement_Player(Game_Object, Map_Object):

    pac_cell_x = int((Game_Object.game_canvas.coords(Game_Object.pac_man)[0] - 20) // 106)
    pac_cell_y = int((Game_Object.game_canvas.coords(Game_Object.pac_man)[1] - 20) // 106)
    pac_cell = (pac_cell_y * 14 ) + pac_cell_x
    #print("pac cell",pac_cell,"pac x",pac_cell_x,"pac y", pac_cell_y)

    if Game_Object.side == 0:
        if Map_Object.Map_Array[pac_cell][Game_Object.direction] != 1 or ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) > 52:
            Game_Object.game_canvas.move(Game_Object.pac_man, Game_Object.change_x, Game_Object.change_y)
            #print(Map_Object.Map_Array[pac_cell][Game_Object.direction], Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis])
    else:
        if Map_Object.Map_Array[pac_cell][Game_Object.direction] != 1 or ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) < 54:
            Game_Object.game_canvas.move(Game_Object.pac_man, Game_Object.change_x, Game_Object.change_y)

    if keyboard.is_pressed("w"):
        if Game_Object.side == 0:
            if Map_Object.Map_Array[pac_cell][0] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) > 51:
                Game_Object.change_x = 0
                Game_Object.change_y = -4
                Game_Object.side = 0
                Game_Object.axis = 1
                Game_Object.direction = 0
        else:
            if Map_Object.Map_Array[pac_cell][0] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) < 55:
                Game_Object.change_x = 0
                Game_Object.change_y = -4
                Game_Object.side = 0
                Game_Object.axis = 1
                Game_Object.direction = 0
                
    if keyboard.is_pressed("a"):
        if Game_Object.side == 0:
            if Map_Object.Map_Array[pac_cell][3] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) > 51:
                Game_Object.change_x = -4
                Game_Object.change_y = 0
                Game_Object.side = 0
                Game_Object.axis = 0
                Game_Object.direction = 3
        else:
            if Map_Object.Map_Array[pac_cell][3] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) < 55:
                Game_Object.change_x = -4
                Game_Object.change_y = 0
                Game_Object.side = 0
                Game_Object.axis = 0
                Game_Object.direction = 3
                
    if keyboard.is_pressed("s"):
        if Game_Object.side == 0:
            if Map_Object.Map_Array[pac_cell][2] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) > 51:
                Game_Object.change_x = 0
                Game_Object.change_y = 4
                Game_Object.side = 1
                Game_Object.axis = 1
                Game_Object.direction = 2
        else:
            if Map_Object.Map_Array[pac_cell][2] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) < 55:
                Game_Object.change_x = 0
                Game_Object.change_y = 4
                Game_Object.side = 1
                Game_Object.axis = 1
                Game_Object.direction = 2

    if keyboard.is_pressed("d"):
        if Game_Object.side == 0:
            if Map_Object.Map_Array[pac_cell][1] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) > 51:
                Game_Object.change_x = 4
                Game_Object.change_y = 0
                Game_Object.side = 1
                Game_Object.axis = 0
                Game_Object.direction = 1
        else:
            if Map_Object.Map_Array[pac_cell][1] != 1 and ((Game_Object.game_canvas.coords(Game_Object.pac_man)[Game_Object.axis] - 20) % 106) > 55:
                Game_Object.change_x = 4
                Game_Object.change_y = 0
                Game_Object.side = 1
                Game_Object.axis = 0
                Game_Object.direction = 1

    Game_Object.root.update()