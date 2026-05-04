import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("timeseries_data.csv")
# print("Raw data",df)

df['Date'] = pd.to_datetime(df['Date'])

# basically conver 0 1 2 index with Date column
df.set_index("Date", inplace=True)
print(df)

# Step 4: Sort index (important for time series) sorted according to date
df.sort_index(inplace=True)
print(df)

print("First 5  rows",df.head())

monthly_data = df.resample('ME').mean()
print("Average sale Monthly",monthly_data)

# Step 6: Rolling statistics (moving average)  Last 7 din ka average nikaalna (har row ke liye)
# Rolling mean = chalte rehne wala (moving) average
df['Rolling_Mean'] = df["Value"].rolling(window=7).mean()
# Last 7 din me data kitna upar-neeche (variation) ho raha hai
df['Rolling_Std']  = df["Value"].rolling(window=7).std()
# print (df)

# Ek naya graph canvas bana do
plt.figure()
plt.plot(df['Value'], label='Original Data')
# plt.show() 

plt.plot(df['Rolling_Mean'],label=['Rolling mean(7days)'])
# plt.show()
plt.title('Time Series Analysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Resampled data = original data ka grouped/converted version (time ke hisaab se)
plt.figure()
plt.plot(monthly_data, label='Monthly Average')
plt.title('Monthly Resampled Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()




