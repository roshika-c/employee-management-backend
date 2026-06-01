from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.employee_exceptions import EmployeeNotFoundException,EmployeeAlreadyExistsException

async def employee_not_found_exception_handler(
        request:Request,
        exc:EmployeeNotFoundException
):
    return JSONResponse(
        status_code=404,
        content= {"message":"Employee not found"}
    )

async def employee_already_exists_exception_handler(
        request:Request,
        exc:EmployeeAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content= {"message":"Employee already Exists"}
    )

