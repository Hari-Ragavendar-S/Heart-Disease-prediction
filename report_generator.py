from reportlab.pdfgen import canvas

def create_pdf_report(name, result):
    filename = f"{name}_report.pdf"
    c = canvas.Canvas(f"static/{filename}")
    c.setFont("Helvetica", 16)
    c.drawString(100, 750, "Heart Disease Prediction Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, f"Patient Name: {name}")
    c.drawString(100, 680, f"Prediction Result: {result}")
    c.save()
    return filename
