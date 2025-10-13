# Heart Disease Prediction using Machine Learning

Predict the likelihood of heart disease using clinical data. The app provides an **on-screen prediction** and a **downloadable PDF medical report**.

---

## Overview

Early detection of heart disease can save lives.  
This project uses **Logistic Regression** to analyze medical features and predict heart disease risk. The web app is built with **Flask + Bootstrap** for responsive, interactive use.

---

## Features

- Predicts heart disease risk (High / Low)  
- Accepts 13 medical parameters  
- Generates personalized **PDF health reports**  
- Responsive **Bootstrap 5** frontend  
- Trained on **UCI Heart Dataset**  
- Deployable on **Vercel / Render / Railway**

---

## Project Structure

```

app.py          # Flask app
predict.py      # Model integration
train_model.py  # Training script
report_generator.py # PDF generator
heart_model.pkl # Saved ML model
heart.csv       # Dataset
templates/      # HTML form
requirements.txt
vercel.json
README.md

````

---

## Tech Stack

- **Frontend:** HTML5, CSS3, Bootstrap 5  
- **Backend:** Flask  
- **ML:** Scikit-Learn, NumPy, Pandas  
- **PDF:** FPDF  

---

## Installation


git clone https://github.com/Hari-Ragavendar-S/Heart-Disease-prediction.git
cd Heart-Disease-prediction
pip install -r requirements.txt
python app.py


Open in browser: `http://127.0.0.1:5000/`

---

## Model Training

* Algorithm: Logistic Regression
* Dataset: heart.csv (UCI)
* Split: 80% train / 20% test
* Accuracy: ~85%
* Saved as: heart_model.pkl

Training Example:

```python
model.fit(X_train, y_train)
pickle.dump(model, open("heart_model.pkl", "wb"))
```

---

## Prediction & PDF Workflow

1. User submits medical details
2. Flask passes inputs to trained model
3. Prediction: `1` → High risk, `0` → Low risk
4. PDF report is generated with patient info, prediction, and summary

---

## Dependencies

```
flask, pandas, numpy, scikit-learn, fpdf
```

---

## Deployment

* Start command: `python app.py`
* Runtime: Python 3.9+
* Compatible with Vercel, Render, Railway

---

## Author

Hari Ragavendar S
[GitHub](https://github.com/Hari-Ragavendar-S) | [Email] (hariragavender54@gmail.com)

---

## Support

If helpful, ⭐ star this repo to support my work.  

If you want, I can also make a **version under 200 lines with badges and a screenshot preview** — perfect for a GitHub portfolio page. Do you want me to do that?
```
