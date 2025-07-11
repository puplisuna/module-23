class parrot:
    species = "bird"

    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self, dance):
        return "{} dances {}".format(self.name, dance)

# Create instances and call methods outside the class
blu = parrot("Blu", 10)
print(blu.sing("Happy Birthday")) 
print(blu.dance("Salsa"))
woo = parrot("Woo", 5)
print(woo.sing("Twinkle Twinkle Little Star"))
print(woo.dance("Ballet"))