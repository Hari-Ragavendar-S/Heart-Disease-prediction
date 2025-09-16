import pickle
import numpy as np
import pandas as pd
from report_generator import create_pdf_report  # Import your PDF generator

# Load model
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load feature names from dataset
data = pd.read_csv("heart.csv")
feature_names = data.drop("condition", axis=1).columns.tolist()

# Example input (must match dataset order)
input_data = [63, 1, 3, 145, 233, 1, 0, 123, 0, 2.0, 1, 1, 1]
input_array = np.array(input_data).reshape(1, -1)

# Prediction
prediction = model.predict(input_array)
probability = model.predict_proba(input_array)[0][1]

# Result message
if prediction[0] == 1:
    result = "The patient is likely to have a heart condition."
else:
    result = "The patient is unlikely to have a heart condition."

# Print results in console
print("=== Patient Data ===")
for feature, value in zip(feature_names, input_data):
    print(f"{feature}: {value}")

print("\nPrediction:", result)
print(f"Confidence: {probability:.2f}")

# Generate PDF Report
patient_name = "Ravi Kumar"  # Example name (can take input dynamically)
report_file = create_pdf_report(patient_name, result, input_data)
print(f"\nReport saved as: static/{report_file}")
