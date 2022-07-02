# creating a class Animalia
class Animalia:
    # initiating instance attributes
    def __init__(self, Kingdom, Class, Order, Genus, Species):
        self.Kingdom = Kingdom
        self.Class = Class
        self.Order = Order
        self.Genus = Genus
        self.Species = Species
    
        
# creating an instance methods    
    def description(self):
        return f"I am from Kingdom {self.Kingdom} and a Specie of the {self.Species} Family"
# another instance method
    def it(self):
        return f"Wow!, wow!, I'm a dog"

# creating a child class, inheriting from the parent class
class Dog(Animalia):
    pass
# another child class inheriting from the parent class     
class Person(Animalia):
    # an instance method of the child class
    def myself(self):
        return f"Hi, I'm a person, and i can talk"

# creating objects of the classes
Hope = Animalia("Animalia", "", "", "Homo", "Sapien")
print(Hope.description())
print(Dog.it(""))
print(Person.myself(""))

        

    
