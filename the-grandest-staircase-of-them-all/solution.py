from itertools import combinations
from math import sqrt

def solution(n):
    staircase = []
    m = 1 + int(sqrt(n - 1))
    for r in range(1, m + 1):
        b = combinations(range(n - 1, 0, -1), r)
        for steps in b:
            if sum(steps) == n:
                staircase.append(steps)
    return len(staircase)

solution(10)

    # # the problem is that you can add bricks on top, on another row and remove them the same way

    # # the first stair is:
    # steps = [n]

    # # the last stair which cannot be modified is the one where the height = width, 
    #     # which happens only for certain numbers,
    #         # in case it doesn't, keep height >= width
    #     # you can find out that number 
        
    # # to reach that stair, remove 1 by 1 from the fist stair and add it to the next
    #     # 
        
    #     # Each type of staircase should consist of 2 or more steps
    #     # each step must be lower than the previous one
    # for step in steps:
    #     for bricks in range(step/2):
    #         step -= bricks
    #         steps[1] += i
    #         # meaning that you can remove only half - 1(2) from the current step and 
    #         # if there's no next step, create it
    #             # add it to the next step
        
    #     # A step's height is classified as the total amount of bricks that make up that step.
        
        
    #     # iterate over every step
    #         # iterate over every brick of the upper half
    #             # remove that brick from the current step
    #             # add that number to a new list
    #             # if there is no other step next, 
    #                 # create it
    #             # in the next step add 1 brick