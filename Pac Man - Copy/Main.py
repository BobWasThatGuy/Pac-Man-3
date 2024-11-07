
from Game_Code import Game
from tkinter import * 
import tkinter as tk
from Classes import *


def main():

    
    def key_handler(event):
        if event.keycode == 27:
            print(Game_Object.Score)
            Game_Object.root.destroy()
            exit()     




    def begin():
        Game(Game_Object)   

    def quitter():
        Game_Object.root.destroy()
        exit()

    def settings():
        Game_Object.start_canvas.destroy()
        Game_Object.settings_canvas.pack(fill = "both", expand = True)

    class Game_Class():
        #private Saved_Index

        def __init__(self):

            self.root = tk.Tk()
            self.root.title("Pac Man")
            self.root.attributes("-fullscreen", True)
            self.root.minsize(1920, 1080)
            self.root.maxsize(1920, 1080)
            self.root.configure(bg = "white")

            self.game_canvas = Canvas(self.root)
            self.game_canvas.configure(bg = "black", width = 1920, height = 1080, highlightbackground = "black")

            self.settings_canvas = Canvas(self.root)
            self.settings_canvas.configure(bg = "grey", width = 1920, height = 1080)


            self.start_canvas = tk.Canvas(self.root)
            self.start_canvas.configure(bg = "black", width = 1920, height = 1080)
            self.start_canvas.pack(fill = "both", expand = True)

            self.Temp_Canvas = tk.Canvas(self.root)
            self.Temp_Canvas.configure(bg = "black", width = 640, height = 360)
            

            self.start_frame = Frame(self.start_canvas, width = 1920, height = 1080, bg = "black")
            self.start_frame.pack()

            self.start_button = Button(self.start_frame, anchor = CENTER, text = "START", command = begin )
            self.start_button.place(x = 960, y = 500, height = 80, width = 320, anchor = CENTER)

            self.quit_button = Button(self.start_frame, anchor = CENTER, text = "QUIT", command = quitter)
            self.quit_button.place(x = 960, y = 700, height = 40, width = 240, anchor = CENTER)

            self.settings_button = Button(self.start_frame, anchor = CENTER, text = "SETTINGS", command = settings)
            self.settings_button.place(x = 960, y = 640, height = 40, width = 240, anchor = CENTER)

            self.red_img = tk.PhotoImage(file = "Red.png")
            self.red = 0

            self.pac_img = tk.PhotoImage(file = "Pac Man2.gif")
            self.pac_man = 0

            self.clyde_img = tk.PhotoImage(file = "Orag.png")
            self.Clyde = 0

            self.Inky_Img = tk.PhotoImage(file = "Aqua.png")
            self.Inky = 0

            self.Pinky_Img = tk.PhotoImage(file = "Pink.png")
            self.Pinky = 0

            self.root.bind("<Key>", key_handler)

            self.change_x = 0
            self.change_y = 0
            self.direction = 1
            self.stretch = 0
            self.axis = 0
            self.side = 0

            self.red_mode = 0
            self.last_direction = 3
            self.Red_Movement = [3.3125, 0]
            self.Red_Saved_Index = 1

            self.Clyde_Last_Direction = 2
            self.Clyde_New_Direction = 2

            self.Score = 0

            self.Pac_Man_Direction = 0

            self.Inky_Last_Direction = 0
            self.Inky_Cell_Target = 0
            self.Inky_Target = [1, 1]
            self.Saved_Index = 1

            self.Pinky_Direction = 1
            self.Pinky_Last_Direction = 3

            self.Controller = False
            self.Pellets = []

        #def setSavedIndex(self, newIndex):
            #self.Saved_Index = newIndex

        #@property
        #def Saved_Index(self):
            #return self._Saved_Index
        
        #@Saved_Index.setter
        #def Saved_Index(self, value):
            #self._Saved_Index = value

        #@property
        #def Inky_Last_Direction(self):
            #return self._Inky_Last_Direction
        
        #@Inky_Last_Direction.setter
        #def Inky_Last_Direction(self, value):
            #self._Inky_Last_Direction = value
    
    Game_Object = Game_Class()



    Game_Object.root.mainloop()


main()