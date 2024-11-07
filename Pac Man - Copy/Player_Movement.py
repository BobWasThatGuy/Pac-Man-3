from tkinter import *
from Game_Code import *
import tkinter as tk
import math
import random
import keyboard

def Pac_Man_Movement(Game_Object, Map_Object):

    Pac_Man_Coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
    Pac_Man_Coords_Stripped = [((Pac_Man_Coords[0] - 20) // 106) * 106 + 73, ((Pac_Man_Coords[1] - 20) // 106) * 106 + 73]
    Pac_Man_Cell = Map_Object.Map_Array_Coords.index(Pac_Man_Coords_Stripped)
    Pac_Man_Coords[0] -= 20
    Pac_Man_Coords[1] -= 20

    Pac_Man_Moves = [[0, -3.3125], [3.3125, 0], [0, 3.3125], [-3.3125, 0]]
    

    if keyboard.is_pressed("w") and Map_Object.Map_Array[Pac_Man_Cell][0] == 0:
        if (Pac_Man_Coords[0] ) % 106 > 44 and (Pac_Man_Coords[0] ) % 106 < 62:

            Game_Object.Pac_Man_Direction = 0

    if keyboard.is_pressed("d") and Map_Object.Map_Array[Pac_Man_Cell][1] == 0:
        if (Pac_Man_Coords[1] ) % 106 > 44 and (Pac_Man_Coords[1] ) % 106 < 62:

            Game_Object.Pac_Man_Direction = 1

    if keyboard.is_pressed("s") and Map_Object.Map_Array[Pac_Man_Cell][2] == 0:
        if (Pac_Man_Coords[0] ) % 106 > 44 and (Pac_Man_Coords[0] ) % 106 < 62:

            Game_Object.Pac_Man_Direction = 2

    if keyboard.is_pressed("a") and Map_Object.Map_Array[Pac_Man_Cell][3] == 0:
        if (Pac_Man_Coords[1] ) % 106 > 44 and (Pac_Man_Coords[1] ) % 106 < 62:

            Game_Object.Pac_Man_Direction = 3


    if Game_Object.Pac_Man_Direction == 1 or Game_Object.Pac_Man_Direction == 3:
        if Pac_Man_Coords[0] % 106 < 48 or  Pac_Man_Coords[0] % 106 > 58 or Map_Object.Map_Array[Pac_Man_Cell][Game_Object.Pac_Man_Direction] != 1 :
        

            Game_Object.game_canvas.move(Game_Object.pac_man, Pac_Man_Moves[Game_Object.Pac_Man_Direction][0], Pac_Man_Moves[Game_Object.Pac_Man_Direction][1])

    else:
        if  Pac_Man_Coords[1] % 106 < 48 or  Pac_Man_Coords[1] % 106 > 58 or Map_Object.Map_Array[Pac_Man_Cell][Game_Object.Pac_Man_Direction] != 1 :
        

            Game_Object.game_canvas.move(Game_Object.pac_man, Pac_Man_Moves[Game_Object.Pac_Man_Direction][0], Pac_Man_Moves[Game_Object.Pac_Man_Direction][1])  

    #print(Pac_Man_Coords)

    return Game_Object, Map_Object


        