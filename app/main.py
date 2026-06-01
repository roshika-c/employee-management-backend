from fastapi import FastAPI
from routes.employee_routes import router
from exceptions.employee_exceptions import EmployeeNotFoundException,EmployeeAlreadyExistsException
from handlers.exception_handler import employee_not_found_exception_handler,employee_already_exists_exception_handler
app=FastAPI()
app.include_router(router)
app.add_exception_handler(
    EmployeeNotFoundException,
    employee_not_found_exception_handler
    )
app.add_exception_handler(
    EmployeeAlreadyExistsException,
    employee_already_exists_exception_handler
    )