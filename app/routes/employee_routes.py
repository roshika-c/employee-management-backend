from fastapi import APIRouter
from models.employee_models import Employee
router=APIRouter()
employees=[]
@router.post("/add_employee")
def add_employee(employee:Employee):
    for emp in employees:
        if emp["id"]==employee.id:
            return {"message":"Employee already exists"}
    employees.append(employee.model_dump())
    return {"message":"Employee added successfully"}

@router.get("/all_employees")
def get_all_employees():
    return {"employees":employees}

@router.get("/get_emp_by_id/{id}")
def get_employee_by_id(id:int):
    for employee in employees:
        if employee["id"]==id:
            return employee
    return {"message":"Employee not found"}

@router.put("/update_employees/{id}")
def update_emp_by_id(updated_employee:Employee,id:int):
    for index,employee in enumerate(employees):
        if employee["id"]==id:
            employees[index]=updated_employee.model_dump()
            return {"message":"Employee updated successfully"}
    return {"message":"Employee not found"}

@router.delete("/delete_employees_by_id/{id}")
def delete_emp_by_id(id:int):
    for employee in employees:
        if employee["id"]==id:
            employees.remove(employee)
            return {"message":"Employee deleted successfully"}
    return {"message":"Employee not found"}


