import tkinter as tk
from tkinter import *
import math
import random
from Game_Code import *

def Pinky_Movement(Game_Object, Map_Object):

    Moves = [[0, -3.3125], [3.3125, 0], [0, 3.3125], [-3.3125, 0]]
    Last_Directions = [2, 3, 0, 1]
    Angle_List = [0, 270, 180, 90, 360]

    Pinky_Coords = Game_Object.game_canvas.coords(Game_Object.Pinky)

    Pinky_Cell = []
    Pinky_Cell.append(Pinky_Coords[0] - 20)
    Pinky_Cell.append(Pinky_Coords[1] - 20)
    Pinky_Cell[0] = (Pinky_Cell[0] // 106) * 106 + 73
    Pinky_Cell[1] = (Pinky_Cell[1] // 106) * 106 + 73
    Pinky_Cell = Map_Object.Map_Array_Coords.index([Pinky_Cell[0], Pinky_Cell[1]])

    Pac_Coords = Game_Object.game_canvas.coords(Game_Object.pac_man)

    Pac_Cell = []
    Pac_Cell.append(Pac_Coords[0] - 20)
    Pac_Cell.append(Pac_Coords[1] - 20)
    Pac_Cell[0] = (Pac_Cell[0] // 106) * 106 + 73
    Pac_Cell[1] = (Pac_Cell[1] // 106) * 106 + 73
    Pac_Cell = Map_Object.Map_Array_Coords.index([Pac_Cell[0], Pac_Cell[1]])
    

    if Pinky_Coords in Map_Object.Map_Array_Coords:
        Angle = (Pinky_Coords[1] - Pac_Coords[1]) / (Pinky_Coords[0] - Pac_Coords[0] + 1)
        Angle = 90 - math.degrees(math.atan(Angle))

        if Pinky_Coords[0] - Pac_Coords[0] + 1 < 0:
            Angle += 180

        Game_Object.Pinky_Direction = 2

        for i in range(0, 4):
            L = 20000

            for j in range(0, 5):
                Angle_List[j] = Angle_List[j] - Angle
                Angle_List[j] **= 2
                Angle_List[j] = math.sqrt(Angle_List[j])

                if Angle_List[j] < L:
                    L = Angle_List[j]
                    Game_Object.Pinky_Direction = j

            if Game_Object.Pinky_Direction == 4:
                Game_Object.Pinky_Direction = 0

                    
                        

            if Map_Object.Map_Array[Pinky_Cell][Game_Object.Pinky_Direction] == 1 or Game_Object.Pinky_Direction == Game_Object.Pinky_Last_Direction:
                Angle_List[Game_Object.Pinky_Direction] += 10000

                if Game_Object.Pinky_Direction == 0:
                    Angle_List[4] += 10000

            else:
                Game_Object.Pinky_Last_Direction = Last_Directions[Game_Object.Pinky_Direction]
                break

        Temp2 = 0
        for i in range(0, 5):
            if Angle_List[i] > 999:
                Temp2 += 1
        if Map_Object.Map_Array[Pinky_Cell][Game_Object.Pinky_Direction] == 1:
            pass

        print(Map_Object.Map_Array[Pinky_Cell][Game_Object.Pinky_Direction], Pinky_Cell, Game_Object.Pinky_Direction, Game_Object.Pinky_Last_Direction)
        if Temp2 == 5 or Map_Object.Map_Array[Pinky_Cell][Game_Object.Pinky_Direction] == 1:

            Game_Object.Pinky_Direction = Game_Object.Pinky_Last_Direction

            Game_Object.Pinky_Last_Direction = Last_Directions[Game_Object.Pinky_Direction]


        

        if Map_Object.Map_Array[Pinky_Cell][Game_Object.Pinky_Direction] == 1:

            Game_Object.Pinky_Direction = Game_Object.Pinky_Last_Direction

            Game_Object.Pinky_Last_Direction = Last_Directions[Game_Object.Pinky_Direction]
        
        
    Game_Object.game_canvas.move(Game_Object.Pinky, Moves[Game_Object.Pinky_Direction][0], Moves[Game_Object.Pinky_Direction][1])

    return Game_Object, Map_Object

            

           

            


        
        
