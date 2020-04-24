###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Bongi Sibanda 
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    # open the file in read mode
    f = open(filename, "r")
    #instantiate an empty dictionary
    dict = {}
    #loop through each line in the file
    for line in f: 
        line = line.rstrip("\n")
        line = line.split(',')
        dict[line[0]] = line[1]
    f.close()
    return dict
    
   
#print(load_cows('ps1_cow_data.txt'))
# Problem 2
def greedy_cow_transport(cows,limit=10):
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
    cows_items = cows.items() 
    sorted_list_of_tuples = sorted(cows_items, key = lambda cow: cow[1], reverse = True)
    result = [] 
    
    while len(sorted_list_of_tuples)>0:
        trip = []
        total_weight = 0
        #clone the sorted list of tuples so that you start back at the element 
        #that comes first after the first cow was removed
        for cow, weight in sorted_list_of_tuples[:]:
            weight = int(weight)
            if total_weight + weight <= limit:
                trip.append(cow)
                total_weight += weight
                sorted_list_of_tuples.pop(0)
        result.append(trip)    
    return result    


    

# Problem 3

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    result = []
    
    for partition in get_partitions(cows.keys()):  
        pass_test = True
        good_partition = []
        
        for trip in partition:
            total_weight = 0 
            for cow in trip: 
                total_weight += int(cows[cow])
            if total_weight <= limit: 
                good_partition.append(trip)
         
        if len(partition) != len(good_partition):
            pass_test = False
        
        if pass_test:
            if len(result) >= len(partition) or len(result)==0:
                result = partition
                
    return result
       
                                        
        

        
# Problem 4
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
    cows = load_cows('ps1_cow_data.txt')
    greedy_start = time.time()
    print('Greedy algorithm solution:', greedy_cow_transport(cows))   
    greedy_stop = time.time()
    print(greedy_stop)
    greedy_alg_time = greedy_stop - greedy_start
    
    
    brute_start = time.time()
    print('Brute Force algorithm solution:', brute_force_cow_transport(cows))  
    brute_stop = time.time()
    brute_alg_time = brute_stop - brute_start
    
    print('Greedy algorithm takes', greedy_alg_time, 'seconds with', len(greedy_cow_transport(cows)), 'trips')
    print('Brute force algorithm takes', brute_alg_time, 'seconds with', len(brute_force_cow_transport(cows)), 'trips' )
    
compare_cow_transport_algorithms()
