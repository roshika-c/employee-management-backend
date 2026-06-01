employees=[]
def add_employee(employee):
    for emp in employees:
        if emp["id"]==employee.id:
            return {"message":"Employee already exists"}
    employees.append(employee.model_dump())
    return {"message":"Employee added successfully"}
def get_all_employees():
    return {"employees":employees}
def get_employee_by_id(id):
    for employee in employees:
        if employee["id"]==id:
            return employee
    return {"message":"Employee not found"}
def update_emp_by_id(updated_employee,id):
    for index,employee in enumerate(employees):
        if employee["id"]==id:
            employees[index]=updated_employee.model_dump()
            return {"message":"Employee updated successfully"}
    return {"message":"Employee not found"}
def delete_emp_by_id(id):
    for employee in employees:
        if employee["id"]==id:
            employees.remove(employee)
            return {"message":"Employee deleted successfully"}
    return {"message":"Employee not found"}