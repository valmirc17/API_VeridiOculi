from fpdf import FPDF

def generate_pdf(analyses):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for analysis in analyses:
        pdf.cell(200, 10, txt=f"Species: {analysis['species']}, Location: {analysis['location']}", ln=True)
    file_path = "/tmp/report.pdf"
    pdf.output(file_path)
    return file_path
