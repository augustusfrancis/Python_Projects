import pickle
import random
from datetime import date

class ATM():
    def __init__(self,name,acc_no,pin,balance=0):
        self.name=name
        self.acc_no=acc_no
        self.pin=pin
        self.balance=balance
        self.failed_attempts = 0
        self.is_locked = False
        self.daily_withdrawn = 0
        self.last_withdraw_date = None

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("amount:",amount,"has been credited to your account:",self.acc_no,"avalable balance:",self.balance)
        else:
            print("invalid amount")

    def withdraw(self,amount):
        DAILY_LIMIT=20000
        today=date.today()

        if self.last_withdraw_date != today:
            self.daily_withdrawn = 0
            self.last_withdraw_date = today

        if amount > self.balance:
            print("Insufficient balance!")

        elif self.daily_withdrawn + amount > DAILY_LIMIT:
            print("Daily withdrawal limit exceeded!")

        else:
            self.balance -= amount
            self.daily_withdrawn += amount
            print("Withdrawal successful,Remaining balance:", self.balance)

    def display(self):
        print("account number:",self.acc_no,"name:",self.name,"balance:",self.balance)

try:
    with open("atm.pkl","rb") as f:
        accounts=pickle.load(f)
except (FileNotFoundError,EOFError):
    accounts={}

def savedata():
    with open("atm.pkl","wb") as f:
        pickle.dump(accounts,f)

def set_pin():
    pin=random.randint(1000,9999)
    return pin
        
def open_account():
    name=input("enter your name:")
    acc_no=len(accounts)+1

    while True:
        print("generate pin: yes/no")
        option=input("enter option:")
        if option.lower()=="yes":
            pin=set_pin()
            print("your generated pin:",pin)
            break
        elif option.lower()=="no":
            break
        else:
            print("invalid input!")
    
    while True:
        try:
            initial=float(input("enter the intial deposit:"))
            break
        except ValueError:
            print("invalid amount!")
            
    accounts[acc_no]=ATM(name,acc_no,pin,initial)
    savedata()
    print("account created sucessfull for ",name,"account number",acc_no)

def deposit_money():
    acc_no=int(input("enter your account number:"))
    pin=int(input("enter your ATM pin:"))
    if acc_no not in accounts:
        print("account not found!")
    elif accounts[acc_no].pin!=pin:
        print("PIN invalid")
    else:
        while True:
            try:
                amount=float(input("enter the deposit:"))
                break
            except ValueError:
                print("invalid amount!")
        accounts[acc_no].deposit(amount)
        savedata()
        
def withdraw_money():
    acc_no=int(input("enter your account number:"))
    pin=int(input("enter your ATM pin:"))
    if acc_no not in accounts:
        print("account not found!")
    elif accounts[acc_no].pin!=pin:
        print("PIN invalid")
    else:
        while True:
            try:
                amount=float(input("enter the withdrawal amount:"))
                break
            except ValueError:
                print("invalid amount!")
        accounts[acc_no].withdraw(amount)
        savedata()

def display_account():
    acc_no=int(input("enter your account number:"))
    if acc_no not in accounts:
        print("account not found!")
    else:
        accounts[acc_no].display()

while True:
    print("options")
    print("1.open account")
    print("2.deposit")
    print("3.withdraw")
    print("4.display")
    print("5.quit")

    option=int(input("enter your option:"))

    if option==1:
        open_account()
    elif option==2:
        deposit_money()
    elif option==3:
        withdraw_money()
    elif option==4:
        display_account()
    elif option==5:
        print("exiting...")
        break
    else:
        print("invalid option!")