import tkinter as tk
from tkinter import *
import time
import math
from Game_Code import *
import random


def Red_Random(Game_Object, Map_Object):
    Red_Moves = [[0, -3.3125], [3.3125, 0], [0, 3.3125], [-3.3125, 0]]
    Last_Direction_List = [2, 3, 0, 1]

    if Game_Object.game_canvas.coords(Game_Object.red) in Map_Object.Map_Array_Coords:
        

        Red_Cell = Map_Object.Map_Array[Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.red))]
        Temp_List = []
        #print("Check 1", Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.red)))

        for i in range(0,4):
            if Red_Cell[i] == 0:
                Temp_List.append(i)
                #print("Check 2", Temp_List)
        
        New_Direction = random.choice(Temp_List)
        Looper = 0

        while New_Direction == Game_Object.last_direction:
            New_Direction = random.choice(Temp_List)
            Looper += 1
            #print("Loop", Looper)
            if Looper == 5:
                Looper = 0
                break

        Game_Object.Red_Movement = Red_Moves[New_Direction]
        Game_Object.last_direction = Last_Direction_List[New_Direction]
        #print("Check 3", Game_Object.Red_Movement, Game_Object.last_direction)

    Game_Object.game_canvas.move(Game_Object.red, Game_Object.Red_Movement[0], Game_Object.Red_Movement[1])

    return Game_Object, Map_Object


def Red_Hunta(Game_Object, Map_Object):

    if Game_Object.game_canvas.coords(Game_Object.red) in Map_Object.Map_Array_Coords:
        Pac_Coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
        Red_Cell = Map_Object.Map_Array[Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.red))]

        Temps = [[Red_Cell, 0]]
        Temp_List = [[]]
        while True:
            
            for j in range(0, len(Temps)):
                for i in range(0,4):
                    if Temps[j][0][i] == 0 and Temps[j][0][i] != Temps[j][1]:
                        Temp_List[j].append(i)
                        #print("Check 2", Temp_List)

            for i in range(0, len(Temps)):
                for j in range(0, len(Temp_List[i])):
                    k = len(Temps)


def Red_Hunt(Game_Object, Map_Object):
    Red_Moves = [[0, -3.3125], [3.3125, 0], [0, 3.3125], [-3.3125, 0]]
    Last_Direction_List = [2, 3, 0, 1]
    Direction_List = [0, 270, 180, 90, 360]

    if Game_Object.game_canvas.coords(Game_Object.red) in Map_Object.Map_Array_Coords:
        Pac_Coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
        Red_Cell = Map_Object.Map_Array[Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.red))]
        Red_Cell_Number = Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.red))

        Temper = []
        Temper.append((Game_Object.game_canvas.coords(Game_Object.red))[0] - Pac_Coords[0])
        Temper.append((Game_Object.game_canvas.coords(Game_Object.red))[1] - Pac_Coords[1])

        Angle = Temper[1] / (Temper[0] + 1)
        Angle = 90 - math.degrees(math.atan(Angle))
        if Temper[0] < 0:
            Angle += 180

        Angle_List = []

        for i in range(0,4):
            Temp_Angle = Direction_List[i] - Angle
            Temp_Angle **= 2
            Temp_Angle = math.sqrt(Temp_Angle)
            Angle_List.append(Temp_Angle)

        l = 360

        for i in range(0,4):
            if Angle_List[i] < l:
                l = Angle_List[i]

        New_Direction = Angle_List.index(l)



        #print("2 Check 1", Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.red)))

        Temp_List = []

        Looper = 0

        while New_Direction == Game_Object.last_direction or Map_Object.Map_Array[Red_Cell_Number][New_Direction] == 1:
            Angle_List[New_Direction] = 361
            l = 360


            for i in range(0,4):
                if Angle_List[i] < l:
                    l = Angle_List[i]
            
            if l == 360:
                New_Direction = Game_Object.last_direction

            else:

                New_Direction = Angle_List.index(l)
            Looper += 1
            #print("2 Loop", Looper)
            if Looper == 5:
                Looper = 0

                break

        Game_Object.Red_Movement = Red_Moves[New_Direction]
        Game_Object.last_direction = Last_Direction_List[New_Direction]
        #print("2 Check 3", Game_Object.Red_Movement, Game_Object.last_direction)

    Game_Object.game_canvas.move(Game_Object.red, Game_Object.Red_Movement[0], Game_Object.Red_Movement[1])

    return Game_Object, Map_Object



            

            
            

        
        
