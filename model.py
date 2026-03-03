import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import joblib

df = pd.read_csv("data/world_happiness.csv")

features = ['Economy (GDP per Capita)','Health (Life Expectancy)',
            'Freedom','Trust (Government Corruption)',
            'Generosity','Family','Dystopia Residual']

X = df[features]
y = df["Happiness Score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression for prediction
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Random Forest for feature importance
rf_model = RandomForestRegressor(n_estimators=300, random_state=42)
rf_model.fit(X_train, y_train)

# Save models
joblib.dump(lr_model, "linear_model.pkl")
joblib.dump(rf_model, "rf_model.pkl")

print("Models saved!")