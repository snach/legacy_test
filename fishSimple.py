class Fish_Simple(object):
    def __init__(self, name, energy=100, init_parameters=dict()):
        if init_parameters:
            self.name = init_parameters['name']
            if 'energy' in init_parameters.keys():
                condition = init_parameters["energy"]
            else:
                condition = energy
        else:
            self.name = name
            condition = energy

        self.energy = condition


    def say(self):
        print("Hello, i'm Fish_Simple and my name is "+str(self.name))


    def run(self):
        print("My name is "+str(self.name)+" and i can't run")


    def swim(self):
        print("My name is "+str(self.name)+" and i swimming")
        self.energy = self.energy - 5


    def fly(self):
        print("My name is "+str(self.name)+" and i can't fly")


    def get_energy(self):
        return self.energy

