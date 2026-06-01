from fastapi import APIRouter
from models.employee_models import Employee
from services import employee_services
router=APIRouter()

@router.post("/add_employee")
def add_employee(employee:Employee):
    return employee_services.add_employee(employee)

@router.get("/all_employees")
def get_all_employees():
    return employee_services.get_all_employees()

@router.get("/get_emp_by_id/{id}")
def get_employee_by_id(id:int):
    return employee_services.get_employee_by_id(id)

@router.put("/update_employees/{id}")
def update_emp_by_id(updated_employee:Employee,id:int):
    return employee_services.update_emp_by_id(updated_employee,id)
@router.delete("/delete_employees_by_id/{id}")
def delete_emp_by_id(id:int):
    return employee_services.delete_emp_by_id(id)


