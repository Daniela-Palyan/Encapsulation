# Encapsulation in a Bank Account System
# Create a class BankAccount with:
# A private field __balance initialized to 0.
# A public getter method to check the balance.
# A public setter method to deposit money (must be a positive number).
# A method to withdraw money (cannot withdraw more than the balance).
# 🔔 Challenge:
# Prevent direct modification of __balance from outside the class.
# Demonstrate by trying account.__balance = 10000 and show that it doesn’t work.

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance
    
    def deposit(self, money):
        if not isinstance(money, (float, int)):
            raise TypeError("Money should be a number!")
        if money <= 0:
            raise ValueError("Money should be a positive number!")
        
        self.__balance += money

    def withdraw(self, money):
        if not isinstance(money, (float, int)):
            raise TypeError("Money should be a number!")
        if money <= 0:
            raise ValueError("Money should be a positive number!")
        if money > self.get_balance():
            raise ValueError("You cannot withdraw more money that you have in your balance!")
        
        self.__balance -= money