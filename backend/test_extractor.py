from ocr import extract_text
from extractor import extract_cbc_values
from validator import validate_cbc

text = extract_text("sample_report.pdf")

values = extract_cbc_values(text)

print("\nExtracted Values")
print(values)

valid, errors = validate_cbc(values)

print("\nValidation")

print(valid)

for error in errors:
    print("-", error)