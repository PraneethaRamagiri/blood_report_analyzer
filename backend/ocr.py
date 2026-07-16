import os
import pdfplumber
import easyocr
import cv2

# Initialize EasyOCR reader once
reader = easyocr.Reader(['en'])


# ==========================
# Extract text from PDF
# ==========================

def extract_text_from_pdf(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


# ==========================
# Extract text from Image
# ==========================



def extract_text_from_image(file_path):

    image = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Enlarge image (improves OCR)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # Threshold
    _, thresh = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    result = reader.readtext(thresh)

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