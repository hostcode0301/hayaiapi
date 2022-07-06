from asyncio import constants
from typing import Union
from fastapi import Request

from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from fastapi.openapi.utils import validation_error_response_definition
from fastapi.openapi.constants import REF_PREFIX
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from starlette.responses import JSONResponse

async def http422_error_handler(
    _: Request,
    exc: Union[RequestValidationError, ValidationError],
) -> JSONResponse:
    return JSONResponse(
        {"errors": exc.errors()},
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
    )

validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {
            "$ref": "{0}ValidationError".format(REF_PREFIX)
        },
    },
}