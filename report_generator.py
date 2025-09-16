from reportlab.pdfgen import canvas
import pandas as pd

# Load feature names from dataset (excluding target column)
data = pd.read_csv("heart.csv")
feature_names = data.drop("condition", axis=1).columns.tolist()

def create_pdf_report(name, result, patient_data=None):
    filename = f"{name}_report.pdf"
    c = canvas.Canvas(f"static/{filename}")
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 750, "Heart Disease Prediction Report")
    
    # Patient Info
    c.setFont("Helvetica", 12)
    c.drawString(100, 720, f"Patient Name: {name}")
    c.drawString(100, 700, f"Prediction Result: {result}")
    
    # List features (if patient_data provided)
    if patient_data is not None:
        y = 670
        c.setFont("Helvetica", 11)
        c.drawString(100, y, "Patient Health Data:")
        y -= 20
        for feature, value in zip(feature_names, patient_data):
            c.drawString(120, y, f"{feature}: {value}")
            y -= 18
            if y < 50:  # New page if content overflows
                c.showPage()
                c.setFont("Helvetica", 11)
                y = 750
    
    # Save PDF
    c.save()
    return filename
