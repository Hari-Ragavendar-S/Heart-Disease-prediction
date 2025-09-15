from flask import Flask, render_template, request, send_file
import numpy as np
import joblib
from fpdf import FPDF

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    name = request.form['name']
    features = [float(request.form[f]) for f in [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]]
    prediction = model.predict([np.array(features)])
    result = 'likely to have a heart condition.' if prediction[0] == 1 else 'unlikely to have a heart condition.'

   
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Heart Disease Prediction Report", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    for i, val in enumerate(features):
        pdf.cell(200, 10, txt=f"Feature {i+1}: {val}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Prediction: The patient is {result}", ln=True)
    pdf_path = f"{name.replace(' ', '_')}_report.pdf"
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
