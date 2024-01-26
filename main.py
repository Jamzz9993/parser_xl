import tkinter
from tkinter import *
from tkinter import ttk
'''
This is a excel parser which can parse data from one or many excel files to one another

'''

class myParser:
    def __init__(self):
        self.__main_window = tkinter.Tk()
        self.__main_window.geometry('700x400')
        self.__description_frame = tkinter.Frame(self.__main_window, relief='solid',
                                                 borderwidth=1)
        text = 'This is a excel parser which can parse data from one or many excel files ' \
               'and extract them to one another.'
        self.__label = tkinter.Label(self.__description_frame,
                                     text=text, borderwidth=5)
        self.__description_frame.pack(side='top', pady=20)
        self.__label.pack(pady=10)

        self.__int_var = tkinter.IntVar()
        self.__int_var.set(0)
        self.__r_button_frame = tkinter.Frame(self.__main_window, relief='groove', borderwidth=1)

        self.__radio_but1 = tkinter.Radiobutton(self.__r_button_frame,
                                                variable=self.__int_var, value=1,
                                                text='Many files parse mode:')
        self.__radio_but2 = tkinter.Radiobutton(self.__r_button_frame,
                                                variable=self.__int_var, value=2,
                                                text='One file parse mode:')
        self.__r_button_frame.pack()
        self.__radio_but1.pack()
        self.__radio_but2.pack()


        self.__quit_button = tkinter.Button(self.__main_window, text='Quit',
                                            command=self.__main_window.destroy)
        self.__quit_button.pack(side='bottom', pady=5)

        mainloop()




if __name__ == '__main__':
    myParser()