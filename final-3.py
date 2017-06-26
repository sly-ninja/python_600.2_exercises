import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    
    success = 0
    failure = 0

    def individual_trial():
        red = 4
        green = 4
        for i in range(3):
            choice = random.randint(1, red + green)
            if choice <= red: 
                red -= 1
            else:
                green -= 1
        return([red, green])

    for i in range(numTrials):
        results = individual_trial()
        if results[0] == 1 or results[1] == 1:
            success += 1
        else:
            failure +=1
    return float(success/(success + failure))

drawing_without_replacement_sim(20)