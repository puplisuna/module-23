class dog:
    species = "dog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

nelson = dog("Nelson", 5)
bruno = dog("Bruno", 3)
print("nelson is a {}".format(nelson.species))
print("bruno is a {}".format(bruno.species))
print("nelson's name is {}".format(nelson.name))
print("bruno's name is {}".format(bruno.name))
print("nelson's age is {}".format(nelson.age))
print("bruno's age is {}".format(bruno.age))
print("bruno's species is {}".format(bruno.species))
print("nelson's species is {}".format(nelson.species))