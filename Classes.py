class Person:
    
    def __init__(self, name, age, height):
        self.name=name
        self.age=age
        self.height=height

    
    def __del__(self):
        print("Object has been deleted!")


person1=Person("Mike", 25, 180)
print(person1.name)
print(person1.age)
print(person1.height)

del person1


person1.name="Michael"
print(person1.name)


