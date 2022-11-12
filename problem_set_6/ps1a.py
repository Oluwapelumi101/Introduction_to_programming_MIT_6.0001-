###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:


from ps1_partition import get_partitions
from copy import deepcopy
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
# Implementing a class for each Cos
class Cow(object):
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
    
    def getName(self):
        return self.name
    
    def getWeight(self):
        return self.weight

    def __str__(self) -> str:
        return(f"Name: {self.name}, Weight: {self.weight}")

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
    # TODO: Your code here
    all_cows = {}
    cows_list = []
    my_file = open(filename, "r")
    for i in my_file:
        cow = i.rstrip().split(",")
        all_cows[cow[0]] = cow[1]
        cows_list.append(Cow(cow[0], cow[1]))
    return all_cows

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
    # TODO: Your code here
    # varables
    result = []
    cows_copy = deepcopy(cows)
    trip = []
    trip_weight = 0

    while (len(cows_copy)) >= 0:
        if len(cows_copy) == 0:
            result.append(trip)
            return(result)
        else:
            max_cow = (max(cows_copy, key=cows.get))
            max_weight = int(cows_copy[max_cow])
            if (max_weight + trip_weight) <= limit:
                trip.append(max_cow)
                trip_weight += max_weight
                del cows_copy[max_cow]
            else:
                result.append(trip)
                trip = []
                trip_weight = 0
        
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
    # Declaring Variables
    count = 0
    results = []
    # print(cows)

    # Generating trip combinations called itinerary
    for itinerary in get_partitions(cows):
        itinerary_weight = []
        for trip in itinerary:
            trip_weight = 0
            for item in trip:
                trip_weight += int(cows[item])
            itinerary_weight.append(trip_weight)
        # print(itinerary_weight, itinerary)
        # Getting only the itinerary that are within the limits
        max_trip = (max(itinerary_weight))
        if max_trip <= limit:
            results.append(itinerary)
            # print(max_trip)

    # Getting the Itinerary with the minimum number of trips in the results
    lowest = 0
    for Itinerary in results:
        t = 0
        for Trip in Itinerary:
            t += 1
        if lowest == 0:
            lowest = (t, Itinerary)
        elif t < lowest[0]:
            lowest = (t, Itinerary)
    return(lowest[1])
 
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
    # TODO: Your code here
    #Importing the Data 
    cows = load_cows("problem_set_6/ps1_cow_data_2.txt") #importig the data set

    # Function to calculate the number of trips
    def num_trips(iternery):
        num = 0
        for trip in iternery:
            num += 1
        # print(iternery)
        return(num)

    # Running and timing the Greedy algorithm
    start_greedy = time.time()
    greedy = greedy_cow_transport(cows)
    end_greedy = time.time()
    time_greedy = (end_greedy - start_greedy)
    num_greedy_trips = num_trips(greedy)

    # # Running and timing the Brute Forece algorithm
    start_brute = time.time()
    brute = brute_force_cow_transport(cows)     
    end_brute = time.time()
    time_brute = (end_brute - start_brute)
    num_brute_trips = num_trips(brute)

    # Outputs
    print("______________________")
    print(f"Number of trips for Greedy Algorithm: {num_greedy_trips} ")
    print(f"Time taken for Greedy Algorithm: {time_greedy}")
    print("______________________")
    print(f"Number of trips for Brute Force Algorithm: {num_brute_trips} ")
    print(f"Time taken for Brute Force Algorithm: {time_brute}")

compare_cow_transport_algorithms()
