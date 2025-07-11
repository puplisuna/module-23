class CSStudent:
    stream = 'cse'
    def __init__(self, roll):
        self.roll = roll
    
    def setaddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

# Create instances and call methods outside the class
add = CSStudent(101)
add.setaddress('123 Main St')
print(add.getaddress())  # Output: 123 Main St

a = CSStudent(101)
b = CSStudent(102)
print(a.stream)  # Output: cse
print(b.stream)  # Output: cse
print(a.roll)    # Output: 101
print(CSStudent.stream)