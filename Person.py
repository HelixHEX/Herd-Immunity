class Person:
    def __init__(self, vaccinated=False, is_dead=False, infected=False):
        self.is_vaccinated = vaccinated
        self.is_dead = is_dead
        self.is_infected = infected