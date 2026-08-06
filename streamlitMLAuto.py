import streamlit as st
import joblib
from dataClean import df
import numpy as np

# App title
st.title("Estimate used car price")

# Car info selection
brand = st.selectbox("Brand", df['Marque'].unique())
brandInt = np.where(df['Marque'].unique() == brand)[0]

dfB = df.loc[df['Marque']==brand]

mod = st.selectbox("Model", dfB['Modele'].unique())
modInt = np.where(df['Modele'].unique() == mod)[0]

carb = st.selectbox("Energy", df['Carburant'].unique())
carbInt = np.where(df['Carburant'].unique() == carb)[0]

km = st.slider("Mile age of the car (km)", min_value=0, max_value=300000, value=50000)
age = st.number_input("Age of the car", min_value=1, max_value=30, value=10)
hp = st.selectbox("Horse power", df['Puissance'].unique())
rYear = st.number_input("Car model year", min_value=2006, max_value=2024, value=2010)


# Button to launch prediction
if st.button("Price estimation"):
    model = joblib.load('modelAuto.pkl')
    
    price = model.predict(np.array([[age,km, carbInt[0], modInt[0], hp, km/age, rYear]]))
    price5year = model.predict(np.array([[age+5,km, carbInt[0], modInt[0], hp, km/age+50000, rYear]]))

    st.success(f"Estimated price **{price[0]:,.0f} €**")
    st.success(f"Estimated price in 5 year assuming 10,000 km/y **{price5year[0]:,.0f} €**")