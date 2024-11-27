from app.models import Report
from app.utils.pdfGenerator import generate_pdf
from app.utils.s3Utils import upload_to_s3

def generate_report(user_id, analyses):
    pdf_file = generate_pdf(analyses)
    url = upload_to_s3(pdf_file)
    report = {"user_id": user_id, "url": url}
    Report.insert_report(report)
    return report

def get_user_reports(user_id):
    return Report.find_by_user(user_id)
