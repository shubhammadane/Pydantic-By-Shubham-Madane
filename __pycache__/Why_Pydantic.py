# Import BaseModel from pydantic for creating data models with validation
from pydantic import BaseModel

# Define a Patient model with name (string) and age (integer) fields
class Patient(BaseModel):
    name: str
    age: int

# Function to insert patient data - prints patient info and success message
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data inserted successfully")

# Function to update patient data - prints patient info and success message
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data updated successfully")

# Sample patient data as a dictionary
patient_info = {
    "name": "Shubham Madane",
    "age": 25
}

# Create a Patient instance by unpacking the dictionary (validates data types)
patient1 = Patient(**patient_info)

# Call insert function with the patient instance
insert_patient_data(patient1)

# Call update function with the patient instance
update_patient_data(patient1)