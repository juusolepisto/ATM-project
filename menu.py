"""

Menu after the login page
From here, you can perform various functions, such as viewing the account balance, depositing money into the account
or withdraw money from the account

"""

import tkinter as tk
# import tkinter.ttk as ttk

# from tkinter import messagebox

class User():
    """ Account's user, theri name, balance and pin code """
    def __init__(self, name="Matti", balance = 0 , pin = "1234"):
        self.name = name
        self.pin = pin 
        f = open("bankaccount.txt", "r")
        self.balance = int(f.read())
        f.close()


class Menu(tk.Tk):    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)       
        
        self.geometry("350x300")
        self.menu()
        self.User = User()

    def menu(self):
        """ Buttons in the menu """
        self.label = tk.Label(self, text="Welcome!", width=12, anchor=tk.CENTER, wraplength=65)
        self.label.grid(row=1, column=2, padx=10, pady=10)

        self.t = tk.Button(self, text="Deposit", width=12, anchor=tk.CENTER, wraplength=65, command=self.deposit)
        self.t.grid(row=2, column=1, padx=10, pady=10)

        self.n = tk.Button(self, text="Withdraw", width=12, anchor=tk.CENTER, wraplength=65, command= self.withdraw)
        self.n.grid(row=2, column=2, padx=10, pady=10)

        self.s = tk.Button(self, text="Balance", width=12, anchor=tk.CENTER, wraplength=65, command=self.balance)
        self.s.grid(row=2, column=3, padx=10, pady=10)

        self.t2 = tk.Button(self, text="Log out", width=12, anchor=tk.S, wraplength=65, command=self.beginning)
        self.t2.grid(row=3, column=2, sticky=tk.S)   

        
                
    def withdraw(self):
        """ Account withdrawal view, its buttons and their operation """
        withdraw = tk.Tk()
        def withdrawConfirm(money):
            if tk.messagebox.showinfo("Attention",f"Withdrawn {money}€"):
                self.User.balance = self.User.balance - money
                withdraw.destroy()
                f = open("bankaccount.txt", "w")
                f.write(str(self.User.balance))
                f.close()
                    

        self.l = tk.Label(withdraw, text="Withdrawing from account XXXX", width=12, anchor=tk.CENTER, wraplength=70)   
        self.l.grid(row=1, column=2, padx=10, pady=10)

        # Money buttons
        self.n1 = tk.Button(withdraw, text="10", width=6, anchor=tk.W, command= lambda: withdrawConfirm(10))
        self.n1.grid(row=2, column=1)

        self.n2 = tk.Button(withdraw, text="20", width=6, anchor=tk.W, command= lambda: withdrawConfirm(20))
        self.n2.grid(row=3, column=1)

        self.n3 = tk.Button(withdraw, text="40", width=6, anchor=tk.W, command= lambda: withdrawConfirm(40))
        self.n3.grid(row=4, column=1)

        self.n4 = tk.Button(withdraw, text="60", width=6, anchor=tk.E, command= lambda: withdrawConfirm(60))
        self.n4.grid(row=2, column=3)

        self.n5 = tk.Button(withdraw, text="80", width=6, anchor=tk.E, command= lambda: withdrawConfirm(80))
        self.n5.grid(row=3, column=3)

        self.n6 = tk.Button(withdraw, text="100", width=6, anchor=tk.E, command= lambda: withdrawConfirm(100))
        self.n6.grid(row=4, column=3)

        self.t4 = tk.Button(withdraw, text="Return", width=12, anchor=tk.CENTER, wraplength=65, command=withdraw.destroy) 
        self.t4.grid(row=5, column=2, padx=10, pady=10)   

    def balance(self):
        """ Account Balance View page """
        balance = tk.Tk()
        self.l1 = tk.Label(balance, text="Balance in account XXXX", width=12, anchor=tk.CENTER, wraplength=70)
        self.l1.grid(row=0, column=2, padx=10, pady=10)

        self.l2 = tk.Label(balance, text=f'{self.User.balance}', width=12, anchor=tk.CENTER, wraplength=70)
        self.l2.grid(row=1, column=2, padx=10, pady=10)

        self.t2 = tk.Button(balance, text="Return", width=12, anchor=tk.CENTER, wraplength=65, command=balance.destroy) 
        self.t2.grid(row=2, column=2, padx=10, pady=10)
        
        f = open("bankaccount.txt", "r")
        f.read()
        f.close()
                      
        

    def deposit(self):
        """ Account deposit view, its buttons and their operation """
        deposit = tk.Tk() 
        def depositConfirm(money):           
            if tk.messagebox.showinfo("Attention", f"Deposited {money}€"):
                self.User.balance = self.User.balance + money
                deposit.destroy()
                f = open("bankaccount.txt", "w")
                f.write(str(self.User.balance))
                f.close()
    
                      
        self.l3 = tk.Label(deposit, text="Depositing to account XXXX", width=12, anchor=tk.CENTER, wraplength=70)
        self.l3.grid(row=1, column=2, padx=10, pady=10)

        # Money buttons
        self.n1 = tk.Button(deposit, text="10", width=6, anchor=tk.W, command= lambda: depositConfirm(10))
        self.n1.grid(row=2, column=1)

        self.n2 = tk.Button(deposit, text="20", width=6, anchor=tk.W, command= lambda: depositConfirm(20))
        self.n2.grid(row=3, column=1)

        self.n3 = tk.Button(deposit, text="40", width=6, anchor=tk.W, command= lambda: depositConfirm(40))
        self.n3.grid(row=4, column=1)

        self.n4 = tk.Button(deposit, text="60", width=6, anchor=tk.E, command= lambda: depositConfirm(60))
        self.n4.grid(row=2, column=3)

        self.n5 = tk.Button(deposit, text="80", width=6, anchor=tk.E, command= lambda: depositConfirm(80))
        self.n5.grid(row=3, column=3)

        self.n6 = tk.Button(deposit, text="100", width=6, anchor=tk.E, command= lambda: depositConfirm(100))
        self.n6.grid(row=4, column=3)

        self.t4 = tk.Button(deposit, text="Return", width=12, anchor=tk.CENTER, wraplength=65, command=deposit.destroy) 
        self.t4.grid(row=5, column=2, padx=10, pady=10)
        
    def beginning(self):
            self.destroy() 
            # if tk.messagebox.askyesno("Do you want to log out?", "You have logged out. Program will shut down."):  
            #     self.destroy()
            # else:
            #     pass