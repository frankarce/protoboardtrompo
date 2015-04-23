__author__ = 'frank'
import numpy as np


def svar(X):
    n = float(len(X))
    svar=(sum([(x-np.mean(X))**2 for x in X]) / n)* n/(n-1.)
    return svar


def CronbachAlpha(itemscores):
    itemvars = [svar(item) for item in itemscores]
    tscores = [0] * len(itemscores[0])
    for item in itemscores:
       for i in range(len(item)):
          tscores[i]+= item[i]
    nitems = len(itemscores)
    #print "total scores=", tscores, 'number of items=', nitems

    Calpha=nitems/(nitems-1.) * (1-sum(itemvars)/ svar(tscores))

    return Calpha

###########Test################
itemscores = [[ 4,14,3,3],
              [ 5,14,4,3],
              [ 1,10,1,1],
              [ 1,10,1,1]]
print "Cronbach alpha = ", CronbachAlpha(itemscores)