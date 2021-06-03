import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fbprophet import Prophet
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults


df = pd.read_csv("weather.csv")
print(df)
train_size, test_size, validation_size = 0.6, 0.2, 0.2
train = df.iloc[:int(len(df)*train_size), :]
test = df.iloc[int(len(df)*train_size+1):int(len(df)*train_size+len(df)*test_size):]
validation = df.iloc[int(len(df)*train_size+len(df)*test_size+1):, :]


def fbprophet_model(train, test, validation):
    """Розбиваємо дані на train, test та validation set, використовуємо метрики rmse та mse для порівняння."""
    work_set = train.copy().append(test.copy())
    work_set = work_set[["Date", "Temperature"]]
    work_set = work_set.rename({"Date": "ds", "Temperature": "y"}, axis=1)
    comp_set = validation.copy()[["Date", "Temperature"]]
    comp_set = comp_set.rename({"Date": "ds", "Temperature": "y"}, axis=1)
    model = Prophet(daily_seasonality=True)
    model.fit(work_set)
    future = model.make_future_dataframe(periods=len(comp_set))
    res_set = model.predict(future)[["ds", "yhat"]].yhat.values[-len(comp_set):]
    rmse = mean_squared_error(comp_set["y"].values, res_set, squared=False)
    return res_set, rmse


fbprophet_model_res, fbprophet_model_rmse = fbprophet_model(train, test, validation)
plt.plot(fbprophet_model_res)
plt.plot(validation["Temperature"].values)


def moving_average():
    """SMA - Simple Moving Average"""
    df = pd.read_csv('weather.csv')  # Load data from csv
    df.head(15)  # Get content
    df.index = pd.Index(df.Date)
    df = df[['Wind', 'Temperature']]
    df.head(15)
    df['Prediction'] = df.Temperature.rolling(window=10).mean()  # Create column with result
    plt.figure(figsize=(12, 8))
    plt.title('Prediction')
    plt.plot(df.index, df[['Prediction']])
    plt.xticks(df.index[::12], rotation='vertical')
    plt.show()


moving_average()


def ARIMAS():
    """Auto Regressive Integrated Moving Average"""
    df=pd.read_csv('weather.csv')
    df.head()

    # Updating the header
    df['Date'] = pd.to_datetime(df['Date'],infer_datetime_format=True)  #convert from string to datetime
    df.head()
    df.describe()
    indexedDataset = df.set_index(['Date'])
    plt.xlabel('Date')
    plt.ylabel('Predict')
    plt.plot(indexedDataset)
    rolmean = indexedDataset.rolling(window=12).mean()  # Can be outputed
    rolstd = indexedDataset.rolling(window=12).std()  # Can be outputed
    plt.legend(loc='best')
    indexedDataset_logScale = np.log(indexedDataset)
    plt.plot(indexedDataset_logScale)
    movingAverage = indexedDataset_logScale.rolling(window=12).mean()
    plt.plot(indexedDataset_logScale)
    plt.plot(movingAverage, color='red')
    datasetLogScaleMinusMovingAverage = indexedDataset_logScale - movingAverage
    datasetLogScaleMinusMovingAverage.head(12)
    datasetLogScaleMinusMovingAverage.dropna(inplace=True)
    datasetLogScaleMinusMovingAverage.head(10)
    plt.show()


ARIMAS()
