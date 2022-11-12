###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
from unittest import result


def dp_make_weight(egg_weights, target_weight, memo = {}, total_eggs = 0):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here

    # sort turple
    egg_weights = sorted(egg_weights, reverse=True)
    current_weight = 0

    # Base case
    if len(egg_weights) == 0:
        return total_eggs 
    if target_weight == 0:
        return total_eggs 
    else:
        num_egg = 0
        while(egg_weights[0] + current_weight <= target_weight):
            num_egg += 1
            current_weight = current_weight + egg_weights[0]
        new_limit = target_weight - current_weight
        total_eggs = total_eggs + num_egg
        return dp_make_weight(egg_weights[1::], new_limit, memo, total_eggs)
        

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    # print(egg_weights[:-6])