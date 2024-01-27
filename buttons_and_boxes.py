import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd


class Buttons:
    def __init__(self):
        """ Radio buttons and file dialog boxes
         There will be two buttons to choose one file mode or many file mode
         Also there will be boxes to enter path of files or directories
        """

        self.__int_var = None
        self.radio_but = None
        self.__radio_but = None
        self.__quit_button = None

        self.__int_var = tkinter.IntVar()  # Creating int var
        self.__int_var.set(0)  # Set int var default value
        


    def radio_buttons(self, value, text):
        

        
        
        self.radio_but = tkinter.Radiobutton(self, variable=self.__int_var, value=value,
                                             text=text)  # Radio button *


        self.radio_but.pack()  # Packing 1st RB

    def quit(self, operating):
        """
        QUIT Button
        """

        self.__quit_button = tkinter.Button(operating, text='Quit',
                                            command=operating.destroy)  # Quit button
        self.__quit_button.pack(side='bottom', pady=5)  # Packing Quit button


class Boxes:
    def __init__(self):
        pass
