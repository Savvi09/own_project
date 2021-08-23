from time import sleep
from random import choice

time_range = list (range(2,8))  #2,3,4,5,6,7,8

class washing_machine():
    def __init__(self,cloth):
        self.cloth = cloth

    def begin_stage(self):
        print("\n")
        machine_desc = "This machine is a brand of Whrilpool and which detects clothes to wash"
        print(machine_desc)
        print("clothes provided to the machine -".format(self.cloth))
        sleep(3)
        return "{} is yet to be washed".format(self.cloth)


class spining_machine(washing_machine):
    def __init__(self,cloth):
        self.cloth =cloth

    def spining_stage(self):
        print(self.begin_stage())
        print("\n--------------\n")
        spin_desc = "The battery of this machine has good components that help to spin the clothes"
        print(spin_desc)
        time_requires = choice(time_range)
        print("\t Total time required - {} secs".format(time_requires))
        sleep(time_requires)
        return "{} is getting spun to clean the dirt".format(self.cloth)


class drying_machine(spining_machine):
    def __init__(self,cloth):
        self.cloth =cloth

    def drying_stage(self):
        print(self.spining_stage())
        print("\n----------------\n")
        dry_desc = "The machine is pk version to dry all clothes"
        print(dry_desc)
        time_requires = choice(time_range)
        print("\t Total Time required - {} secs".format(time_requires))
        sleep(time_requires)
        return "{} is getting dry".format(self.cloth)

my_cloth =[]
my_cloth = eval(input("Enter the list of clothes : \t"))
cloths =choice(my_cloth)
machine = drying_machine(cloth=cloths)
print(machine.drying_stage())
print("\n\n {} washed successfully".format(cloths))







