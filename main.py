import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# =====================
# 1. Load data 
# =====================
data = yf.download("TSLA", start="2020-01-01", end="2024-01-01")

# flatten columns
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# keep Close only
data = data[['Close']]

print(data.head())

# =====================
# 2. Feature Engineering
# =====================
data['Days'] = range(len(data))

# =====================
# 3. Train/Test Split
# =====================
train_size = int(len(data) * 0.8)

train = data[:train_size]
test = data[train_size:]

X_train = train[['Days']]
y_train = train['Close']

X_test = test[['Days']]
y_test = test['Close']

# =====================
# 4. Model
# =====================
model = LinearRegression()
model.fit(X_train, y_train)

# =====================
# 5. Evaluation
# =====================
test_predictions = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
print("RMSE:", rmse)

# =====================
# 6. Forecast
# =====================
future_days = pd.DataFrame({'Days': range(len(data), len(data)+30)})
predictions = model.predict(future_days)

# =====================
# 7. Decision
# =====================
current_price = float(data['Close'].iloc[-1])
next_price = float(predictions[0])

if next_price > current_price:
    decision = "BUY"
elif next_price < current_price:
    decision = "SELL"
else:
    decision = "HOLD"

print("Current Price:", current_price)
print("Predicted Price:", next_price)
print("Decision:", decision)

# =====================
# 8. Plot
# =====================
future_dates = pd.date_range(start=data.index[-1], periods=30, freq='D')

plt.figure(figsize=(10,5))
plt.plot(data.index, data['Close'], label="Actual")
plt.plot(future_dates, predictions, label="Forecast")

plt.legend()
plt.title("Stock Price Forecast")
plt.xlabel("Date")
plt.ylabel("Price")

plt.savefig("forecast.png")
plt.show()


