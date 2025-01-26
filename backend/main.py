from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, NoResultFound
from api.routers import all_routers
from utilities.logging_utils import logger


app = FastAPI(title="SeekHub")

for router in all_routers:
    app.include_router(router)


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    error_message = str(exc.orig) if exc.orig else "Integrity error occurred."
    response_content = {
        "error": "A database integrity error occurred.",
        "detail": error_message,
        "path": request.url.path,
    }
    if "unique constraint" in error_message:
        response_content["detail"] = "A record with this unique field already exists."
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=response_content,
    )


@app.exception_handler(NoResultFound)
async def no_result_found_error_handler(request: Request, exc: NoResultFound):
    response_content = {
        "error": "The requested resource was not found.",
        "detail": str(exc),
        "path": request.url.path,
    }
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=response_content,
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    response_content = {
        "error": "Internal Server Error",
        "detail": "An unexpected error occurred. Please try again later.",
        "path": request.url.path,
    }
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response_content,
    )
