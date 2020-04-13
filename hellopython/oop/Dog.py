# Object Oriented Programming Tutorial:
# https://www.datacamp.com/community/tutorials/python-oop-tutorial

class Dog:
    # Instantiation method
    def __init__(self, name, age):
        # Attributes: properties of the class
        self.name = name
        self.age = age
        pass

    # Method: something that the class can do
    def bark(self):
        print('bark bark!')

    # Method
    def doginfo(self):
        if self.age <= 1:
            print(self.name + ' is ' + str(self.age) + ' year old.')
        else:
            print(self.name + ' is ' + str(self.age) + ' years old.')
        
    # Method
    def birthday(self):
        self.age += 1
    
    def setBuddy(self, buddy):
        self.buddy = buddy


if __name__ == "__main__":
    ozzy = Dog("Ozzy", 2)
    skippy = Dog("Skippy", 12)
    filou = Dog("Filou", 8)
    odin = Dog("Odin", 1)

    ozzy.doginfo()
    skippy.doginfo()
    filou.doginfo()
    odin.doginfo()

    # Ozzy just had his birthday:
    ozzy.birthday()
    ozzy.doginfo()

    # Ozzy and Filou are buddies
    # Here "object filou" is assigned as buddy to ozzy,
    # therefore the methods available in filou are assesable as below
    ozzy.setBuddy(filou)
    ozzy.buddy.doginfo()
    filou.setBuddy(ozzy)
    print(ozzy.name + ' is buddies with ' + ozzy.buddy.name)