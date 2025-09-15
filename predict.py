import pickle
import numpy as np

with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)


input_data = [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]

input_array = np.array(input_data).reshape(1, -1)

prediction = model.predict(input_array)
if prediction[0] == 1:
    print("Patient likely has a heart condition.")
else:
    print("Patient is unlikely to have a heart condition.")
