# dunder method
# magic function

class Mother:
    
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father # None
        self.mother = mother # None

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}" 

        # return self.name 


class Father:

    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"
        # return self.name 


class Child:
    
    # constructor
    # initialize instance
    def __init__(self, name, father, mother):
        # self: child1
        # name: "mohammad"
        # father: None
        # mother: None

        # self
        # self.name = name
        # child1.name = "Jafaei"
        # attribute
        # self.name = "jafaei"
        self.name = name
        self.father = father
        self.mother = mother

    def __str__(self):
        # call when instance is casting to str
        mother_name = self.mother.name if self.mother else ""
        father_name = self.father.name if self.father else ""
        return f"name: {self.name}, mother: {mother_name}, father: {father_name}"
        

# child1 = Child("mohammad", None, None) -> 
# __init__(child1, "mohammad", None, None)
# 
# ----------------------------------
hava = Mother("hava", None, None)
adam = Father("adam", None, None)

print(hava)

# ----------------------------------
habil = Child("habil", adam, hava)
ghabil = Child("ghabil", adam, hava)

# access to the property
# instance_name . attribute
# print(habil.name)
# print(ghabil.name)
#      [instance, instance]
kids = [habil, ghabil]

my_name = str(habil)
print(my_name)

# for kid in kids:
#     # attribute
#     #   - name
#     #   - mother
#     #   - father
#     # <__main__.Child object at 0x00000265DDDC8E50>
#     # print - str(kid)
#     print(f"kid: {kid}")
#     print(f"kid.name: {kid.name}")
#     # <__main__.Mother object at 0x000002F1E8F77880>
#     # <__main__.Father object at 0x000002F1E8F8E700>
#     print(f"kid.mother: {kid.mother}")
#     print(f"kid.father: {kid.father}")
