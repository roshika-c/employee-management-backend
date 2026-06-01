from exceptions.employee_exceptions import EmployeeNotFoundException,EmployeeAlreadyExistsException
employees=[]
def add_employee(employee):
    for emp in employees:
        if emp["id"]==employee.id:
            raise EmployeeAlreadyExistsException
    employees.append(employee.model_dump())
    return {"message":"Employee added successfully"}

def get_all_employees():
    return {"employees":employees}

def get_employee_by_id(id):
    for employee in employees:
        if employee["id"]==id:
            return employee
    raise EmployeeNotFoundException()
def update_emp_by_id(updated_employee,id):
    for index,employee in enumerate(employees):
        if employee["id"]==id:
            employees[index]=updated_employee.model_dump()
            return {"message":"Employee updated successfully"}
    raise EmployeeNotFoundException
def delete_emp_by_id(id):
    for employee in employees:
        if employee["id"]==id:
            employees.remove(employee)
            return {"message":"Employee deleted successfully"}
    raise EmployeeNotFoundException