import os, sys
curr_dir = os.getcwd().split('/')
sys.path.append('/'.join(curr_dir[:-1]))
ts_dir = curr_dir[:-1]
ts_dir.append('timeseries')
sys.path.append('/'.join(ts_dir))
import timeseries.Timeseries as ts
import SimilaritySearch as ss
import numpy as np

'''
This file is a script to generate
1000 different timeseries

How to run:
python generateTS.py

Require folders:
tsdata

'''


if __name__ == "__main__":

	for i in range(1000):
		file_path = 'tsdata/ts'+str(i)+'.dat'
		fp = open(file_path,'w+')
		t1 = ss.tsmaker(0.5, 0.1, 0.01)
		np.savetxt(file_path,np.transpose(np.array([list(t1.itertimes()),list(t1)])), delimiter=' ')

