# Herd-Immunity-Simulation

### Rules

1. A sick person only has a chance at infecting uninfected, unvaccinated people they encounter.  
2. An infected person cannot infect a vaccinated person. This still counts as an interaction.  
3. An infected person cannot infect someone that is already infected.  This still counts as an interaction.
4. At the end of a time step, an infected person will either die of the infection or get better.  The chance they will die is the percentage chance stored in `mortality_rate`.  
5. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change `is_vaccinated` to `True` when this happens.  
6. Dead people can no longer be infected, either. Any time an individual dies, we should also change their `infected` attribute to `False`.  
7. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.  
8. During the interactions, make note of any new individuals infected on this step. After the interactions are over, we will change the `infected` attribute of all newly infected individuals to `True`.  
9. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.  
10. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation.  We will use this logfile to determine final statistics and answer questions about the simulation.

### File Structure

There are 4 classes - `Simulation`, `Person`, `Virus`, & `Logger`

* `Simulation`: Runs the entire simulation (contains the other classes)
* `Person`: Represents the individual people in simulation
* `Virus`: Represents the virus that is spread in the simulation
* `Logger`: Logs each step of the simulation and outputs the result of the simulation

### How to run

Arguments: (`population size`, `vaccination percentage`, `virus name`, `mortality rate`, `reproduction rate`, `initial infected`(optional))

Example script (run inside terminal): ```python3 Simulation.py 100000 0.90 Ebola 0.70 0.25 10```