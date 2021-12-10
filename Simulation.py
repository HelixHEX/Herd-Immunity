from Virus import Virus
from Person import Person
from random import choice, shuffle, random, seed
import sys
from time import sleep, time
from Logger import Logger

class Simulation:
    def __init__(self, pop_size, vaccinated_percentage, virus_name, reproductive_rate, mortality_rate, inital_infected=1):
        self.virus = Virus(virus_name, mortality_rate, reproductive_rate)
        self.population = []
        # print(virus_name)
        self.logger = Logger(pop_size, self.virus, vaccinated_percentage, inital_infected)

        #create population
        for i in range(pop_size):
            self.population.append(Person())
        
        #vaccinate people 
        for i in range(int(pop_size * vaccinated_percentage)):
            self.population[i].is_vaccinated = True

        #infect people
        infected_people = inital_infected
        while infected_people > 0:
            person = choice(self.population)
            if not person.is_vaccinated and not person.is_infected:
                person.is_infected = True
                infected_people -= 1
            shuffle(self.population)

    def get_infected_people(self):
        infected_people = []
        for i in range(len(self.population)):
            if self.population[i].is_infected and not self.population[i].is_dead:
                infected_people.append(self.population[i])
        return infected_people

    def get_normal_people(self):
        normal_people = []
        for i in range(len(self.population)):
            if not self.population[i].is_vaccinated and not self.population[i].is_dead and not self.population[i].is_infected:
                normal_people.append(self.population[i])
        return normal_people

    def get_vaccinated_people(self):
        vaccinated_people = []
        for i in range(len(self.population)):
            if self.population[i].is_vaccinated:
                vaccinated_people.append(self.population[i])
        return vaccinated_people

    def get_dead_people(self):
        dead_people = []
        for i in range(len(self.population)):
            if self.population[i].is_dead:
                dead_people.append(self.population[i])
        return dead_people

    def step(self):
        infected = self.get_infected_people()
        new_infected = []
        saved_people = 0
        for i in range(len(infected)):
            for x in range(100):
                ranum_person = choice(self.population)
                if not ranum_person.is_dead and not ranum_person.is_vaccinated and not ranum_person.is_infected:
                    ranum_num = random()
                    if ranum_num <= self.virus.reproductive_rate:
                        ranum_person.is_infected = True
                        new_infected.append(ranum_person)
                elif ranum_person.is_infected:
                    saved_people += 1
            ranum_mort = random()
            if ranum_mort <= self.virus.mortality_rate:
                infected[i].is_dead = True
                infected[i].is_infected = False
            else:
                infected[i].is_vaccinated = True
                infected[i].is_infected = False
        self.logger.log(len(self.get_normal_people()), len(self.get_vaccinated_people()), len(self.get_dead_people()), len(self.get_infected_people()), saved_people)
        # print(self.get_infected_people())
        if len(self.get_infected_people()) <= 0:
            self.logger.questions()

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("Missing a few arguments")
        quit()
    else:
        seed(time())
        simulation = Simulation(int(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), int(sys.argv[6]))
        steps = 0
        while len(simulation.get_infected_people()) > 0:
            print("")
            simulation.step()
            steps += 1

        print(f"\nSteps: {steps}")