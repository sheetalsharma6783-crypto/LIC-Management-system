from pydantic import BaseModel

class Employee(BaseModel):
    emp_id: int
    name: str
    salary: float
    department: str
employee = Employee(
    emp_id=101,
    name="Rahul",
    salary="Fifty Thousand",
    department="IT"
)

print(employee)