class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
blu = parrot("Blu", 5)
woo = parrot("Woo", 3)
print("blu is a {}".format(blu.species))
print("blu's name is {}".format(blu.name))
print("blu's age is {}".format(blu.age))
print("woo is a {}".format(woo.species))
print("woo's name is {}".format(woo.name))
print("woo's age is {}".format(woo.age))        
