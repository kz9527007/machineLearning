import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pylab as plt
from collections import defaultdict as dd

def timeSeries(ar,n):
	dates = pd.date_range('2012-10-01', periods=n, freq='D')
	daily = Series(ar,dates)
	
	daily_log = np.log(daily)
	
	weekly = daily.resample('W', how='sum')
	weekly_pct = np.exp(np.mean(np.log(weekly.pct_change())))
	print weekly_pct
	
	monthly = daily.resample('M', how='sum')
	monthly_pct = np.exp(np.mean(np.log(monthly.pct_change())))
	print monthly_pct
	
	week, month = dd(list), dd(list)
	for i, day in enumerate(daily):
		week[i%7].append(day/(weekly[i%7]/7.))
		month[(i/30)%12].append(day/monthly[(i/30)%12]/30)
	
	day_pct = []
	for i in xrange(7):
		day_pct.append(np.exp(np.mean(np.log(week[i]))))
	print day_pct

	month_pct = []
	for j in xrange(12):
		month_pct.append(np.exp(np.mean(np.log(month[j]))))
	print month_pct
	
		
if __name__ == '__main__':
	'''
	n = int(raw_input())
	ar = []
	for _ in xrange(n):
		ar.append(int(raw_input()))
	'''
	with open('sample_timeseries.txt') as f:
		n = int(f.readline())
		ar = []
		for _ in xrange(n):
			ar.append(float(f.readline()))
	timeSeries(ar,n)