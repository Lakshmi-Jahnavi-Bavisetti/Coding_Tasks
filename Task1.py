class BankAccount:
    def __init__(self,Ah_name,Acc_num,Acc_balance=0):
        self.Ah_name=Ah_name
        self.Acc_num=Acc_num
        self.Acc_balance=Acc_balance
    def deposite(self,amount):
        if(amount>0):
            self.Acc_balance+=amount
            print(f"Deposited {amount}rs and Total Balance:{self.Acc_balance}")
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if(0<amount<=self.Acc_balance):
            self.Acc_balance-=amount
            print(f"Withdrew {amount}rs and Remaining Balance:{self.Acc_balance}")
        else:
            print("Insufficient Fund")
    def display(self):
        print(f"Available Total Balance is {self.Acc_balance}")
name=input("Enter account holder name:")
account_num=int(input("Enter account number:"))
print("Account Created!!")
Bank_Acc=BankAccount(name,account_num)
while(True):
    print("Select one of these options:\n")
    print("1.Deposite\n2.Withdraw\n3.Display Balance\n4.Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        amt=float(input("Enter amount to deposite\n"))
        Bank_Acc.deposite(amt)
    elif(choice==2):
        amt=float(input("Enter amount to withdraw\n"))
        Bank_Acc.withdraw(amt)
    elif(choice==3):
        Bank_Acc.display()
    else:
        break
