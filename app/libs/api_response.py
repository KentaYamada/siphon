import json
from flask import Response


class ApiResponse(Response):
    def __init__(self, status_code, message='', data=None, errors=None):
        super().__init__()
        self.mimetype = 'application/json'
        self.status_code = status_code
        body = {
            'message': message,
            'errors': errors
        }
        if data is not None:
            body.update(data)
        json_data = json.dumps(
            body,
            ensure_ascii=False,
            indent=2
        )
        self.set_data(json_data)
