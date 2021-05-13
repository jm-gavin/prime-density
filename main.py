import math
import graph_data
"""
AUTHOR: Jacob M Gavin
MODULES USED: math, matplotlib
DESCRIPTION: This program uses a function to check if a number is prime as well as
    another function that will take the information and compute the percentage of numbers
    within a certain range. Using this data the program will create a graph using the 
    matplotlib module and the data of both prime percentages as well as the range from 
    which the data was collected.
"""

# Changing these variables will affect the graph.
step = 20          # h This variable affects the sample size used by the graph.
                        # smaller values will create more jagged graphs

sample_range = 1000   # The amount of numbers to check. ie: a value of 10,000 will create
                        # a graph for all numbers from 1 to 10,000


def check_prime(number):
    """Takes a number and returns True if the number is prime"""
    upper_bound = math.ceil(number/2)  # calculate upper and lower bounds
    lower_bound = 2
    prime = True  # Assumes that the number is prime, until proven wrong
    for index in range(lower_bound, upper_bound):
        dividend = number/index                    # Divides the number by every index between 1 and half of itself
        if dividend - int(dividend) == 0:  # Uses the "int" function to check if a factor is whole.
            prime = False           # If is has any whole factors, it has proven not prime
            break            # Save computing power by quitting once a number has been proven not prime

    if prime:
        return True          # Self-explanatory
    else:
        return False


def prime_percent(lower_bound, upper_bound, type):
    """Calculates the likelihood that any number in the selected range will be prime"""
    total = 0     # Inits counter variable
    primes = []   # Inits list of all primes found

    print(f"-----Prime Percentage: {lower_bound} to {upper_bound}------")  # User info for range of numbers to scan
    print(f"----- scanning {upper_bound-lower_bound} numbers ------")

    for index in range(lower_bound, upper_bound):
        prime = check_prime(index)
        if prime:                           # Updates the counter variable if a number in the range is prime
            total += 1
            primes.append(index)
    prime_range = upper_bound-lower_bound    # creates tow variables for later use; just range and percent chance
    prime_pc = total/prime_range
    print(f" {prime_pc}\n\n")  # prints final value
    if type == 0:                   # if the function has 0 as an argument, returns the data for the graph
        return {upper_bound: prime_pc}
    elif type == 1: # This was used for debug purposes, to ensure that the function was catching all primes
        return primes


ranges = []         # Creates two empty lists, to be passed through the graphing function
percentages = []

# graph from 10 to whatever range, stepping by the value of "step"

for i in range(10, sample_range, step):
    """assembles lists for the graphing function"""
    percentage = prime_percent(i-step, i, 0)
    percentages.append(percentage[i])
    ranges.append(i)

graph_data.plot(ranges, percentages, step) # graphs data
