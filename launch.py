import joblib
from dataClean import df
import numpy as np
import warnings
warnings.filterwarnings("ignore")


model = joblib.load('modelAuto.pkl')


brand = str(input('Choose your car brand among these '+str(df['Marque'].unique())+': '))
brandInt = np.where(df['Marque'].unique() == brand)[0]
if len(brandInt)==0:
    print('Unknown brand, try again')

rdf = df.loc[df['Marque']==brand]
mod = str(input('Choose your car model among these '+str(rdf['Modele'].unique())+': '))
modInt = np.where(df['Modele'].unique() == mod)[0]
if len(modInt)==0:
    print('Unknown model try again')

carb = str(input('Choose your car enerfy among these '+str(df['Carburant'].unique())+': '))
carbInt = np.where(df['Carburant'].unique() == carb)[0]
if len(carbInt)==0:
    print('Unknown energy, try again')
    

age = float(input('Enter your car age: '))
km = float(input('Enter your car km number: '))
hp = float(input('Enter your car HP: '))
rYear = float(input("Enter your car year's model : "))


print('#######')
print('Final Choice:')
print('Brand, Model, Energy, Age, Km, HP, Year Model')
print(brand, mod, carb, age, km, hp, rYear)

#features = ['Age', 'Km', 'IntCarb', 'IntMod', 'Puissance', 'Usage', 'Annee_modele]
print('Your car price: ')
print(model.predict(np.array([[age,km, carbInt[0], modInt[0], hp, km/age, rYear]]))[0], 'euros')
print('Price in 5 year assuming 10,000 km/y :')
print(model.predict(np.array([[age+5,km, carbInt[0], modInt[0], hp, km/age+50000, rYear]]))[0], 'euros')

