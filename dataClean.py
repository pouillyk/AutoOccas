import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

print('### Data cleaning ###')
#Load dataset as a DataFrame
df = pd.read_csv('dataset_Car.csv')

print('Initial data lenght', len(df))

#Create a float version of the "Date_premiere_mise_en_circulation" column
#Assume today's date in Jan 1st 2025 as the last dataset's update was in 2024
dateMax = '2024-12-31'
#Use POSIX timestamp (number of seconds since Jan 1st 1970) converted in years
dateMax = pd.Timestamp(dateMax).timestamp()/31536000
df['Date_PMC_Float'] = df['Date_premiere_mise_en_circulation']
for i in range(len(df['Date_PMC_Float'])):
    df['Date_PMC_Float'][i] = pd.Timestamp(df['Date_PMC_Float'][i]).timestamp()/31536000

#Define new colum "Age" for the age of the car
df['Age'] = dateMax - df['Date_PMC_Float']
#Remove all cars released after the today's date
df = df.drop(df[df.Age <= 0].index)

#Define new column "Usage" defined as the number of Km drove per year
df['Usage'] = df['Km']/df['Age']
#Remove all cars with non feasible usage columns (based on the world record 160 000 km/yr)
kmMax = 160000
df.loc[df['Usage']>=kmMax, :]
df = df.drop(df[df.Usage >= kmMax].index)
#Convert the "Carburant" column to int to be included in the model
df['IntCarb'] = df['Carburant']
CarbArr=df['Carburant'].unique()
for i, carb in enumerate(CarbArr):
    df['IntCarb'].loc[df['IntCarb']==carb]=i
#Convert the "Modele" column to int to be included in the model
df['IntMod'] = df['Modele']
ModArr=df['Modele'].unique()
for i, mod in enumerate(ModArr):
    df['IntMod'].loc[df['IntMod']==mod]=i

#Remove Tesla car other than electric type
df = df.drop(df[(df.Marque =='Tesla') & (df.Carburant!='Electrique')].index)
#Remove Electrique and Hybrid car othe that automatic
df = df.drop(df[(df.Carburant =='Electrique') & (df.Boite_vitesse!='Automatique')].index)
df = df.drop(df[(df.Carburant =='Hybride') & (df.Boite_vitesse!='Automatique')].index)



print('Final data length', len(df))