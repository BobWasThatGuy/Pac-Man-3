import math
import tkinter as tk
from tkinter import *
from Game_Code import *
from While import *
from While import While_


def Map(Game_Object):

    #def breaker():
    #   Game_Object, Map_Object = While_(Game_Object, Map_Object)


    

    class Map_Class():
        def __init__(self):
            self.Map_Array = [[1,0,0,1, 0], [1,0,1,0, 0], [1,0,0,0, 0], [1,0,0,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [1,0,0,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [1,0,0,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [1,1,0,0, 0],
                              [0,1,0,1, 0], [1,1,0,1, 1], [0,0,1,1, 0], [0,1,0,0, 0], [1,0,0,1, 1], [1,0,1,0, 1], [1,1,0,0, 1], [0,1,0,1, 0], [1,0,0,1, 1], [1,1,0,0, 1], [0,1,0,1, 0], [1,0,1,1, 1], [1,1,0,0, 1], [0,1,0,1, 0],
                              [0,1,0,1, 0], [0,0,0,1, 1], [1,1,1,0, 1], [0,1,0,1, 0], [0,1,0,1, 1], [1,1,0,1, 0], [0,1,1,1, 1], [0,1,0,1, 0], [0,0,0,1, 1], [0,1,0,0, 1], [0,0,1,1, 0], [1,1,0,0, 0], [0,1,0,1, 1], [0,1,0,1, 0],
                              [0,1,0,1, 0], [0,1,0,1, 1], [1,0,1,1, 0], [0,1,0,0, 0], [0,1,0,1, 1], [0,0,1,1, 0], [1,0,1,0, 0], [0,1,1,0, 0], [0,0,0,1, 1], [0,0,1,0, 1], [1,1,1,0, 1], [0,1,0,1, 0], [0,1,1,1, 1], [0,1,0,1, 0],
                              [0,1,0,1, 0], [0,0,1,1, 1], [1,1,1,0, 1], [0,1,0,1, 0], [0,0,1,1, 1], [1,0,0,0, 1], [1,0,1,0, 1], [1,0,1,0, 1], [0,1,1,0, 1], [1,0,0,1, 0], [1,0,1,0, 0], [0,0,1,0, 0], [1,0,1,0, 0], [0,1,0,0, 0],
                              [0,0,0,1, 0], [1,0,1,0, 0], [1,0,1,0, 0], [0,0,1,0, 0], [1,1,0,0, 0], [0,1,1,1, 1], [1,0,0,1, 0], [1,0,1,0, 0], [1,0,1,0, 0], [0,1,0,0, 0], [1,0,0,1, 1], [1,0,0,0, 1], [1,1,0,0, 1], [0,1,0,1, 0],
                              [0,1,0,1, 0], [1,0,1,1, 1], [1,0,1,0, 1], [1,1,0,0, 1], [0,0,0,1, 0], [1,0,1,0, 0], [0,1,0,0, 0], [1,0,0,1, 1], [1,1,0,0, 1], [0,1,0,1, 0], [0,0,1,1, 1], [0,0,1,0, 1], [0,1,1,0, 1], [0,1,0,1, 0],
                              [0,0,0,1, 0], [1,0,1,0, 0], [1,1,0,0, 0], [0,1,0,1, 1], [0,1,0,1, 0], [1,1,0,1, 1], [0,1,0,1, 0], [0,0,0,0, 1], [0,1,0,0, 1], [0,0,0,1, 0], [1,0,1,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [0,1,0,0, 0],
                              [0,1,0,1, 0], [1,1,1,0, 1], [0,1,0,1, 0], [0,1,1,1, 1], [0,1,0,1, 0], [0,1,1,1, 1], [0,1,0,1, 0], [0,0,1,1, 1], [0,1,1,0, 1], [0,1,0,1, 0], [1,0,1,1, 1], [1,0,1,0, 1], [1,1,1,0, 1], [0,1,0,1, 0],
                              [0,0,1,1, 0], [1,0,1,0, 0], [0,0,1,0, 0], [1,0,1,0, 0], [0,0,1,0, 0], [1,0,1,0, 0], [0,0,1,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [0,0,1,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [1,0,1,0, 0], [0,1,1,0, 0]]
            
            self.Map_Array_Coords = []

            Pellet_Img = tk.PhotoImage(file = "Pellet.png")
            Pellets = []

            for i in range(0,10):
                for j in range(0,14):
                    self.Map_Array_Coords.append([j * 106 + 73, i * 106 + 73])
                    #print("1")
                    
                    if self.Map_Array[(i * 14) + (j)][4] == 0:
                        #print("2")
                        #Pellet = Game_Object.game_canvas.create_image(j * 106 + 73, i * 106 + 73, image = Pellet_Img, anchor = CENTER)
                        #Pellets.append(Pellet)
                        
                        Game_Object.root.update()
            



                


            print(self.Map_Array_Coords)


            for i in range(0, len(self.Map_Array)):
                if self.Map_Array[i][0] == 1:
                    self.Vertical_Column = ((i + 1) // 14.00000001) 
                    if i % 14 != 0:
                        self.Horizontal_Row = math.ceil((i) % 14.00000001)
                    else:
                        self.Horizontal_Row = 0
                    Game_Object.game_canvas.create_line(((self.Horizontal_Row) * 106 + 10), (self.Vertical_Column * 106 + 10), ((self.Horizontal_Row + 1) * 106 + 10), ((self.Vertical_Column) * 106 + 10), width = 5, fill = "blue")

                if self.Map_Array[i][1] == 1:
                    self.Vertical_Column = ((i + 1 ) // 14.00000001) 
                    self.Horizontal_Row = math.ceil((i + 1) % 14.00000001)
                    Game_Object.game_canvas.create_line((self.Horizontal_Row * 106 + 10), ((self.Vertical_Column ) * 106 + 10), ((self.Horizontal_Row ) * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), width = 5, fill = "blue")

                if self.Map_Array[i][2] == 1:
                    self.Vertical_Column = ((i + 1) // 14.00000001) 
                    if i % 14 != 0:
                        self.Horizontal_Row = math.ceil((i) % 14.00000001)
                    else:
                        self.Horizontal_Row = 0
                    Game_Object.game_canvas.create_line((self.Horizontal_Row * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), ((self.Horizontal_Row + 1) * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), width = 5, fill = "blue")

                if self.Map_Array[i][3] == 1:
                    self.Vertical_Column = ((i + 1) // 14.00000001) 
                    self.Horizontal_Row = math.ceil((i + 1) % 14.00000001) - 1
                    Game_Object.game_canvas.create_line((self.Horizontal_Row * 106 + 10), ((self.Vertical_Column ) * 106 + 10), ((self.Horizontal_Row ) * 106 + 10), ((self.Vertical_Column + 1) * 106 + 10), width = 5, fill = "blue")



            #self.Map_Outline_West = Game_Object.game_canvas.create_line(20, 20, 20, 1060, width = 5, fill = "navy")
            #self.Map_Outline_North = Game_Object.game_canvas.create_line(20, 20, 1483, 20, width = 5, fill = "navy")
            #self.Map_Outline_East = Game_Object.game_canvas.create_line(1483, 20, 1483, 1060, width = 5, fill = "navy")
            #self.Map_Outline_South = Game_Object.game_canvas.create_line(20, 1060, 1483, 1060, width = 5, fill = "navy")

            self.Scoreboard_Outline_North = Game_Object.game_canvas.create_line(1586, 20, 1900, 20, width = 5, fill = "navy")
            self.Scoreboard_Outline_South = Game_Object.game_canvas.create_line(1586, 1060, 1900, 1060, width = 5, fill = "navy")
            self.Scoreboard_Outline_West = Game_Object.game_canvas.create_line(1586, 20, 1586, 1060, width = 5, fill = "navy")
            self.Scoreboard_Outline_East = Game_Object.game_canvas.create_line(1900, 20, 1900, 1060, width = 5, fill = "navy")

            self.Score_Outline_North = Game_Object.game_canvas.create_line(1606, 40, 1880, 40, width = 5, fill = "navy")
            self.Score_Outline_South = Game_Object.game_canvas.create_line(1606, 140, 1880, 140, width = 5, fill = "navy")
            self.Score_Outline_West = Game_Object.game_canvas.create_line(1606, 40, 1606, 140, width = 5, fill = "navy")
            self.Score_Outline_East = Game_Object.game_canvas.create_line(1880, 40, 1880, 140, width = 5, fill = "navy")

            # self.Temp_Canvas_Background = Game_Object.game_canvas.create_rectangle(640, 360, 1280, 720, fill = "black")
            # self.Temp_Canvas_Border_North = Game_Object.game_canvas.create_line(640, 360, 1280, 360, width = 5, fill = "navy")
            # self.Temp_Canvas_Border_South = Game_Object.game_canvas.create_line(640, 720, 1280, 720, width = 5, fill = "navy")
            # self.Temp_Canvas_Border_East = Game_Object.game_canvas.create_line(640, 360, 640, 720, width = 5, fill = "navy")
            # self.Temp_Canvas_Border_West = Game_Object.game_canvas.create_line(1280, 360, 1280, 720, width = 5, fill = "navy")

            # #self.temp_frame = Frame(Game_Object.game_canvas, width = 640, height = 360, bg = "black")
            # #self.temp_frame.pack()


            # self.Temp_Canvas_Button = tk.Button(Game_Object.game_canvas, anchor = CENTER, command = breaker, background = "black", activebackground = "navy")
            # self.Temp_Canvas_Button.place(x = 960, y = 420, height = 80, width = 600, anchor= CENTER)



            self.High_Score_Img = tk.PhotoImage(file = "High Score.png")
            self.High_Score_Image = Game_Object.game_canvas.create_image(1744, 70, image = self.High_Score_Img, anchor = CENTER)

            self.wasd_img = tk.PhotoImage(file = "WASD.png")
            self.wasd = Game_Object.game_canvas.create_image(1744, 940, image = self.wasd_img, anchor = CENTER)

            



            


            
    Map_Object = Map_Class()

    return Map_Object, Game_Object


    