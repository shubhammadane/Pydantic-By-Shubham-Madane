# 📦 Pydantic - Data Validation in Python

## 🚀 Overview

**Pydantic** is a Python library used for **data validation and parsing** using Python type hints.
It ensures that the data you work with is correct, structured, and safe.

It is widely used with modern frameworks like FastAPI to build robust APIs.

---

## 🎯 Why Use Pydantic?

* ✅ Automatic data validation
* 🔄 Type conversion (parsing)
* ⚡ High performance
* 🧹 Cleaner and readable code
* 📦 Easy JSON handling
* 🚀 Perfect for API development

---

## ⚙️ Installation

```bash
pip install pydantic
```

---

## 🧠 Basic Example

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

patient = Patient(name="Shubham", age="25")

print(patient)
```

### ✅ Output

```
name='Shubham' age=25
```

👉 Pydantic automatically converts `"25"` (string) → `25` (integer)

---

## ❌ Invalid Data Example

```python
Patient(name="Shubham", age="Twenty Five")
```

### ❌ Output

```
ValidationError: value is not a valid integer
```

---

## 🔍 Key Features

### 1. Data Validation

Ensures correct data types at runtime.

### 2. Type Parsing

Automatically converts compatible types.

### 3. Detailed Errors

Provides clear and structured error messages.

### 4. JSON Support

Easily convert models to JSON format.

```python
patient.json()
```

---

## 🔗 Use with FastAPI

Pydantic is the backbone of FastAPI:

* Request validation
* Response formatting
* Auto API documentation

---

## 📊 Comparison

| Feature         | Normal Python | Pydantic    |
| --------------- | ------------- | ----------- |
| Type Checking   | ❌ No          | ✅ Yes       |
| Auto Conversion | ❌ No          | ✅ Yes       |
| Error Handling  | ❌ Manual      | ✅ Automatic |
| Code Simplicity | ❌ Low         | ✅ High      |

---

## 🧩 When to Use Pydantic?

* Building APIs
* Handling user input
* Working with JSON data
* Data validation in projects

---

## 🏁 Conclusion

Pydantic makes Python applications **more reliable, maintainable, and error-free** by ensuring proper data validation and structure.

---

## 📌 One-Line Summary

👉 *Pydantic is used for automatic data validation and parsing using Python type hints.*

---
