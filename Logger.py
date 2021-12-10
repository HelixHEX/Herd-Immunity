from datetime import date, datetime


class Logger:
    def __init__(self, pop_size, virus, initial_infected, vaccinated_percentage):
        self.pop_size = pop_size
        self.vaccinated_percentage = vaccinated_percentage
        self.initial_infected = initial_infected

        self.total_infected = 0
        self.dead_people = 0
        self.saved_people = 0

        self.file_name = f"{virus.name}-{str(datetime.now())}.txt"

        f = open(self.file_name, 'a+')
        f.write(f"{str(datetime.now())} \n")
        f.write(f"Population Size: {pop_size} - Percent Vaccinated: {vaccinated_percentage} - Virus Name:  - Mortality Rate:  - Reproductive Rate: \n\n")

    def log(self, normal_people, vaccinated_people, dead_people, infected_people, saved_people):
        self.total_infected += infected_people
        self.dead_people = dead_people
        self.saved_people += saved_people

        f = open(self.file_name, "a+")
        f.write("\n")
        f.write(f"{str(datetime.now())}\n")
        f.write(f"\tNormal People: {normal_people} - Vaccinated People: {vaccinated_people} - Infected People: {infected_people} - Dead People: {dead_people}\n")
        f.close()

    def questions(self):
        f = open(self.file_name, "a+")
        f.write("\n")

        f.write("Percentage of the population that became infected at some point: ")
        f.write(f"{(self.total_infected/self.pop_size)*100}% \n")

        f.write("Percentage of the population that died from the virus: ")
        f.write(f"{(self.dead_people/self.pop_size)*100}% \n")

        f.write("Total number of people saved because of vaccination: ")
        f.write(f"{self.saved_people} \n")
        f.close()