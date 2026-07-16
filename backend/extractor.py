import re


def extract_value(text, patterns):
    """
    Search for the first matching parameter in OCR text and return its numeric value.
    """
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                continue
    return None


# ==========================================================
# CBC (Anemia)
# ==========================================================

def extract_cbc_values(text):
    """
    Extract CBC values from OCR text.
    Returns dictionary with model feature names.
    """

    values = {
        "HGB": extract_value(text, [
            r"Hemoglobin.*?([\d.]+)",
            r"\bHb\b.*?([\d.]+)"
        ]),

        "RBC": extract_value(text, [
            r"Total\s*RBC\s*Count.*?([\d.]+)",
            r"\bRBC\b.*?([\d.]+)"
        ]),

        "WBC": extract_value(text, [
            r"Total\s*WBC\s*Count.*?([\d.]+)",
            r"\bWBC\b.*?([\d.]+)"
        ]),

        "MCV": extract_value(text, [
            r"Mean\s*Corpuscular\s*Volume.*?([\d.]+)",
            r"\bMCV\b.*?([\d.]+)"
        ]),

        "MCH": extract_value(text, [
            r"Mean\s*Corpuscular\s*Hemoglobin.*?([\d.]+)",
            r"\bMCH\b.*?([\d.]+)"
        ]),

        "MCHC": extract_value(text, [
            r"Mean\s*Corpuscular\s*Hemoglobin\s*Concentration.*?([\d.]+)",
            r"\bMCHC\b.*?([\d.]+)"
        ]),

        "PLT": extract_value(text, [
            r"Platelet\s*Count.*?([\d.]+)",
            r"\bPlatelets?\b.*?([\d.]+)"
        ])
    }

    return values


# ==========================================================
# Liver Function Test (LFT)
# ==========================================================

def extract_liver_values(text):

    values = {
        "TB": extract_value(text, [
            r"Total\s*Bilirubin.*?([\d.]+)"
        ]),

        "DB": extract_value(text, [
            r"Direct\s*Bilirubin.*?([\d.]+)"
        ]),

        "ALT": extract_value(text, [
            r"ALT.*?([\d.]+)",
            r"SGPT.*?([\d.]+)"
        ]),

        "AST": extract_value(text, [
            r"AST.*?([\d.]+)",
            r"SGOT.*?([\d.]+)"
        ]),

        "ALP": extract_value(text, [
            r"Alkaline\s*Phosphatase.*?([\d.]+)",
            r"\bALP\b.*?([\d.]+)"
        ]),

        "Albumin": extract_value(text, [
            r"Albumin.*?([\d.]+)"
        ]),

        "TP": extract_value(text, [
            r"Total\s*Protein.*?([\d.]+)"
        ])
    }

    return values


# ==========================================================
# Diabetes
# ==========================================================

def extract_diabetes_values(text):

    values = {
        "Glucose": extract_value(text, [
            r"Glucose.*?([\d.]+)",
            r"Blood\s*Sugar.*?([\d.]+)",
            r"Fasting\s*Blood\s*Sugar.*?([\d.]+)"
        ]),

        "HbA1c": extract_value(text, [
            r"HbA1c.*?([\d.]+)"
        ])
    }

    return values


# ==========================================================
# Thyroid
# ==========================================================

def extract_thyroid_values(text):

    values = {
        "TSH": extract_value(text, [
            r"TSH.*?([\d.]+)"
        ]),

        "T3": extract_value(text, [
            r"\bT3\b.*?([\d.]+)"
        ]),

        "T4": extract_value(text, [
            r"\bT4\b.*?([\d.]+)"
        ])
    }

    return values