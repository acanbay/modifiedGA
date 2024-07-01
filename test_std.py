from modifiedGA import *
from math import *
import time

def std(array,mu):
    all = [(array[i]-mu)**2 for i in range(len(array))]
    return ( sum(all)/(len(all)) )**0.5

def problem(x):
    return (x[0]-5)**2 + (x[1]-3)**2 +(x[0]*x[1])**2 + x[0]**2*x[1]
    # 3.644972089876373416236325937

for number in [10,100,1000,10000]:
    start_time = time.time()
    all_res = []
    all_val= []
    for i in range(1000):
        mGA = algorithm(popSize=100,
                nGen=100,
                nVar=2,
                mins = [-number,-number],
                maxs = [ number, number],
                problem = problem,
                info=False )
        
        res, val = mGA.optimize()

        all_res.append(res)
        all_val.append(val)

    print()
    print( std(all_res,3.644972089876373416236325937) )
    print()

    end_time = time.time()
    hour, rem = divmod(end_time-start_time, 3600)
    minute, second = divmod(rem, 60)
    str_time = "{:0>2}:{:0>2}:{:05.2f}".format(int(hour),int(minute),second)
    print(str_time)
    print()
