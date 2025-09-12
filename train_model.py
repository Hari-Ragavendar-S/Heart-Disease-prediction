import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


data = pd.read_csv("heart.csv")


X = data.drop('condition', axis=1)
y = data['condition']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier()
model.fit(X_train, y_train)


joblib.dump(model, 'model.pkl')

print("✅ Model trained and saved as model.pkl")
