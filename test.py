# import all necessary packages and functions.
import csv
import datetime
import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

print ('Importing CSV file')
df_trip_201402 = pd.read_csv('201402_trip_data.csv', names=('TripID','Duration','Start_Date','Start_Station','Start_Terminal','End_Date','End_Station','End_Terminal','Bike','Subscription_Type','Zip_Code'), header = 0)
df_trip_201402['Start_Date'] = pd.to_datetime(df_trip_201402['Start_Date'])

print('Only dates')
df_trip_201402["only_date"] = [str(d.date()) for d in df_trip_201402["Start_Date"]]
print(df_trip_201402["only_date"])

unique_dates = df_trip_201402.only_date.unique()
print ("UNIQUE DATES")
print(unique_dates)

no_of_bikes = {}
for di in unique_dates:
    date = df_trip_201402[df_trip_201402['only_date'].str.contains(d)]
    bike = date["Bike"].sum()
    no_of_bikes[d] = bike
print("Dates and bike")
print(no_of_bikes)

dates_list = []
bikes = []
for key, values in no_of_bikes.items():
    dates_list.append(key)
    bikes.append(values)

print (dates_list)
print(bikes)

plt.plot(bikes, "ro-")
plt.show()
