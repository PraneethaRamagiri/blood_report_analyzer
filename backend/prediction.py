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

    return prediction[0]


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

    return result[0]


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
    return prediction[0]


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

    return prediction[0]