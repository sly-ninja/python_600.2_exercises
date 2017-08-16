import random
#import pylab

# Global Variables
max_rabbit_pop = 1000
current_rabbit_pop = 500
current_fox_pop = 30

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global current_rabbit_pop

    for rabbit in range(current_rabbit_pop):
        if (1 - (current_rabbit_pop/max_rabbit_pop)) > random.random():
            current_rabbit_pop += 1

            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global current_rabbit_pop
    global current_fox_pop 

    for fox in range(current_fox_pop):
        if (current_rabbit_pop/max_rabbit_pop) >= random.random() and current_rabbit_pop > 10:
            current_rabbit_pop -= 1
            if 1/3 >= random.random():
                current_fox_pop += 1
        else:
            if 1/10 >= random.random() and current_fox_pop > 10:
                current_fox_pop -= 1    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []

    for steps in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(current_rabbit_pop)
        fox_populations.append(current_fox_pop)
    
    return (rabbit_populations, fox_populations)

print(runSimulation(12))