#! /bin/env python3

import numpy as np
from matplotlib.pyplot import plot, show
from random import randint
from time import clock_gettime_ns, CLOCK_MONOTONIC_RAW

def runGame(stratScore):
    score = 0.
    while(score < stratScore):
        dice = randint(1, 6)
        if dice == 1:
            score = 0
            break
        score += dice
    return score

NSim = 100000 # Run number of sims per strat
N = 100

if __name__ == '__main__':
    startTime = clock_gettime_ns(CLOCK_MONOTONIC_RAW)
    stratScores = np.arange(1, N + 1)
    data = np.zeros(N)
    for stratScore in stratScores:
        #print('Running stratScore {0}'.format(stratScore))
        for i  in range(NSim):
            #if i % 25000 == 0:
                #print('Simulation #{0}'.format(i))
            data[stratScore - 1] += runGame(stratScore) / NSim
    print("Time spent is {0}ns.".format(clock_gettime_ns(CLOCK_MONOTONIC_RAW) - startTime))
    plot(stratScores, data, 'k-')
    show()