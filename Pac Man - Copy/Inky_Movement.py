import time
import random
from tkinter import *
import tkinter as tk
from Game_Code import *
import math
import copy

def Inky_Movement(Game_Object, Map_Object):
    Moves = [[0, -3.3125], [3.3125, 0], [0, 3.3125], [-3.3125, 0]]
    Changes = [-28, 2, 28, -2] 
    Angles = [0, 270, 180, 90, 360]

    Last_Directions = [2, 3, 0, 1]

    
    Pac_Man_Coords = Game_Object.game_canvas.coords(Game_Object.pac_man)

    Pac_Man_Cell = []
    Pac_Man_Cell.append(Pac_Man_Coords[0] - 20)
    Pac_Man_Cell.append(Pac_Man_Coords[1] - 20)
    Pac_Man_Cell[0] //= 106
    Pac_Man_Cell[1] //= 106
    Pac_Man_Cell = Pac_Man_Cell[1] * 14 + Pac_Man_Cell[0]

    Inky_Coords = Game_Object.game_canvas.coords(Game_Object.Inky)
    Inky_Cell = []
    Inky_Cell.append(Inky_Coords[0] - 20)
    Inky_Cell.append(Inky_Coords[1] - 20)
    Inky_Cell[0] //= 106
    Inky_Cell[1] //= 106
    Inky_Cell = Inky_Cell[1] * 14 + Inky_Cell[0]

    if Inky_Coords in Map_Object.Map_Array_Coords:
        Change = Changes[Game_Object.Pac_Man_Direction]
        Game_Object.Inky_Cell_Target = Pac_Man_Cell + Change
        Game_Object.Inky_Target = [(Game_Object.Inky_Cell_Target % 14) * 106 + 73, (Game_Object.Inky_Cell_Target // 14) * 106 + 73]

        Gradient = ((Inky_Coords[1] - Game_Object.Inky_Target[1]) / (Inky_Coords[0] - Game_Object.Inky_Target[0] + 1) )
        Angle = 90 - math.degrees(math.atan(Gradient)) 
        
        if (Inky_Coords[0] - Pac_Man_Coords[0] + 1) < 0:
            #
            Angle += 180
            pass

        #print(Angle, Gradient)
        Inky_Cell = int(Inky_Cell)
       

        
        Game_Object.Saved_Index = 0

        for j in range(0, 4):
            Lower = 36100

            for i in range(0,5):
                Angles[i] = Angles[i] - Angle
                Angles[i] **= 2
                Angles[i] = math.sqrt(Angles[i])

                #print("Temp Angle",Angles[i])

                if Angles[i] < Lower:
                    Lower = Angles[i]
                    Game_Object.Saved_Index = i

                #print("Lower then Saved Index", Lower, Game_Object.Saved_Index)

            if Game_Object.Saved_Index == 4:
                Game_Object.Saved_Index = 0


            Inky_Cell = int(Inky_Cell)

            if Map_Object.Map_Array[Inky_Cell][Game_Object.Saved_Index] == 1 or Game_Object.Inky_Last_Direction == Game_Object.Saved_Index:
                Angles[Game_Object.Saved_Index] += 1000
                if Game_Object.Saved_Index == 0:
                    Angles[4] += 1000

            else:
                Game_Object.Inky_Last_Direction = Last_Directions[Game_Object.Saved_Index]
                break

        Temp2 = 0
        for i in range(0, 5):
            if Angles[i] > 999:
                Temp2 += 1
        if Map_Object.Map_Array[Inky_Cell][Game_Object.Saved_Index] == 1:
            pass


        if Temp2 == 5 or Map_Object.Map_Array[Inky_Cell][Game_Object.Saved_Index] == 1:
            #print("HERE")
            #print("HERE")

            #print("Saved Index", Game_Object.Saved_Index, "Last Direction", Game_Object.Inky_Last_Direction)

            #Game_Object.Saved_index = copy.deepcopy(Game_Object.Inky_Last_Direction)
            Game_Object.Saved_Index = Game_Object.Inky_Last_Direction
            #print("Saved Index", Game_Object.Saved_Index, "Last Direction", Game_Object.Inky_Last_Direction)
            Game_Object.Inky_Last_Direction = Last_Directions[Game_Object.Saved_Index]
            #print("Saved Index", Game_Object.Saved_Index, "Last Direction", Game_Object.Inky_Last_Direction)

            

            


            #print("ANGLES", Angles)

            #print("THIS", Game_Object.Saved_Index, Game_Object.Inky_Last_Direction)

        Inky_Cell = int(Inky_Cell)
        
        #print(Inky_Cell, Map_Object.Map_Array[Inky_Cell], Game_Object.Saved_Index, Game_Object.Inky_Last_Direction, Moves)




    Inky_Cell = int(Inky_Cell)
    #print("ALL", Inky_Cell, Map_Object.Map_Array[Inky_Cell], Game_Object.Inky_Last_Direction, Game_Object.Saved_Index)
    Game_Object.game_canvas.move(Game_Object.Inky, Moves[Game_Object.Saved_Index][0], Moves[Game_Object.Saved_Index][1])

    return Game_Object, Map_Object


   

    





