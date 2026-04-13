from typing import List, Dict, Optional
from pydantic import BaseModel, EmailStr

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Patient data inserted successfully")


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data updated successfully")


# ✅ Clean input (correct data types)
patient_info = {
    "name": "Shubham Madane",
    "email": "shubhammadane003@gmail.com",
    "age": 25,
    "weight": 84.5,
    "married": False,
        # optional but added
    "contact_details": {
        "email": "shubhammadane003@gmail.com",
        "phone": "8055113546"
    }
}


patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)