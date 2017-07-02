# this program is to perform the finding cluters program on parallel 


import numpy as np
import scipy as sp
import multiprocessing as mp
from cluster_finder import *


pool=mp.Pool(processes=4)
result_list=mp.Manager().list()


def p(result,i):
	a=galaxy(i).lden()
	print galaxy(i).Id,a
#	b=galaxy(i).theata()
	result.append([galaxy.Id,a])

for i in range(500):
	pool.apply_async(p,(result_list,i))
pool.close()
pool.join()

print 'end'
