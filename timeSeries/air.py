import pandas as pd
import numpy as np
import matplotlib.pylab as plt

def test_stationarity(timeseries):
    from statsmodels.tsa.stattools import adfuller
	
    #Determing rolling statistics
    rolmean = pd.rolling_mean(timeseries, window=12)
    rolstd = pd.rolling_std(timeseries, window=12)

    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    
    #Perform Dickey-Fuller test:
    print 'Results of Dickey-Fuller Test:'
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput

def logTransform(ts):
	#One of the first tricks to reduce trend can be transformation. For example, in this case we can clearly see that the there is a significant positive trend. So we can apply transformation which penalize higher values more than smaller values. These can be taking a log, square root, cube root, etc. Lets take a log transform here for simplicity:
	ts_log = np.log(ts)
	
	# Smoothing technique = taking rolling averages
	moving_avg = pd.rolling_mean(ts_log,window=12)
	# Average of year, so we assign 12
	'''
	plt.plot(ts_log)
	plt.plot(moving_avg, color='red')
	plt.show()
	'''
	# Subtract moving_avg from ts_log to create stationary trend
	smoothing = ts_log - moving_avg
	# Remove nan (yearly average so only December data should be not null)
	smoothing.dropna(inplace=True)
	test_stationarity(smoothing)
	
def weightAverage(ts):
	# In this case we can take yearly averages but in complex situations like forecasting a stock price, its difficult to come up with a number. So we take a weighted moving average where more recent values are given a higher weight. There can be many technique for assigning weights. A popular one is exponentially weighted moving average where weights are assigned to all the previous values with a decay factor. Find details here. This can be implemented in Pandas as:
	ts_log = np.log(ts)
	# http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-moment-functions
	expweight_avg = pd.ewma(ts_log, halflife=12)
	
	smoothing = ts_log - expweight_avg
	test_stationarity(smoothing)

def differencing(ts):
	ts_log = np.log(ts)
	
	print ts_log.head()
	print ts_log.shift().head()
	ts_log_diff = ts_log - ts_log.shift()
	
def decomposing(ts):
	from statsmodels.tsa.seasonal import seasonal_decompose
	ts_log = np.log(ts)
	decomposition = seasonal_decompose(ts_log)

	trend = decomposition.trend
	seasonal = decomposition.seasonal
	residual = decomposition.resid
	
	ts_log_decompose = residual
	ts_log_decompose.dropna(inplace=True)
	test_stationarity(ts_log_decompose)
	
	
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
df = pd.read_csv('AirPassengers.csv', parse_dates='Month', date_parser=dateparse, index_col='Month')

ts = df['#Passengers']

#test_stationarity(ts)
#logTransform(ts)
#weightAverage(ts)
#differencing(ts)
decomposing(ts)