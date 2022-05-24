from datetime import datetime, timedelta


# encapsulate
class Student:

    def __init__(self, name, birthday, gender):
        self.name = name
        self.birthday = birthday
        # private - encapsulate
        self.__gender = gender
        self.__scores = []

    # propery
    @property # read
    def scores(self): # def get_scores() 
        for item in self.__scores:
            if item < 19:
                return []
        
        return self.__scores

    @scores.setter # write
    def scores(self, scores):
        # scores: [19, 20 , 19]

        for score in scores:
            if 0 <= score <= 20:
                self.__scores.append(score)
            else:
                print("Invalid score")

    @scores.deleter # delete
    def scores(self):
        # score: 20
        self.__scores.clear()

    # -------------------------------------------
    @property # behaviour -> attribute
    def age(self): # no inputs
        utcnow = datetime.utcnow()
        year, month, day = list(map(int, self.birthday.split("-")))
        birthdate = datetime(year=year, month=month, day=day)

        return (utcnow - birthdate).days // 365
    
    
    # behaviour
    # interface, gateway
    # def add_score(self, score):
    #     # score: 20
    #     if 0 <= score <= 20:
    #         self.__scores.append(score)
    #     else:
    #         print("Invalid score")
    # def get_scores()
    # def clear_scores()


asghar = Student("asghar", "1990-03-02", "male")
maryam = Student("maryam", "1999-03-02", "female")

# access to the attribute
# print(asghar.age) 

# behaviours
# def get_scores() scores
# def set_scores()
# def del_scores()

# 
# asghar.scores = []
# del asghar.scores

# attribute
# asghar.name = "akbar" # set
# print(asghar.name) # get
# del asghar.name # del

# AttributeError: 'Student' object has no attribute '__gender'
# print(asghar.__gender)
# asghar.scores = [10, 12, 13]
# print(asghar.scores)
# Invalid data
# asghar.scores = [20, 22 ,20]
# print(asghar.scores)
# asghar.add_score(20)

# setter
# asghar.scores([20 ,10 , 19]) 
print(asghar.scores) # -->  def scores(self):
asghar.scores = [19, 20 , 19] # --> def scores(self, scores):
print(asghar.scores) # -->  def scores(self):
del asghar.scores # -->     @scores.deleter def scores(self):
print(asghar.scores)

# asghar.scores = [10 , 19 , 20]

# 
# print(asghar.scores)

# -----------------------------
# set
# asghar.__scores = [20 ,10 , 19]

# asghar.add_score(10)
# print(asghar.scores)

# asghar.scores = [10, 10 , 20]
# print(asghar.scores)

# print(asghar.age())
# asghar.gender = "female"
# print(asghar.gender)