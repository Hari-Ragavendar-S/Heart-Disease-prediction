import pickle
import numpy as np
# Load trained model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)
# Sample input (replace these values as needed)
# Order: ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
input_data = [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
# Convert to 2D array
input_array = np.array(input_data).reshape(1, -1)
# Make prediction
prediction = model.predict(input_array)
if prediction[0] == 1:
    print("Patient likely has a heart condition.")
else:
    print("Patient is unlikely to have a heart condition.")
