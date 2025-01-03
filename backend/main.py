from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError, NoResultFound
from api.routers import all_routers


app = FastAPI(title="SeekHub")

for router in all_routers:
    app.include_router(router)


@app.exception_handler(IntegrityError)
async def integrity_error_handler(request: Request, exc: IntegrityError):
    error_message = str(exc.orig) if exc.orig else "Integrity error occurred."
    response_content = {
        "detail": "A database integrity error occurred.",
        "error": error_message,
        "path": request.url.path
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
        "detail": "The requested resource was not found.",
        "error": str(exc),
        "path": request.url.path
    }
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=response_content,
    )
