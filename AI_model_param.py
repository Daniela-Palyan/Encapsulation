# Encapsulation for AI Model Parameters
# Create a class AIModel with:
# A private field __learning_rate.
# A getter and setter for learning_rate.
# 🔔 Requirements:
# Ensure learning_rate is between 0 and 1.
# Demonstrate how encapsulation prevents setting an invalid learning rate.

class AIModel:
    def __init__(self, rate):
        self.set_learning_rate(rate)

    def set_learning_rate(self, rate):
        if not isinstance(rate, (float, int)):
            raise TypeError("learning rate must be a number")
        if not 0 <= rate <= 1:
            raise ValueError("learning rate must be between 0 and 1")
        
        self.__learning_rate = rate
    
    def get_learning_rate(self):
        return self.__learning_rate
    
    
