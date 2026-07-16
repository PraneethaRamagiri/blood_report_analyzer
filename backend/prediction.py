from explanation import (
    explain_diabetes,
    explain_thyroid,
    explain_anemia,
    explain_liver
)
import pandas as pd

from model_loader import (
    diabetes_model,
    diabetes_features,

    thyroid_model,
    thyroid_features,
    thyroid_encoder,

    anemia_model,
    anemia_features,

    liver_model,
    liver_features
)


# ==========================
# Diabetes Prediction
# ==========================

def predict_diabetes(data):

    input_data = pd.DataFrame(
        [data]
    )

    input_data = input_data[
        diabetes_features
    ]

    prediction = diabetes_model.predict(
        input_data
    )

    prediction_label = "Diabetes" if int(prediction[0]) == 1 else "No Diabetes"

    explanation = explain_diabetes(data)

    return {
    "prediction": prediction_label,
    "explanation": explanation["explanation"],
    "suggestions": explanation["suggestions"]
    }


# ==========================
# Thyroid Prediction
# ==========================

def predict_thyroid(data):

    input_data = pd.DataFrame(
        [data]
    )

    input_data = input_data[
        thyroid_features
    ]

    prediction = thyroid_model.predict(
        input_data
    )

    result = thyroid_encoder.inverse_transform(
        prediction
    )

    explanation = explain_thyroid(data)

    return {
        "prediction": result[0],
        "explanation": explanation["explanation"],
        "suggestions": explanation["suggestions"]
    }


# ==========================
# Anemia Prediction
# ==========================

def predict_anemia(data):

    input_data = pd.DataFrame(
        [data]
    )

    input_data = input_data[
        anemia_features
    ]

    prediction = anemia_model.predict(
        input_data
    )

    # Anemia model returns text label
    explanation = explain_anemia(data)

    return {
        "prediction": prediction[0],
        "explanation": explanation["explanation"],
        "suggestions": explanation["suggestions"]
    }


# ==========================
# Liver Disease Prediction
# ==========================

def predict_liver(data):

    input_data = pd.DataFrame(
        [data]
    )

    input_data = input_data[
        liver_features
    ]

    prediction = liver_model.predict(
        input_data
    )
    prediction_label = "Liver Disease" if int(prediction[0]) == 1 else "No Liver Disease"

    explanation = explain_liver(data)

    return {
        "prediction": prediction_label,
        "explanation": explanation["explanation"],
        "suggestions": explanation["suggestions"]
    }