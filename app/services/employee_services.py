from utils.logger import logger
from exceptions.employee_exceptions import EmployeeNotFoundException,EmployeeAlreadyExistsException
employees=[]
def add_employee(employee):
    for emp in employees:
        if emp["id"]==employee.id:
            logger.warning(f"Employee with {employee.id} already exists")
            raise EmployeeAlreadyExistsException()
    employees.append(employee.model_dump())
    logger.info(f"Employee with {employee.id} added successfully")
    return {"message":"Employee added successfully"}

def get_all_employees():
    logger.info("Employees found")
    return {"employees":employees}

def get_employee_by_id(id):
    for employee in employees:
        if employee["id"]==id:
            logger.info(f"Employee with {id} found")
            return employee
    logger.error(f"Employee with {id} not found")
    raise EmployeeNotFoundException()
def update_emp_by_id(updated_employee,id):
    for index,employee in enumerate(employees):
        if employee["id"]==id:
            employees[index]=updated_employee.model_dump()
            logger.info(f"Employee with {id} updated successfully")
            return {"message":"Employee updated successfully"}
    logger.error(f"Employee with {id} not found")
    raise EmployeeNotFoundException()
def delete_emp_by_id(id):
    for employee in employees:
        if employee["id"]==id:
            employees.remove(employee)
            logger.info(f"Employee with id:{id} deleted successfully")
            return {"message":"Employee deleted successfully"}
    logger.error(f"Employee with {id} not found")
    raise EmployeeNotFoundException()