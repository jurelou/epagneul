from epagneul.api.events import start_app_handler, stop_app_handler
from epagneul.api.errors.http_error import http_error_handler
from epagneul.api.errors.validation_error import http_422_error
from epagneul.api.routes import router
from epagneul import settings
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException


def get_app() -> FastAPI:
    """Configure and returns a FastAPI application."""
    app = FastAPI(title=settings.api.app_name, debug=settings.api.debug)

    app.add_event_handler("startup", start_app_handler(app))
    app.add_event_handler("shutdown", stop_app_handler(app))
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_exception_handler(RequestValidationError, http_422_error)
    app.add_exception_handler(HTTPException, http_error_handler)

    app.include_router(router, prefix=settings.api.url_prefix)

    return app


app = get_app()
