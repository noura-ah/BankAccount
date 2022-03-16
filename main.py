# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime


class Account:
    def __init__(self):
        self.__balance = 0  # set to zero when initiate new acount

    def deposit(self, money):
        self.__balance += money
        self.print_info("{} SAR was deposited into".format(money))

    def withdraw(self, money):
        self.__balance -= money
        self.print_info("{} SAR was withdrawn from".format(money))

    #print the current balance when called by user
    def query(self):
        print("Your current balance is", self.__balance,"SAR")

    #print the process(deposit, withdraw) summary to the user when get called by the process
    def print_info(self, process):
        date = datetime.datetime.today()
        print(process + " your bank balance on",
              date.strftime("%A, %B %d %Y at %I:%M %p"))


newaccount = Account()
newaccount.query()
newaccount.deposit(100)
newaccount.query()
newaccount.withdraw(60)
newaccount.query()

'''
Your current balance is 0 SAR
100 SAR was deposited into your bank balance on Wednesday, March 16 2022 at 07:20 PM
Your current balance is 100 SAR
60 SAR was withdrawn from your bank balance on Wednesday, March 16 2022 at 07:20 PM
Your current balance is 40 SAR
'''