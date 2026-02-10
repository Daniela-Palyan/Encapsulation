# Using Python’s @property Decorators
# Refactor the Person class from Task 1 to:
# Use the @property decorator for the getter.
# Use the @name.setter decorator for the setter.
# 🔔 Requirements:
# Add validation to ensure the name length is at least 3 characters.

class Person:
    def __init__(self, new_name):
        self.name = new_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        if not new_name:
            raise ValueError("Name can not be empty")
        
        if not new_name[0].isupper():
            raise ValueError("Name must begin with uppercase letter")
        
        self.__name = new_name

    
p1 = Person("Anna")
print(p1.name)

p1.name = "Artyom"
print(p1.name)