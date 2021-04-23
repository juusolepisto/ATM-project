"""

@author: Tuomas Ylönen, Anni Halminen, Timo Uuttu, Anna Tamminen, Juuso Lepistö

A program that simply simulates an ATM
The program creates a view for netering the PIN code, from which you go to the main menu.

There currently is only one correct PIN: 1234

"""

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from menu import Menu, User


class ATM(tk.Tk):
    def __init__(self, otsikko=str(), *args, **kwargs):
        super().__init__(*args, **kwargs) #calls Tk
        self.title(otsikko)
        self.geometry('350x300')
        self.protocol('WM_DELETE_WINDOW', self.close)
        
        self.pin = ''
        self.__login()
        self.User = User()

    def __login(self):
        ''' Create a pin code entry view with buttons'''
        
        self.title('Welcome to the ATM')
        self.showpin = '_ _ _ _'
        self.Label= ttk.Label(self,text=self.showpin, background='#696969', width=5, anchor=tk.N, wraplength=60)
        self.Label.grid(row=0, column=2, sticky=tk.NE, padx=10, pady=30)
        self.Label_2=ttk.Label(self, width=10, anchor=tk.NW)
        self.Label_2.grid(row=0, column= 0, sticky=tk.NSEW, padx=10, pady=10)
        self.texts = '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '0', ' '
        self.texts_2 = 'Cancel', 'Fix', '', 'OK'
        self.colours = 'Red', 'Orange', 'White', 'Green'
        self.buttons = []
        self.buttons_2 = []
        self.commands = self.close, self.fix, self.guess, self.advance
       
        for i, text in enumerate(self.texts):
            self.buttons.append(ttk.Button(self, text=self.texts[i],command=lambda i=i: self.pinster(i+1), width=5))
            self.buttons[i].grid(row=1+i // 3, column=1+i % 3, sticky = tk.NSEW, pady = 2, padx = 2)
        
        for i, text in enumerate(self.texts_2):
            self.buttons_2.append(tk.Button(self, text=self.texts_2[i], command=self.commands[i], bg=self.colours[i], fg='White', width=10))
            self.buttons_2[i].grid(row=1+i, column=4, sticky = tk.NSEW, pady = 2, padx = 2)
        
     
    def fix(self):
        '''Correct the pin code one number at a time by deleting from the end'''
        if 4 >= len(self.pin) >= 0: 
            self.pin = self.pin[:-1]
            self.showpin = self.showpin[:len(self.pin)] + '_'
            self.Label.config(text=f'{self.showpin}')
    
    def guess(self):
        '''unused method'''
        pass
        
    def advance(self):
        '''OK button to check if the PIN is correct and go to the main menu of the machine'''
        
        if self.pin == self.User.pin:
            self.menu = Menu()
            self.destroy()
        else:
            tk.messagebox.showinfo("Warning","Incorrect PIN code") 
            self.pin = ''
            self.showpin = '_ _ _ _'
            self.Label.config(text=f'{self.showpin}')           
        
    
    def pinster(self, num):
        '''The method for entering the PIN code. Modifying the pin variable but displaying the showpin.
           Intended to obscure numbers from view for everyone'''
           
        if len(self.pin) < 4:
            if num == 11:
                self.pin += '0'
                self.showpin = self.showpin[:len(self.pin)-1] +'*'+ self.showpin[len(self.pin)-1:3]
            elif num != 10 and num != 12:
                self.pin += str(num)
                self.showpin = self.showpin[:len(self.pin)-1] +'*'+ self.showpin[len(self.pin)-1:3]
            self.Label.config(text=f'{self.showpin}')
            # print(self.pin)       #If you want to see the entered numbers in the console   

    
    def close(self):
            '''Closes the window'''
            
            title = 'You are leaving the service'
            text = 'Are you sure you want to exit?'
            if messagebox.askyesno(title, text):
                self.destroy()
            else:
                self.pin = ''
                self.showpin = '_ _ _ _'
                self.Label.config(text=f'{self.showpin}')
                

if __name__=='__main__':
    root=ATM()
    root.mainloop()