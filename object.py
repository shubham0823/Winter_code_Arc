class Anime:
    def __init__(self, name , eposides , type):
        self.name  = name
        self.eposides = eposides
        self.type = type

    def info(self):
        print(f"{self.name} has {self.eposides} eposides and tpye of anime is {self.type}")

# a = Anime()
# b = Anime()
# c = Anime()

# a.name = "naruto"
# a.eposides = 720

# b.name= "dragon ball z"
# b.eposides = 320

# c.name = "fullmetal alchemist"
# c.eposides = 64
# c.type = "action  dark adventure"

#ulternate method
first = Anime("maid sama" , 24 , "rom com")
e = Anime("euraka seven" , 11 , "mecha")
f = Anime("fuuka" , 12 , "music  romcom")


# a.info()
# b.info()
# c.info()
first.info()
e.info()
f.info()


  