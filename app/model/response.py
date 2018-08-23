# HTTP status codes
OK = 200
CREATED = 201
NO_CONTENT = 204
MOVED_PARMANENTLY = 301
BAD_REQUEST = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
CONFLICT = 409
INTERNAL_SERVER_ERROR = 500
SERVICE_UNAVAILABLE = 503


class ResponseBodyCreator():
    def __init__(self):
        self.__response = {
            'errors': [],
            'message': '',
            'status_code': None
        }

    def get_success_response(self, data, status_code, message):
        self.__response['message'] = message
        self.__response['status_code'] = status_code
        if data is not None:
            self.__response.update(data)
        return self.__response

    def get_failed_response(self, errors, status_code, message):
        if errors is None:
            raise ValueError()
        self.__response['errors'] = errors
        self.__response['message'] = message
        self.__response['status_code'] = status_code
        return self.__response

    def ok(self, data, message=''):
        if not message:
            message = '処理成功しました'
        return self.get_success_response(data, OK, message)

    def created(self, data, message=''):
        if not message:
            message = '登録しました'
        return self.get_success_response(data, CREATED, message)

    def no_content(self, message=''):
        if not message:
            message = '削除しました'
        return self.get_success_response(None, NO_CONTENT, message)

    def moved_marmently(self, data, message=''):
        if not message:
            message = ''
        return self.get_success_response(data, MOVED_PARMANENTLY, message)

    def bad_request(self, errors, message=''):
        if not message:
            message = '不正なリクエストです'
        return self.get_failed_response(errors, BAD_REQUEST, message)

    def unauthorized(self, message=''):
        if not message:
            message = '認証されていません'
        return self.get_failed_response((), UNAUTHORIZED, message)

    def forbidden(self, message=''):
        raise NotImplementedError()

    def not_found(self, message=''):
        if not message:
            message = '要求されたリソースは見つかりませんでした'
        return self.get_failed_response((), NOT_FOUND, message)

    def conflict(self, errors, message=''):
        if not message:
            message = '変更に失敗しました'
        return self.get_failed_response(errors, CONFLICT, message)

    def internal_server_error(self, message=''):
        if not message:
            message = 'サーバープログラムでエラーが発生しました'
        return self.get_failed_response((), INTERNAL_SERVER_ERROR, message)
