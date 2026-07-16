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

def extract_gender(text):
    match = re.search(r"Age\s*/\s*Sex\s*:\s*\d+\s*YRS\s*/\s*([MF])", text, re.IGNORECASE)

    if match:
        gender = match.group(1).upper()

        # Use the same encoding as your dataset
        return 1 if gender == "M" else 0

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
        "Age": extract_value(text, [
        r"Age\s*/\s*Sex\s*:\s*(\d+)"
    ]),

    "Gender": extract_gender(text),



            "Total_Bilirubin": extract_value(text, [
        r"SERUM\s*BILIRUBIN\s*\(TOTAL\).*?([\d.]+)",
        r"Total\s*Bilirubin.*?([\d.]+)"
    ]),

            "Direct_Bilirubin": extract_value(text, [
        r"SERUM\s*BILIRUBIN\s*\(DIRECT\).*?([\d.]+)",
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

        "Alkaline_Phosphotase": extract_value(text, [
            r"Alkaline\s*Phosphatase.*?([\d.]+)",
            r"\bALP\b.*?([\d.]+)"
        ]),

        "Albumin": extract_value(text, [
            r"Albumin.*?([\d.]+)"
        ]),

            "Total_Proteins": extract_value(text, [
        r"SERUM\s*PROTEIN.*?([\d.]+)",
        r"Total\s*Protein.*?([\d.]+)"
    ]),
        "Albumin_Globulin_Ratio": extract_value(text, [
        r"A/G\s*RATIO.*?([\d.]+)"
    ])

    }

    return values


# ==========================================================
# Diabetes
# ==========================================================

def extract_diabetes_values(text):

    values = {
        "Chol": extract_value(text, [
            r"Total\s*Cholesterol.*?([\d.]+)",
            r"\bChol\b.*?([\d.]+)"
        ]),

        "Trig": extract_value(text, [
            r"Triglycerides?.*?([\d.]+)",
            r"\bTrig\b.*?([\d.]+)"
        ]),

        "HDL": extract_value(text, [
            r"HDL.*?([\d.]+)"
        ]),

        "LDL": extract_value(text, [
            r"LDL.*?([\d.]+)"
        ]),

        "VLDL": extract_value(text, [
            r"VLDL.*?([\d.]+)"
        ]),

        "RBS": extract_value(text, [
            r"Random\s*Blood\s*Sugar.*?([\d.]+)",
            r"\bRBS\b.*?([\d.]+)",
            r"Blood\s*Sugar.*?([\d.]+)"
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

        "TT4": extract_value(text, [
            r"\bT4\b.*?([\d.]+)"
        ])
    }

    return values