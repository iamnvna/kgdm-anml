class Animalia:
    def __init__(self, Kingdom, Class, Order, Genus, Species):
        self.Kingdom = Kingdom
        self.Class = Class
        self.Order = Order
        self.Genus = Genus
        self.Species = Species
    
        
    
    def description(self):
        return f"I am from Kingdom {self.Kingdom} and a Specie of the {self.Species} Family"

    def it(self):
        return f"Wow!, wow!, I'm a dog"

class Dog(Animalia):
    pass
    
class Person(Animalia):
    def myself(self):
        return f"Hi, I'm a person, and i can talk"

Hope = Animalia("Animalia", "", "", "Homo", "Sapien")
print(Hope.description())
print(Dog.it(""))
print(Person.myself(""))

        

    
