import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/33244/Desktop/IBI1_2022-23/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5) #read the head 5 line of the dataframe
covid_data.info()
print(covid_data.describe(include='all'))
covid_data.iloc[0,1]
covid_data.iloc[2,0:5]
covid_data.iloc[0:2,:]
covid_data.iloc[0:10:2,0:5]
a = covid_data.iloc[100:1001:100,2]
print(a)
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3,my_columns]
covid_data.loc[2:4,"date"]
covid_data.loc[0:81,"total_cases"]
#creat a variable to calculate the number of loop
#use a while loop to test the place
 #add a boolean value to the variable
 #change the index
#print the Afghanistan's total_cases
Afghanistan_rows = []
i = 0
while i != 7996:
    if covid_data.loc[i,"location"] == "Afghanistan":
       Afghanistan_rows.append(i)
    i = i + 1

print(Afghanistan_rows)
covid_data.iloc[Afghanistan_rows,5]


new_data_rows = []
i = 0
while i != 7996:
    if covid_data.loc[i,"date"] == "2020-03-31":
       new_data_rows.append(i)
    i = i + 1

new_data_columns = [False, True, True, True, False, False]
new_data = covid_data.iloc[new_data_rows,new_data_columns]
print(new_data)


mean = new_data[['new_cases','new_deaths']].mean()
print(mean)
new_cases = new_data.loc[:, 'new_cases']
mean_new_cases = np.mean(new_cases)
new_deaths = new_data.loc[:, 'new_deaths']
mean_new_deaths = np.mean(new_deaths)
result = mean_new_deaths / mean_new_cases
print (result)



# Create two separate box plots using matplotlib
boxprops = dict(linestyle='--', linewidth=2, color='black')
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].boxplot(new_cases,boxprops=boxprops)
axs[0].set_title('New Cases on March 31')
axs[1].boxplot(new_deaths,boxprops=boxprops)
axs[1].set_title('New Deaths on March 31')
plt.show()




Algeria = []
i = 0
while i != 7996:
    if covid_data.loc[i,"location"] == "Algeria":
       Algeria.append(i)
    i = i + 1

print(Algeria)
world_data = covid_data.loc[Algeria,['total_cases','total_deaths']]
world_dates = covid_data.loc[Algeria,'date']
plt.plot(world_dates, world_data['total_cases'], 'bo')
plt.plot(world_dates, world_data['total_deaths'], 'rs')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()




Austria = []
i = 0
while i != 7996:
    if covid_data.loc[i,"location"] == "Austria":
       Austria.append(i)
    i = i + 1

print(Austria)
Austria_data = covid_data.loc[Austria,['total_cases','total_deaths']]
Austria_dates = covid_data.loc[Austria,'date']
plt.plot(Austria_dates, Austria_data['total_cases'], 'ro')
plt.plot(Austria_dates, Austria_data['total_deaths'], 'bo')
plt.xticks(Austria_dates.iloc[0:len(Austria_dates):4],rotation=-90)
plt.title('Total cases and deaths in Austria')
plt.xlabel('Date')
plt.ylabel('number')
plt.show()

UK = []
i = 0
while i != 7996:
    if covid_data.loc[i,"location"] == "United Kingdom":
       UK.append(i)
    i = i + 1

UK_data = covid_data.loc[UK,['new_cases','total_cases']]
UK_dates = covid_data.loc[UK,'date']
plt.plot(UK_dates, UK_data['new_cases'], 'ro')
plt.plot(UK_dates, UK_data['total_cases'], 'bo')
plt.xticks(UK_dates.iloc[0:len(UK_dates):4],rotation=-90)
plt.title('Trends in total and new cases in the United Kingdom')
plt.xlabel('Date')
plt.ylabel('number')
plt.show()





