class Person:
    def __init__(self, fname=None, lname=None, age=None, gender=None) : 
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def __str__(self):
        return "fname: {}, lname: {}, age: {} , gender: {}".format(self.fname,self.lname,self.age,self.gender)
    

if __name__ == "__main__":
    p = Person("Peter","Parker",25)
    print(p)