import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
import joblib
from dataClean import df


#Select features to be included in the model
features = ['Age', 'Km', 'IntCarb', 'IntMod', 'Puissance', 'Usage', 'Annee_modele']
X = df[features]
y = df.Prix_occassion
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#Parameters optimised
params = {
    "n_estimators": 2500,
    "max_depth": 4,
    "min_samples_split": 5,
    "learning_rate": 0.3,
    "loss": "squared_error",
}
reg = GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

#Save the model
joblib.dump(reg, 'modelAuto.pkl')
