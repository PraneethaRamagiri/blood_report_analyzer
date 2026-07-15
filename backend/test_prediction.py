from prediction import (
    predict_diabetes,
    predict_thyroid,
    predict_anemia,
    predict_liver
)


# ==========================
# Diabetes Test
# ==========================

diabetes_data = {
    "Chol": 180,
    "Trig": 150,
    "HDL": 40,
    "LDL": 110,
    "VLDL": 30,
    "RBS": 170
}


diabetes_result = predict_diabetes(
    diabetes_data
)

print(
    "Diabetes Prediction:",
    diabetes_result
)



# ==========================
# Thyroid Test
# ==========================

thyroid_data = {

    "Age": 45,
    "Sex": 0,
    "On_Thyroxine": 0,
    "On_Antithyroid_Medication": 0,
    "Query_Hypothyroid": 1,
    "Query_Hyperthyroid": 0,
    "Thyroid_Surgery": 0,
    "I131_Treatment": 0,
    "TSH": 8.5,
    "T3": 0.8,
    "TT4": 70,
    "T4U": 0.9,
    "FTI": 78

}


thyroid_result = predict_thyroid(
    thyroid_data
)

print(
    "Thyroid Prediction:",
    thyroid_result
)


# ==========================
# Anemia Test
# ==========================

anemia_data = {

    "WBC": 7.2,
    "RBC": 3.97,
    "HGB": 9.0,
    "MCV": 77.0,
    "MCH": 22.6,
    "MCHC": 30.0,
    "PLT": 170

}


anemia_result = predict_anemia(
    anemia_data
)


print(
    "Anemia Prediction:",
    anemia_result
)


# ==========================
# Liver Test
# ==========================

liver_data = {

    "Age": 45,
    "Gender": 1,
    "Total_Bilirubin": 1.8,
    "Direct_Bilirubin": 0.6,
    "Alkaline_Phosphotase": 250,
    "ALT": 80,
    "AST": 70,
    "Total_Proteins": 6.5,
    "Albumin": 3.0,
    "Albumin_Globulin_Ratio": 0.8

}


liver_result = predict_liver(
    liver_data
)

print(
    "Liver Prediction:",
    liver_result
)