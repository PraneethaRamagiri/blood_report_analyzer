def validate_cbc(values):
    """
    Validate extracted CBC values.

    Returns:
        valid (bool)
        errors (list)
    """

    errors = []

    hgb = values.get("HGB")
    rbc = values.get("RBC")
    wbc = values.get("WBC")
    plt = values.get("PLT")
    mcv = values.get("MCV")
    mch = values.get("MCH")
    mchc = values.get("MCHC")

    # -------------------------
    # Missing values
    # -------------------------

    for key, value in values.items():
        if value is None:
            errors.append(f"{key} not found")

    # -------------------------
    # Range validation
    # -------------------------

    if hgb is not None and not (3 <= hgb <= 22):
        errors.append(f"Invalid Hemoglobin: {hgb}")

    if rbc is not None and not (2 <= rbc <= 8):
        errors.append(f"Invalid RBC Count: {rbc}")

    if wbc is not None and not (1000 <= wbc <= 50000):
        errors.append(f"Suspicious WBC Count: {wbc}")

    if plt is not None and not (50000 <= plt <= 1000000):
        errors.append(f"Suspicious Platelet Count: {plt}")

    if mcv is not None and not (50 <= mcv <= 130):
        errors.append(f"Invalid MCV: {mcv}")

    if mch is not None and not (10 <= mch <= 45):
        errors.append(f"Invalid MCH: {mch}")

    if mchc is not None and not (20 <= mchc <= 45):
        errors.append(f"Invalid MCHC: {mchc}")

    return len(errors) == 0, errors