import numpy as np
import time

def EDistance_loop(X):
    result_loop = np.zeros_like(X)
    distance = 0
    for i in range(len(X)): # no. of rows
        ci = 0
        while(ci < len(X)):
            for j in range(len(X[0])): # no. of cols
                distance += ((X[i][j]-X[ci][j])**2)
            result_loop[i][ci] = np.float64(np.sqrt(distance))
            ci += 1
            distance = 0
    return result_loop


def EDistance_cool(X):
    result_cool = np.zeros_like(X)
    result_cool = np.sqrt((np.square(X[:,np.newaxis]-X).sum(axis=2)))
    return result_cool

print 'starting running .....'
np.random.seed(100)
params = range(10,100,10)   # different param setting
nparams = len(params)       # number of different parameters

perf_loop = np.zeros([10,nparams])  # 10 trials = 10 rows, each parameter is a column
perf_cool = np.zeros([10,nparams])

counter = 0

for ncols in params:
    nrows = ncols

    print "matrix dimensions: ", nrows, ncols

    for i in range(10):
        X = np.random.randint(0,20,[nrows,ncols])   # random matrix
                                                    # you need to use random.rand(...) for float matrix

        st = time.time()
        ED_loop = EDistance_loop(X)
        et = time.time()
        perf_loop[i,counter] = et - st              # time difference

        st = time.time()
        ED_cool = EDistance_cool(X)
        et = time.time()
        perf_cool[i,counter] = et - st

    counter = counter + 1

mean_loop = np.mean(perf_loop, axis = 0)    # mean time for each parameter setting (over 10 trials)
mean_cool = np.mean(perf_cool, axis = 0)

std_loop = np.std(perf_loop, axis = 0)      # standard deviation
std_cool = np.std(perf_cool, axis = 0)

import matplotlib.pyplot as plt
plt.errorbar(params, mean_loop[0:nparams], yerr=std_loop[0:nparams], color='red',label = 'Loop Solution')
plt.errorbar(params, mean_cool[0:nparams], yerr=std_cool[0:nparams], color='blue', label = 'Matrix Solution')
plt.xlabel('Number of Cols of the Matrix')
plt.ylabel('Running Time (Seconds)')
plt.legend()
plt.savefig('CompareEDistance.pdf')
# plt.show()    # uncomment this if you want to see it right way

print "result is written to CompareEDistance.pdf"