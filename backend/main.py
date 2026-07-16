from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile, File
import shutil
import os


from ocr import extract_text
from extractor import (
    extract_cbc_values,
    extract_liver_values,
    extract_diabetes_values,
    extract_thyroid_values
)

from prediction import (
    predict_diabetes,
    predict_thyroid,
    predict_anemia,
    predict_liver
)

# Temporary storage for diabetes values
diabetes_cache = {}

app = FastAPI(
    title="Blood Report Analyzer API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Root Test API
# ==========================

@app.get("/")
def home():

    return {
        "message": "Blood Report Analyzer API is running"
    }



# ==========================
# Diabetes API
# ==========================

class DiabetesInput(BaseModel):

    Chol: float
    Trig: float
    HDL: float
    LDL: float
    VLDL: float
    RBS: float



@app.post("/predict/diabetes")
def diabetes_prediction(data: DiabetesInput):

    result = predict_diabetes(data.dict())

    return {
        "disease": "Diabetes",
        **result
    }


# ==========================
# Thyroid API
# ==========================

class ThyroidInput(BaseModel):

    Age: float
    Sex: int
    On_Thyroxine: int
    On_Antithyroid_Medication: int
    Query_Hypothyroid: int
    Query_Hyperthyroid: int
    Thyroid_Surgery: int
    I131_Treatment: int
    TSH: float
    T3: float
    TT4: float
    T4U: float
    FTI: float



@app.post("/predict/thyroid")
def thyroid_prediction(data: ThyroidInput):

    result = predict_thyroid(
        data.dict()
    )

    return {
    "disease": "Thyroid",
    **result
    }



# ==========================
# Anemia API
# ==========================

class AnemiaInput(BaseModel):

    WBC: float
    RBC: float
    HGB: float
    MCV: float
    MCH: float
    MCHC: float
    PLT: float



@app.post("/predict/anemia")
def anemia_prediction(data: AnemiaInput):

    result = predict_anemia(
        data.dict()
    )

    return {
    "disease": "Anemia",
    **result
    }   



# ==========================
# Liver API
# ==========================

class LiverInput(BaseModel):

    Age: float
    Gender: int
    Total_Bilirubin: float
    Direct_Bilirubin: float
    Alkaline_Phosphotase: float
    ALT: float
    AST: float
    Total_Proteins: float
    Albumin: float
    Albumin_Globulin_Ratio: float



@app.post("/predict/liver")
def liver_prediction(data: LiverInput):

    result = predict_liver(
        data.dict()
    )

    return {
    "disease": "Liver Disease",
    **result
}



@app.post("/upload-report")
def upload_report(file: UploadFile = File(...)):

    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ==========================
    # OCR
    # ==========================

    extracted_text = extract_text(file_path)

    print("\n========== OCR TEXT ==========")
    print(extracted_text)
    print("========== END OCR TEXT ==========\n")

    # ==========================
    # Extraction
    # ==========================

    cbc = extract_cbc_values(extracted_text)
    liver = extract_liver_values(extracted_text)
    diabetes = extract_diabetes_values(extracted_text)
    thyroid = extract_thyroid_values(extracted_text)

    print("\n===== EXTRACTED VALUES =====")
    print("CBC:", cbc)
    print("Liver:", liver)
    print("Diabetes:", diabetes)
    print("Thyroid:", thyroid)
    print("============================\n")

    # ==========================
    # Anemia
    # ==========================

    if cbc["HGB"] is not None:

        result = predict_anemia(cbc)

        return {
            "filename": file.filename,
            "disease": "Anemia",
            **result
        }

    # ==========================
    # Liver Disease
    # ==========================

    if liver["Total_Bilirubin"] is not None:

        result = predict_liver(liver)

        return {
            "filename": file.filename,
            "disease": "Liver Disease",
            **result
        }

    # ==========================
    # Diabetes
    # ==========================

    # Check if this report contains any diabetes values
    has_diabetes_data = any(
        value is not None for value in diabetes.values()
    )

    if has_diabetes_data:

        print(">>> ENTERED DIABETES BLOCK <<<")

        # Save values into cache
        for key, value in diabetes.items():
            if value is not None:
                diabetes_cache[key] = value

        print("Current Report:", diabetes)
        print("Cache:", diabetes_cache)

        required_features = [
            "Chol",
            "Trig",
            "HDL",
            "LDL",
            "VLDL",
            "RBS"
        ]

        missing_features = [
            feature
            for feature in required_features
            if diabetes_cache.get(feature) is None
        ]

        print("Missing:", missing_features)

        # If all values are available → Predict
        if len(missing_features) == 0:

            result = predict_diabetes(diabetes_cache)

            diabetes_cache.clear()

            return {
                "filename": file.filename,
                "disease": "Diabetes",
                **result
            }

        # Otherwise wait for another report
        return {
            "filename": file.filename,
            "message": "Diabetes report detected. Please upload another report containing the missing parameters.",
            "missing_features": missing_features,
            "current_values": diabetes_cache
        }

    # ==========================
    # Thyroid
    # ==========================

    if thyroid["TSH"] is not None:

        return {
            "filename": file.filename,
            "message": "Thyroid report detected.",
            "thyroid": thyroid
        }

    # ==========================
    # Unknown Report
    # ==========================

    return {
        "filename": file.filename,
        "message": "Unable to detect report type."
    }