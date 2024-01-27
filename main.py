import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fb
import buttons_and_boxes as bb

'''
This is a excel parser which can parse data from one or many excel files to one another

'''


class myParser:
    def __init__(self):
        ''''''
        '''
        Main window and frames
        '''
        self.__main_window = tkinter.Tk()                           # Creating main window
        self.__main_window.geometry('700x400')                      # Main window size

        '''
        Description frame
        '''

        self.__description_frame = tkinter.Frame(self.__main_window, relief='solid',
                                                 borderwidth=1)     # description frame

        text = 'This is a excel parser which can parse data from one or many excel files ' \
               'and extract them to one another.'                   # Description text

        self.__label = tkinter.Label(self.__description_frame,
                                     text=text, borderwidth=5)      # Description label
        self.__description_frame.pack(side='top', pady=20)          # Packing description FRAME
        self.__label.pack(pady=10)                                  # Packing description LABEL

        """
        Buttons and Boxes were put into other file, So they imported
        """

        self.__r_button_frame = tkinter.Frame(self.__main_window, relief='groove',
                                              borderwidth=1)  # Radio buttons frame
        self.many_file_button = bb.Buttons.radio_buttons(self.__r_button_frame, value=1,
                                                         text='Many files mode:')
        self.one_file_button = bb.Buttons.radio_buttons(self.__r_button_frame, value=2,
                                                        text='One file mode:')
        self.__r_button_frame.pack()  # Packing RB FRAME



        bb.Buttons.quit(self, self.__main_window)
        mainloop()




if __name__ == '__main__':
    myParser()