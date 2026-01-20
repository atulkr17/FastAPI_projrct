from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

def register_exception_hendlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )   