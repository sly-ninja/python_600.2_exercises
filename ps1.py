###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_dict_copy = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    result = []
    total_weight = 0
    trip_list = []

        
#==============================================================================
#     for i in range (len(cow_dict_copy)):
#         
#         if (total_weight <= limit):
#             if (total_weight + cow_dict_copy[0][1] <= limit):
#                 trip_list.append(cow_dict_copy[0][0])
#                 total_weight += cow_dict_copy[0][1]
#                 print("trip_list:", trip_list, 'total_weight:', total_weight)
#                 cow_dict_copy = cow_dict_copy[1:]
#             else: 
#                 print("trip_list 2:", trip_list, 'total_weight:', total_weight)
#                 result.append(trip_list)
#                 trip_list = []
#                 total_weight = 0
#             
#         else:
#             print("when do you get here?")
#             result.append(trip_list)
#             print("result", result)
#             trip_list = []
#             total_weight = 0
#             
#     return (result)
#==============================================================================

    while cow_dict_copy[0] != cow_dict_copy[-1]:
        if (total_weight <= limit):
            if (total_weight + cow_dict_copy[0][1] <= limit):
                trip_list.append(cow_dict_copy[0][0])
                total_weight += cow_dict_copy[0][1]
                cow_dict_copy = cow_dict_copy[1:]

            else:
                result.append(trip_list)
                trip_list = []
                total_weight = 0
            
    else:
        trip_list.append(cow_dict_copy[0][0])
        result.append(trip_list)
             
    return (result)


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cow_dict_copy = sorted(cows.items(), key=lambda x: x[1], reverse=True)
        

    def trip_list_creator(cow_dict_copy, limit):
        total_weight = 0
        remaining_weight = limit - total_weight
        result = []
        trip_list = []
        
        if cow_dict_copy == [] or limit == 0:
#            print('if', total_weight)
            return trip_list
            
        elif cow_dict_copy[0][1] > remaining_weight:
#            print('elif', cow_dict_copy[0], remaining_weight, total_weight)
            trip_list = trip_list_creator(cow_dict_copy[1:], remaining_weight)
            
        else:
#            print('else', total_weight)
#            limit -= cow_dict_copy[0][1]
            with_cow = trip_list_creator(cow_dict_copy[1:], remaining_weight - cow_dict_copy[0][1])
            with_cow.append(cow_dict_copy[0][0])
            total_weight = total_weight + cow_dict_copy[0][1]
            
            without_cow = trip_list_creator(cow_dict_copy[1:], remaining_weight)
#            print('with_cow', with_cow, 'without_cow', with_cow, with_cow > without_cow)
            
            if with_cow > without_cow:
                trip_list = with_cow

            else:
                trip_list = without_cow
        
        return trip_list          
    
    for partition in get_partitions(cow_dict_copy):
        trip_list_creator(cow_dict_copy, limit)
    
#==============================================================================
#     if to_analyze == [] or limit == 0:
#         print('did you get to if 1?')
#         
#         
#     elif to_analyze[0][1] > (limit - total_weight):
#         print('did you get to if 2?')
#         to_analyze = to_analyze[1:]
#         brute_force_cow_transport(to_analyze, limit)
#         
#     else:
#         print('did you get to else?')
#         limit -= to_analyze[0][1]
#         total_weight = total_weight + to_analyze[0][1]
#         
#         if total_weight > limit:
#             print('did you get to sub-if?')
#             trip_list.append(to_analyze[0][0])
#             to_analyze = to_analyze[1:]
#             brute_force_cow_transport(to_analyze, limit)
#             
#         else:
#             print('did you get to sub-else?')
#             return trip_list
#     
#     return trip_list 
#==============================================================================

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """    
    
    start_time = time.time()
    greedy = greedy_cow_transport(cows, limit=10)
    elapsed_time = time.time() - start_time
    print('number of trips:', len(greedy))    
    print('elapsed time:', (elapsed_time))
    
#==============================================================================
#     start_time = time.time()
#     brute = brute_force_cow_transport(cows, limit=10)
#     elapsed_time = time.time() - start_time
#     print('number of trips:', len(brute))    
#     print('elapsed time:', (elapsed_time))
#==============================================================================


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=9

#print(cows)

#compare_cow_transport_algorithms()

#print(greedy_cow_transport(cows, limit=10))
#print(brute_force_cow_transport(cows, limit=10))

#brute_force_cow_transport(cows, limit=10)

