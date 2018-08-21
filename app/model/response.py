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

    def __get_success_response(self, data, status_code, message):
        self.__response['message'] = message
        self.__response['status_code'] = status_code
        if data is not None:
            self.__response.update(data)
        return self.__response

    def __get_failed_response(self, errors, status_code, message):
        if errors is None:
            raise ValueError()
        self.__response['errors'] = errors
        self.__response['message'] = message
        self.__response['status_code'] = status_code
        return self.__response

    def added(self, data, status_code=CREATED, message=''):
        """ get response body if added """
        if not message:
            message = '登録しました。'
        return self.__get_success_response(data, status_code, message)

    def add_failed(self, errors, status_code=BAD_REQUEST, message=''):
        """ get response body if add failed """
        if not message:
            message = '登録に失敗しました'
        return self.__get_failed_response(errors, status_code, message)

    def edited(self, data, status_code=OK, message=''):
        """ get response body if updated """
        if not message:
            message = '変更しました'
        return self.__get_success_response(data, status_code, message)

    def edit_failed(self, errors, status_code=CONFLICT, message=''):
        """ get response body if update failed """
        if not message:
            message = '変更に失敗しました'
        return self.__get_failed_response(errors, status_code, message)

    def deleted(self, status_code=NO_CONTENT, message=''):
        """ get response body if deleted """
        if not message:
            message = '削除しました'
        return self.__get_success_response(None, status_code, message)

    def delete_failed(self, errors, status_code=CONFLICT, message=''):
        """ get response body if delete failed """
        if not message:
            message = '削除に失敗しました'
        return self.__get_failed_response(errors, status_code, message)

    def fetch_success(self, data, status_code=OK, message=''):
        """ get response body if fetched """
        if not message:
            message = 'データ取得成功'
        return self.__get_success_response(data, status_code, message)

    def fetch_failed(self, errors, status_code, message=''):
        """ get response body if fetch failed"""
        raise NotImplementedError()

    def fetch_no_data(self, status_code=NO_CONTENT, message=''):
        """ get response if fetch no data """
        if not message:
            message = 'データがありません'
        return self.__get_success_response((), status_code, message)

    def notfound(self, message=''):
        """ get response if resource not found """
        if not message:
            message = '要求されたリソースは見つかりませんでした'
        return self.__get_failed_response((), NOT_FOUND, message)

    def unauthorized(self, message=''):
        """ get response if unauthorized request """
        if not message:
            message = '認証されていません'
        return self.__get_failed_response((), UNAUTHORIZED, message)

    def internal_server_error(self, message=''):
        """ get response if exceptions """
        if not message:
            message = 'サーバープログラムでエラーが発生しました'
        return self.__get_failed_response((), INTERNAL_SERVER_ERROR, message)
