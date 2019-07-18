from app.libs.api_response import ApiResponse


def api_error_handler(error):
    if error is None:
        return ApiResponse(500, 'Application internal error')
    message = ''
    if hasattr(error, 'description') and error.description:
        message = error.description
    errors = None
    if hasattr(error, 'response') and error.response is not None:
        errors = error.response
    return ApiResponse(error.code, message, errors=errors)
