# dunder method
# magic function

class Human:
    
    # constructor
    def __init__(self, name, father, mother):
        self.name = name
        # father: Instance of Human
        # mother: Instance of Human
        self.father = father
        self.mother = mother

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"
        

# child1 = Child("mohammad", None, None) -> 
# __init__(child1, "mohammad", None, None)
# 
# ----------------------------------
hava = Human("hava", None, None)
adam = Human("adam", None, None)

# ----------------------------------
habil = Human("habil", adam, hava)
ghabil = Human("ghabil", adam, hava)
marry = Human("marry", adam, hava)

asghar = Human("asghar", habil, marry)

kids = [habil, ghabil]


