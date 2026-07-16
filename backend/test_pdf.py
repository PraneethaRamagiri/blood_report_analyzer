import pdfplumber

with pdfplumber.open("sample_report.pdf") as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

    print(text)