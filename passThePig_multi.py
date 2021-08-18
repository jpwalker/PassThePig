#! /bin/env python3

import numpy as np
from matplotlib.pyplot import plot, show
from random import randint
from multiprocessing import Pool
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


def runSims(stratScore):
    data = np.zeros(N, dtype=float)
    #print('Running stratScore {0}'.format(stratScore))
    for i  in range(NSim):
        #if i % 25000 == 0:
            #print('Simulation #{0}'.format(i))
        data[stratScore - 1] += runGame(stratScore) / NSim
    return data

NSim = 100000 # Run number of sims per strat
N = 100

if __name__ == '__main__':    
    startTime = clock_gettime_ns(CLOCK_MONOTONIC_RAW)
    stratScores = np.arange(1, N + 1)
    with Pool(4) as p:
        data = p.map(runSims, stratScores)
    data = np.sum(data, 1)
    print("Time spent is {0}ns.".format(clock_gettime_ns(CLOCK_MONOTONIC_RAW) - startTime))
    plot(stratScores, data, 'k-')
    show()