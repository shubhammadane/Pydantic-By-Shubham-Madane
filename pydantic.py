# Example 1: simple function without type hints
# This function accepts any values for name and age and prints them.
def insert_patient_data(name,age):
    print(name)
    print(age)
    print("Patient data inserted successfully")

insert_patient_data("Shubham Madane", "Twenty Five")

print("\n")

# Example 2: function with type hints
# Type hints are declared, but Python does not enforce them at runtime by default.
def insert_patient_data(name:str,age:int):
    print(name)
    print(age)
    print("Patient data inserted successfully") 
insert_patient_data("Shubham Madane", "Twenty Five")

print("\n")

# Example 3: function with manual runtime type checking
# This function checks that name is a string and age is an integer.
# If the types are incorrect, it raises a TypeError.
def update_patient_data(name:str,age:int):
    if type(name)== str and type(age)==int:
       print(name)
       print(age)
       print("Updated patient data successfully In database")
    else:
        raise TypeError("Invalid data type for name or age. Name should be a string and age should be an integer.")
update_patient_data("Shubham Madane", "Twenty Five")