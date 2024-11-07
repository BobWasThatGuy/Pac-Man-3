from Map_Code import *
import time
import keyboard
from tkinter import *
import tkinter as tk
import random
import math
from Player_Movement import *
from Red_Movement import *
from Clyde_Movement import *
from Inky_Movement import *
from Pinky_Movement import *
from While import *

def Game(Game_Object):



        #1760 940
        # 4 5 6
        # 3 2 1

        last_coords = 1 
        e = [0, 1]

        a = [[[0, -4, 6], [-4, 0, 2], 1],
              [[4, 0, 1], [0, -4, 5], [-4, 0, 3], 2],
              [[0, -4, 4], [4, 0, 2], 3],
              [[4, 0, 5], [0, 4, 3], 4],
              [[4, 0, 6], [0, 4, 2], [-4, 0, 4], 5],
              [[0, 4, 1], [-4, 0, 5], 6]]
        
        b = [[1760, 940], [960, 940], [160, 940], [160, 140], [960, 140], [1760, 140]]


        

        Game_Object.start_canvas.destroy()
        Game_Object.game_canvas.pack(fill = "both", expand = True)
        
        Map_Object, Game_Object = Map(Game_Object)

        Game_Object.root.update()

        tick = -2

        Pellet_Img = tk.PhotoImage(file = "Pellet.png")
        Big_Pellet_Img = tk.PhotoImage(file = "Big.png")
        Game_Object.Pellets = []

        for i in range(0,10):
            for j in range(0,14):
                #Map_Object.Map_Array_Coords.append([j * 106 + 73, i * 106 + 73])
                #print("1")
                    
                if Map_Object.Map_Array[(i * 14) + (j)][4] == 0:
                    #print("2")

                    Temp3 = random.randint(0,20)
                    if Temp3 == 1:
                        Pellet = Game_Object.game_canvas.create_image(j * 106 + 73, i * 106 + 73, image = Big_Pellet_Img, anchor = CENTER)
                         
                    else:
                        Pellet = Game_Object.game_canvas.create_image(j * 106 + 73, i * 106 + 73, image = Pellet_Img, anchor = CENTER)
                    Game_Object.Pellets.append(Pellet)
                        
                    Game_Object.root.update()

        Game_Object.red = Game_Object.game_canvas.create_image(73, 73, image = Game_Object.red_img, anchor = CENTER)
        Game_Object.pac_man = Game_Object.game_canvas.create_image(73, 603, image = Game_Object.pac_img, anchor = CENTER) 
        Game_Object.Clyde = Game_Object.game_canvas.create_image(179, 73, image = Game_Object.clyde_img, anchor = CENTER)   
        Game_Object.Inky = Game_Object.game_canvas.create_image(285, 73, image = Game_Object.Inky_Img, anchor = CENTER)
        Game_Object.Pinky = Game_Object.game_canvas.create_image(391, 73, image = Game_Object.Pinky_Img, anchor = CENTER)



        temp1 = time.time()




        
        

        while True:



            # Game_Object.game_canvas.move(Map_Object.Temp_Canvas_Border_North, 2000, 0)
            # Game_Object.game_canvas.move(Map_Object.Temp_Canvas_Border_East, 2000, 0)
            # Game_Object.game_canvas.move(Map_Object.Temp_Canvas_Border_West, 2000, 0)
            # Game_Object.game_canvas.move(Map_Object.Temp_Canvas_Border_South, 2000, 0)
            # Game_Object.game_canvas.move(Map_Object.Temp_Canvas_Background, 2000, 0)
            # Map_Object.Temp_Canvas_Button.destroy()

            Game_Object.root.update()
            
            temp2 = time.time()
            if temp2 - temp1 > 0.02:
                #print(Game_Object.game_canvas.coords(Game_Object.pac_man))
                #print(tick)
                Game_Object.root.update()
                tick = tick + 1

                temp1 = time.time()

                
                Game_Object, Map_Object = Pac_Man_Movement(Game_Object, Map_Object)

                #print(3)
                

                #if tick % 200 == 0:
                    #coords = Game_Object.game_canvas.coords(Game_Object.red)
                    #no_list = b.index(coords)
                    #length = len(a[no_list])
                    #d = random.randint(0, length - 2)
                    #while True:
                        #print(no_list, d, length)
                        #if a[no_list][d][2] == last_coords:
                            #d = random.randint(0, length - 2)
#                            
                        #else:
#                            
                            #e = a[no_list][d]
                            #break
#                    
                    #last_coords = no_list + 1
#
                #Game_Object.game_canvas.move(Game_Object.red , e[0], e[1])
                if tick % 500 == 0:
                    Game_Object.red_mode = random.choice(e)
                    print(Game_Object.red_mode)
                if Game_Object.red_mode == 0:
                    Game_Object, Map_Object = Red_Random(Game_Object, Map_Object)
                else:
                    Game_Object, Map_Object = Red_Hunt(Game_Object, Map_Object)

                Game_Object, Map_Object = Clyde_Moves(Game_Object, Map_Object)

                Game_Object, Map_Object = Inky_Movement(Game_Object, Map_Object)

                Game_Object, Map_Object = Pinky_Movement(Game_Object, Map_Object)


                Game_Object.root.update()

                

                
                        



                total_diff = 0

                ghosts = [Game_Object.red, Game_Object.Clyde]

                for i in range(0,2):
                    total_diff = 0
                    for j in range(0,2):

                        p = Game_Object.game_canvas.coords(Game_Object.pac_man)
                        q = Game_Object.game_canvas.coords(ghosts[i])
                        diff = p[j] - q[j]
                        diff = diff * diff
                        diff = math.sqrt(diff)
                        total_diff += diff
                
                    if total_diff <= 170:
                        #Game_Object.game_canvas.destroy()
                        #Game_Object.start_canvas.pack(fill = "both", expand = True)
                        pass
                
                Delete_List = []

                for i in range(0, len(Game_Object.Pellets)):
                    total_diff = 0
                    for j in range(0,2):
                        p = Game_Object.game_canvas.coords(Game_Object.pac_man)
                        q = Game_Object.game_canvas.coords(Game_Object.Pellets[i])
                        diff = p[j] - q[j]
                        diff = diff * diff
                        diff = math.sqrt(diff)
                        total_diff += diff

                    if total_diff <= 20:
                        #print("HIIIi")
                        Game_Object.game_canvas.move(Game_Object.Pellets[i], 10000, 10000)
                        Delete_List.append(i)

                        Game_Object.Score += 1

                for i in range(0, len(Delete_List)):
                    del Game_Object.Pellets[Delete_List[i]]
                    
                    

                #if tick % 2 == 0:
                    #Game_Object.pac_img = tk.PhotoImage(file = "pac man2.gif")
                    #temp_coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
                    #Game_Object.pac_man.delete()
                    #Game_Object.pac_man = Game_Object.game_canvas.create_image(temp_coords[0], temp_coords[1], image = Game_Object.pac_img)
                #elif tick % 2 == 1:
                    #Game_Object.pac_img = tk.PhotoImage(file = "pac man.gif")
                    #temp_coords = Game_Object.game_canvas.coords(Game_Object.pac_man)
                    #Game_Object.pac_man.delete()
                    #Game_Object.pac_man = Game_Object.game_canvas.create_image(temp_coords[0], temp_coords[1], image = Game_Object.pac_img)

            else:
                Time_Diff = temp2 - temp1
                time.sleep(Time_Diff)

            