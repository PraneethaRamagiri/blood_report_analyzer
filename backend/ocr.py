import os
import pdfplumber
import easyocr
import fitz
import cv2
import numpy as np

# Initialize EasyOCR reader once
reader = easyocr.Reader(['en'])


# ==========================
# Extract text from PDF
# ==========================

def extract_text_from_pdf(file_path):

    text = ""

    # Try extracting text directly
    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    # If text looks good, return it
    if len(text) > 300:
        print("✅ Extracted text using pdfplumber")
        return text

    print("⚠ Falling back to OCR...")

    doc = fitz.open(file_path)

    text = ""

    for page in doc:

        pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))

        img = np.frombuffer(pix.samples, dtype=np.uint8)

        img = img.reshape(pix.height, pix.width, pix.n)

        if pix.n == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)

        result = reader.readtext(img)

        for item in result:
            text += item[1] + "\n"

    return text


# ==========================
# Extract text from Image
# ==========================

def extract_text_from_image(file_path):

    result = reader.readtext(file_path)

    text = ""

    for item in result:
        text += item[1] + "\n"

    return text


# ==========================
# Auto Detect File Type
# ==========================

def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)

    else:
        raise ValueError("Unsupported file format.")
    

if __name__ == "__main__":

    file_path = "sample_report.pdf"   # Replace with your file

    text = extract_text(file_path)

    print(text)