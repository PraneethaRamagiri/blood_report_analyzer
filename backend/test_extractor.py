from ocr import extract_text
from extractor import extract_cbc_values

text = extract_text("sample_report.pdf")

print(text)

print("\nExtracted CBC Values:")
print(extract_cbc_values(text))