#  Advantages of Private Fields (__field)
# Create two classes:
# PublicData with a public field data.
# PrivateData with a private field __data and proper setters and getters.
# 🔔 Requirements:
# Show how data in PublicData can be easily changed to invalid values.
# Show how __data in PrivateData prevents direct modifications.


class PublicData:
    def __init__(self, data):
        self.data = data


class PrivateData:
    def __init__(self, data):
        self.set_data(data)

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        if not isinstance(data, str):
            raise TypeError("Data should be a string")
        
        self.__data = data


data1 = PublicData([1, 2, 3]) #ashxatum a
data1.data = None #eli ashxatum a
print(data1.data)
data2 = PrivateData("abracadabra") #TypeError: Data should be a string
print(data2.__data) #AttributeError: 'PrivateData' object has no attribute '__data'
