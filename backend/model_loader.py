import joblib
import os


# Path to models folder
MODEL_PATH = "../models"


# =========================
# Diabetes Model
# =========================

diabetes_model = joblib.load(
    os.path.join(
        MODEL_PATH,
        "Diabetes_model.pkl"
    )
)

diabetes_features = joblib.load(
    os.path.join(
        MODEL_PATH,
        "diabetes_feature_list.pkl"
    )
)


# =========================
# Thyroid Model
# =========================

thyroid_model = joblib.load(
    os.path.join(
        MODEL_PATH,
        "thyroid_model.pkl"
    )
)

thyroid_encoder = joblib.load(
    os.path.join(
        MODEL_PATH,
        "thyroid_label_encoder.pkl"
    )
)

thyroid_features = joblib.load(
    os.path.join(
        MODEL_PATH,
        "thyroid_features.pkl"
    )
)


# =========================
# Anemia Model
# =========================

anemia_model = joblib.load(
    os.path.join(
        MODEL_PATH,
        "anemia_decision_tree_model.pkl"
    )
)

anemia_features = joblib.load(
    os.path.join(
        MODEL_PATH,
        "anemia_feature_list.pkl"
    )
)


# =========================
# Liver Model
# =========================

liver_model = joblib.load(
    os.path.join(
        MODEL_PATH,
        "liver_disease_model.pkl"
    )
)

liver_features = joblib.load(
    os.path.join(
        MODEL_PATH,
        "liver_feature_names.pkl"
    )
)


print("All ML models loaded successfully")