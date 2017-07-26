# import all necessary packages and functions.
import csv
import datetime
import numpy as np
import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

# file locations
file_in  = '201402_trip_data.csv'
file_out = '201309_trip_data.csv'

with open(file_out, 'w') as f_out, open(file_in, 'r') as f_in:
    # set up csv reader and writer objects
    in_reader = csv.reader(f_in)
    out_writer = csv.writer(f_out)

    # write rows from in-file to out-file until specified date reached
    while True:
        datarow = next(in_reader)
        # trip start dates in 3rd column, m/d/yyyy HH:MM formats
        if datarow[2][:9] == '10/1/2013':
            break
        out_writer.writerow(datarow)

sample_data = pd.read_csv('201309_trip_data.csv')
display(sample_data.head())

df_201402 = pd.read_csv('201402_station_data.csv')
result = df_201402.drop(df_201402.columns[[0,2,3]], axis=1)

# city stores the unique landmark names
cities = result.landmark.unique()

no_of_docks = {}
no_of_station = {}
for city in cities:
    land = result[result['landmark'].str.contains(city)]
    docks = land["dockcount"].sum()
    no_of_station[city] = len(land.index)
    no_of_docks[city] = docks

print(no_of_docks)
print(no_of_station)

labels_dock = []
values_dock = []
for key, value in no_of_docks.items():
    labels_dock.append(key)
    values_dock.append(value)

labels_station = []
values_station = []
for key, value in no_of_station.items():
    labels_station.append(key)
    values_station.append(value)

fig = plt.figure()
fig.suptitle('Docks ', fontsize=12, fontweight='bold')
# Create a pie chart
colors = ["#0287BC","#0AB9FB", "#5CD1FE","#8BDAF9", "#ACE6FD"]
plt.pie(values_dock, labels = labels_dock,shadow = True, colors = colors, startangle = 90)
# View the plot
plt.tight_layout()
plt.show()

fig = plt.figure()
fig.suptitle('Station ', fontsize=12, fontweight='bold')
# Create a pie chart
colors = ["#0287BC","#0AB9FB", "#5CD1FE","#8BDAF9", "#ACE6FD"]
plt.pie(values_station, labels = labels_station, shadow = True, colors = colors, startangle = 90)
# View the plot
plt.tight_layout()
plt.show()


# who uses the BABS
df_trip_201402 = pd.read_csv('201402_trip_data.csv', names=('TripID','Duration','Start_Date','Start_Station','Start_Terminal','End_Date','End_Station','End_Terminal','Bike','Subscription_Type','Zip_Code'), header = 0)

df_trip_201402['Start_Date'] = pd.to_datetime(df_trip_201402['Start_Date'])

# city stores the unique landmark names
subscription = df_trip_201402.Subscription_Type.unique()
subscription_count = []
for i in subscription:
    sub = df_trip_201402[df_trip_201402['Subscription_Type'].str.contains(i)]
    subscription_count.append(len(sub.index))

print (subscription)
print (subscription_count)

fig = plt.figure()
fig.suptitle('Station ', fontsize=12, fontweight='bold')
# Create a pie chart
colors = ["#0287BC", "#ACE6FD"]
patches = plt.pie(subscription_count, shadow = True, colors = colors, startangle=90)
plt.legend(patches, labels= subscription, loc="best")
plt.show()

# Create a bar graph
x_plot = np.arange(len(subscription_count))
patches = plt.bar([1,2], subscription_count, color=colors)
plt.suptitle("Riders")
plt.ylabel('Costumers')
plt.xticks(x_plot+1, subscription)
plt.legend(patches, labels= subscription, loc="best")
plt.show()
