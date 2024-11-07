import tkinter as tk
from tkinter import *
import time
import random
import math
from Game_Code import *

def Clyde_Moves(Game_Object, Map_Object):

    Clyde_Moves = [[0, -3.3125], [3.3125, 0], [0, 3.3125], [-3.3125, 0]]
    Clyde_Last_Directions = [2, 3, 0, 1]
    Clyde_Variation = [0,2,2]
    
    if Game_Object.game_canvas.coords(Game_Object.Clyde) in Map_Object.Map_Array_Coords:

        Clyde_Cell_Number = Map_Object.Map_Array_Coords.index(Game_Object.game_canvas.coords(Game_Object.Clyde))
        Clyde_Variation_Use = random.choice(Clyde_Variation)

        if Map_Object.Map_Array[Clyde_Cell_Number][2] != 1 and Game_Object.Clyde_Last_Direction != 2:
            Game_Object.Clyde_New_Direction = 2
        
        else:
            if Game_Object.game_canvas.coords(Game_Object.pac_man)[0] <= Game_Object.game_canvas.coords(Game_Object.Clyde)[0]:
                if Map_Object.Map_Array[Clyde_Cell_Number][3] != 1 and Game_Object.Clyde_Last_Direction != 3:
                    Game_Object.Clyde_New_Direction = 3

                
                elif Map_Object.Map_Array[Clyde_Cell_Number][1] != 1 and Game_Object.Clyde_Last_Direction != 1:
                    Game_Object.Clyde_New_Direction = 1
                
                else:
                    Game_Object.Clyde_New_Direction = 0

            else:
                if Map_Object.Map_Array[Clyde_Cell_Number][1] != 1 and Game_Object.Clyde_Last_Direction != 1:
                    Game_Object.Clyde_New_Direction = 1
                
                elif Map_Object.Map_Array[Clyde_Cell_Number][3] != 1 and Game_Object.Clyde_Last_Direction != 3:
                    Game_Object.Clyde_New_Direction = 3
                
                else:
                    Game_Object.Clyde_New_Direction = 0

        #print(Game_Object.Clyde_Last_Direction)

        Game_Object.Clyde_Last_Direction = Clyde_Last_Directions[Game_Object.Clyde_New_Direction]

        #print(Game_Object.Clyde_New_Direction, Game_Object.Clyde_Last_Direction, Clyde_Cell_Number, Clyde_Variation_Use)


                
            

        
    
    Game_Object.game_canvas.move(Game_Object.Clyde, Clyde_Moves[Game_Object.Clyde_New_Direction][0], Clyde_Moves[Game_Object.Clyde_New_Direction][1])


    return Game_Object, Map_Object