# Error handling logic for the Flask application

from flask import jsonify
from api.exceptions import AppException

class CustomError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code
        self.message = message

    def to_dict(self):
        return {'message': self.message}

class NotFoundError(CustomError):
    def __init__(self, message="Resource not found"):
        super().__init__(message, status_code=404)

class UnauthorizedError(CustomError):
    def __init__(self, message="Unauthorized access"):
        super().__init__(message, status_code=401)

class ValidationError(CustomError):
    def __init__(self, message="Invalid input data"):
        super().__init__(message, status_code=422)

def handle_error(error):
    if isinstance(error, CustomError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    response = jsonify({'message': 'An unexpected error occurred.'})
    response.status_code = 500
    return response

def register_error_handlers(app):
    app.register_error_handler(Exception, handle_error)

def handle_app_exception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

def handle_generic_exception(error):
    print(f"[Unhandled Error] {str(error)}")
    response = jsonify({"error": "An unexpected error occurred"})
    response.status_code = 500
    return response

def register_error_handlers(app):
    app.register_error_handler(AppException, handle_app_exception)
    app.register_error_handler(Exception, handle_generic_exception)