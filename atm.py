#This is an attempt to build an atm machine interface
import sys
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def greetings(self):
        print("WELCOME.....\nPlease insert your card.")
        print("Loading.......")


        print("Welcome, Please select your choice of language")
        print("1. Yoruba\t\t 2. English")
        print("3. Igbo\t\t   4. Hausa")
        print("\n\n5. Cancel\n")
        

    def set_Quickteller_Bills(self, amount):
        if self.__balance >amount:
            self.__balance-=amount

        else:
            print("Error occured: Insuficient funds.")

    def Airtime_Top_up(self,amount):
        if self.__balance > amount:
            self.__balance -=amount

        else:
            print("ERROR: Insuficient funds.")

        
    def Withdraw(self, amount):
        if self.__balance > amount:
            self.__balance-=amount

        else:
            print("ERROR: insuficient funds.")

        
    def Transfer(self, amount):
        if self.__balance > amount:
            self.__balance -= amount

        else:
            print("ERROR: Insuficient funds.")


    def Payarena_Bills(self, amount):
        if self.__balance > amount:
            self.__balance -= amount

        else:
            print("ERROR: Insufficient funds.")

    #The accessors
    def get_Quickteller(self):
        return self.__balance

    def get_Withdraw(self):
        return self.__balance

    def get_Transfer(self):
        return self.__balance

    def get_Payarena(self):
        return self.__balance

    def get_Airtime_topup(self):
        return self.__balance
