from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Patients(BaseModel):
    patient_name: str
    patient_id: int
    patient_age: int
    is_patient: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"PatientManagementSystem": "Welcome"}


@app.get("/patients/")
def read_all_patients(patient_id: int, patient_name:str):
    return {
        "patient_id": patient_id
    }

@app.post("/patients/")
def create_patients(patient_id: int, patient_name:str,patient_age:int):
    return {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "patient_age": patient_age, 
    }


@app.get("/patients/{patient_id}")
def read_patients(patient_id: int, q: Union[str, None] = None):
    return {"patient_id": patient_id, "q": q}


@app.put("/patients/{patient_id}")
def update_patients(patient_id: int, patient_name:str,patient_age:int, patient: Patients):
    return {"patient_name": patient.patient_name, "patient_id": patient_id}