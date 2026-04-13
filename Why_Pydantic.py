# Import BaseModel and EmailStr from pydantic for data validation and email validation
# Import List, Dict, and Optional from typing for type hints
from typing import List, Dict, Optional
from pydantic import BaseModel, EmailStr

# Define a Patient model using Pydantic's BaseModel
# Pydantic will validate the values and convert types when possible
class Patient(BaseModel):
    # Required string field for the patient's name
    name: str

    # EmailStr is a Pydantic type that validates email address format
    email: EmailStr

    # Required integer field for the patient's age
    age: int

    # Required float field for the patient's weight
    weight: float

    # Optional boolean field with a default value of False
    married: bool = False

    # Optional list of allergy names; default is None when no allergies are provided
    allergies: Optional[List[str]] = None

    # Required dictionary for contact details (phone, email, etc.)
    contact_details: Dict[str, str]


# Function to simulate inserting patient data
# It accepts a validated Patient model instance and prints selected fields
def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Patient data inserted successfully")


# Function to simulate updating patient data
# It accepts the same Patient model instance and prints selected fields
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print("Patient data updated successfully")


# Example patient data as a dictionary
# Pydantic will convert the string values to the correct types automatically
patient_info = {
    "name": "Shubham Madane",
    "email": "shubhammadane003@gmail.com",
    "age": "25",  # This is a string, but Pydantic will convert it to int
    "weight": "84.5",  # This is a string, but Pydantic will convert it to float
    "married": "False",  # This string will be converted to boolean
    "allergies": ["Pizza", "Burger", "Chicken"],
    "contact_details": {
        "email": "shubhammadane003@gmail.com",
        "phone": "8055113546"
    }
}


# Create a Patient instance by unpacking the dictionary into the model
# This performs validation and type conversion before creating the object
patient1 = Patient(**patient_info)

# Use the validated Patient instance in the insert and update functions
insert_patient_data(patient1)
update_patient_data(patient1)
