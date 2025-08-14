"""ARIMA/SARIMA/LSTM modeling functions"""
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pmdarima as pm
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Load the processed data
data = pd.read_csv('data/processed/merged_data.csv', index_col='Date', parse_dates=True)
tsla_data = data['TSLA'].dropna()

# Split the data
train_size = int(len(tsla_data) * 0.8)
train, test = tsla_data[0:train_size], tsla_data[train_size:len(tsla_data)]

# ARIMA Model
auto_arima_model = pm.auto_arima(train, seasonal=False, stepwise=True, suppress_warnings=True, trace=True)
print(f"Best ARIMA order: {auto_arima_model.order}")

model = ARIMA(train, order=auto_arima_model.order)
model_fit = model.fit()
arima_forecast = model_fit.forecast(steps=len(test))

# LSTM Model
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(tsla_data.values.reshape(-1, 1))

train_data = scaled_data[0:train_size,:]
test_data = scaled_data[train_size:len(tsla_data),:]

def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        dataX.append(a)
        dataY.append(dataset[i + time_step, 0])
    return np.array(dataX), np.array(dataY)

time_step = 100
X_train, y_train = create_dataset(train_data, time_step)
X_test, y_test = create_dataset(test_data, time_step)

X_train = X_train.reshape(X_train.shape[0],X_train.shape[1] , 1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1] , 1)

lstm_model = Sequential()
lstm_model.add(LSTM(50,return_sequences=True,input_shape=(100,1)))
lstm_model.add(LSTM(50, return_sequences=True))
lstm_model.add(LSTM(50))
lstm_model.add(Dense(1))
lstm_model.compile(loss='mean_squared_error',optimizer='adam')
lstm_model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=1,batch_size=64,verbose=1)

# For simplicity, we are not generating a full forecast with LSTM here,
# as it requires a more complex iterative prediction loop.
# The focus is on demonstrating the model building process.

print("Modeling complete.")