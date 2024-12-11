import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('dailyActivity_merged.csv')
print(df.dtypes)
list1 = df['ActivityDate'].values.tolist()
list2 = df['TotalDistance'].values.tolist()
fig = plt.figure(figsize = (10, 5))
plt.bar(list1, list2,width = 1, color = ['red', 'green'])
plt.show()
#
df=pd.read_csv('dailySteps_merged.csv')
list1=df['ActivityDay'].values.tolist()
list2 = df['StepTotal'].values.tolist()
plt.plot(list1,list2, color =  'green')
plt.show()
#
df=pd.read_csv('sleepDay_merged.csv')
list1=df['SleepDay'].values.tolist()
list2 = df['TotalTimeInBed'].values.tolist()
plt.scatter(list1, list2, c ="blue")
plt.show()
#
df=pd.read_csv('hourlySteps_merged.csv')
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])  # Convert to datetime
list1 = df[df['ActivityHour'].dt.date == pd.to_datetime('2016-04-12').date()]

# Aggregate total steps by hour
list2 = list1.groupby(list1['ActivityHour'].dt.hour)['StepTotal'].sum()

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(list2, labels=list2.index, autopct='%1.1f%%', startangle=140)
plt.show()
