def explain_anemia(data):
    explanations = []
    suggestions = []

    hemoglobin = data.get("HGB")
    mcv = data.get("MCV")
    mch = data.get("MCH")
    mchc = data.get("MCHC")

    if hemoglobin is not None and hemoglobin < 12:
        explanations.append(
            "Hemoglobin level is lower than normal. This may indicate reduced oxygen-carrying capacity of the blood."
        )

        suggestions.append(
            "Include iron-rich foods such as leafy vegetables, beans, and lentils in your diet."
        )

    if mcv is not None and mcv < 80:
        explanations.append(
            "MCV level is lower than normal. This indicates that the red blood cells are smaller than usual."
        )

        suggestions.append(
            "Consider consuming foods rich in iron and vitamin B12."
        )

    if mch is not None and mch < 27:
        explanations.append(
            "MCH level is low. This means the red blood cells may contain less hemoglobin than normal."
        )

    if mchc is not None and mchc < 32:
        explanations.append(
            "MCHC level is lower than normal. This may indicate reduced hemoglobin concentration in red blood cells."
        )

    if explanations:
        suggestions.append(
            "Consider consulting a healthcare professional for further evaluation."
        )

    return {
        "explanation": explanations,
        "suggestions": suggestions
    }







def explain_liver(data):
    explanations = []
    suggestions = []

    total_bilirubin = data.get("Total_Bilirubin")
    alt = data.get("ALT")
    ast = data.get("AST")
    albumin = data.get("Albumin")

    if total_bilirubin is not None and total_bilirubin > 1.2:
        explanations.append(
            "Total Bilirubin is elevated. This may indicate difficulty in processing bilirubin by the liver."
        )

    if alt is not None and alt > 40:
        explanations.append(
            "ALT level is higher than normal. This can indicate liver cell injury."
        )

        suggestions.append(
            "Maintain a balanced diet and avoid unnecessary substances that may stress the liver."
        )

    if ast is not None and ast > 40:
        explanations.append(
            "AST level is elevated. This may indicate liver or tissue damage."
        )

    if albumin is not None and albumin < 3.5:
        explanations.append(
            "Albumin level is low. Reduced albumin can be associated with decreased liver protein production."
        )

        suggestions.append(
            "Include adequate protein and nutrient-rich foods in your diet, based on professional dietary advice."
        )

    if explanations:
        suggestions.append(
            "Consider consulting a healthcare professional for further liver evaluation."
        )

    return {
        "explanation": explanations,
        "suggestions": suggestions
    }



def explain_thyroid(data):
    explanations = []
    suggestions = []

    tsh = data.get("TSH")
    t3 = data.get("T3")
    tt4 = data.get("TT4")
    t4u = data.get("T4U")
    fti = data.get("FTI")

    if tsh is not None and tsh > 4.5:
        explanations.append(
            "TSH level is elevated. This may indicate reduced thyroid activity."
        )

    if t3 is not None and t3 < 1.0:
        explanations.append(
            "T3 level is lower than normal. This may be associated with reduced thyroid hormone activity."
        )

    if tt4 is not None and tt4 < 77:
        explanations.append(
            "TT4 level is lower than normal. This may indicate reduced thyroid hormone levels."
        )

    if t4u is not None and t4u < 0.8:
        explanations.append(
            "T4U level is lower than the expected range."
        )

    if fti is not None and fti < 65:
        explanations.append(
            "FTI level is lower than normal. This may indicate reduced thyroid hormone availability."
        )

    if explanations:
        suggestions.append(
            "Monitor thyroid hormone levels regularly."
        )

        suggestions.append(
            "Consider consulting a healthcare professional for further thyroid evaluation."
        )

    return {
        "explanation": explanations,
        "suggestions": suggestions
    }


def explain_diabetes(data):
    explanations = []
    suggestions = []

    chol = data.get("Chol")
    trig = data.get("Trig")
    hdl = data.get("HDL")
    ldl = data.get("LDL")
    vldl = data.get("VLDL")
    rbs = data.get("RBS")

    if rbs is not None and rbs >= 200:
        explanations.append(
            "Random blood sugar level is high. This may indicate abnormal blood glucose regulation."
        )

        suggestions.append(
            "Monitor blood glucose levels regularly."
        )

    if trig is not None and trig >= 150:
        explanations.append(
            "Triglyceride level is elevated. High triglyceride levels may be associated with metabolic health risks."
        )

        suggestions.append(
            "Limit foods high in added sugars and unhealthy fats."
        )

    if hdl is not None and hdl < 40:
        explanations.append(
            "HDL cholesterol level is low. HDL is commonly known as good cholesterol."
        )

        suggestions.append(
            "Regular physical activity may help support healthy HDL cholesterol levels."
        )

    if ldl is not None and ldl >= 130:
        explanations.append(
            "LDL cholesterol level is elevated. High LDL levels may increase cardiovascular health risk."
        )

        suggestions.append(
            "Choose foods lower in saturated and trans fats."
        )

    if chol is not None and chol >= 200:
        explanations.append(
            "Total cholesterol level is elevated."
        )

    if explanations:
        suggestions.append(
            "Consider consulting a healthcare professional for further evaluation."
        )

    return {
        "explanation": explanations,
        "suggestions": suggestions
    }

def generate_explanation(disease, values):

    disease = disease.lower()

    if disease == "anemia":
        return explain_anemia(values)

    elif disease == "diabetes":
        return explain_diabetes(values)

    elif disease == "thyroid":
        return explain_thyroid(values)

    elif disease == "liver":
        return explain_liver(values)

    else:
        return {
            "explanation": [],
            "suggestions": []
        }

