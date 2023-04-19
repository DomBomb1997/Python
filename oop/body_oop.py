#Parent Class
class organism:
    name = "unknown"
    species = "unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "unknown"
    carbon_based = True

    def information(self):
        msg = "\n Name: {}\n Species: {}\nLegs: {}\nArm: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg

# child class instance
class human(organism):
    name = "Alex"
    species = "Homosapian"
    legs = 2
    arms = 2
    orgin = "Earth"

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using a paper clip, chewing gum, and a roll of duct tape"
        return msg

    
# another class instance
class Dog(organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bit(self):
        msg = "\nEmites a loud, menacing growl and bites down ferociously on it's target!"
        return msg


# another child instance
class Bacterium(organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two seperate organisms"
        return msg
    









if __name__="__main__"
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bit())

    bacteria = Bacterium
    print(bacteria.information())
    print(baeria.replication())

