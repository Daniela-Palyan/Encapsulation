# Basic Encapsulation with Getters and Setters
# Create a class named Person with the following:
# A private field __name.
# A public getter method get_name() that returns the name.
# A public setter method set_name(new_name) that sets a new name.
# 🔔 Requirements:
# Prevent setting the name to an empty string.
# Demonstrate usage by creating a Person object, setting the name, and printing it.

class Person:
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if not new_name:
            raise ValueError("Name can not be empty")
        
        if not new_name[0].isupper():
            raise ValueError("Name must begin with uppercase letter")
        
        self.__name = new_name

    def get_name(self):
        return self.__name
    
p1 = Person("Anna")
print(p1.get_name())