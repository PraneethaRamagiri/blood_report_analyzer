from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from prediction import (
    predict_diabetes,
    predict_thyroid,
    predict_anemia,
    predict_liver
)


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

    result = predict_diabetes(
        data.dict()
    )

    return {
        "disease": "Diabetes",
        "prediction": int(result)
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
        "prediction": result
    
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
        "prediction": result
    
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
        "prediction": int(result)
    }