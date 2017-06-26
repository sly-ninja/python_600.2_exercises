import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.

    For example,
    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]
    """
    import itertools

    test = []
    second = []
    
    for i in [list(i) for i in itertools.product([0, 1], repeat=len(choices))]:

        current_sum = sum(c*e for c,e in zip(choices,i))
        previous_sum = 0
        
        if current_sum == total:
            test.append(i)
        
        if current_sum < total:
            
            if current_sum > previous_sum:
                second.append(i)
                previous_sum = current_sum
            
    return (min(test, key=sum) if test else max(second))


#def find_combination(choices, total):
#    bins = np.array(list(itertools.product([0, 1], repeat=len(choices))))
#    combinations = [b for b in bins if sum(choices * b) == total]
#    return (min(combinations, key=sum) if combinations else
#            max([b for b in bins if sum(choices * b) < total], key=sum))    
    


print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3], 5))
print(find_combination([1,1,1,9], 4))