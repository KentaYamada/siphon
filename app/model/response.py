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

    @property
    def response_body(self):
        return self.__response

    def added(self, data, message=''):
        """ get response body if added """
        self.__response['status_code'] = CREATED
        self.__response['message'] = message if not message else '登録しました。'
        self.__response['errors'] = []
        self.__response.update(data)
        return self.__response

    def add_failed(self, errors, message=''):
        """ get response body if add failed """
        self.__response['status_code'] = BAD_REQUEST
        self.__response['message'] = message if not message else '登録に失敗しました。'
        self.__response['errors'] = errors
        return self.__response

    def edited(self, data, message=''):
        """ get response body if updated """
        self.__response['status_code'] = CREATED
        self.__response['message'] = message if not message else '変更しました。'
        self.__response['errors'] = []
        self.__response.update(data)
        return self.__response

    def edit_failed(self, errors, message=''):
        """ get response body if update failed """
        self.__response['status_code'] = CONFLICT
        self.__response['message'] = message if not message else '変更に失敗しました。'
        self.__response['errors'] = errors
        return self.__response

    def set_delete_success(self, message=''):
        """ get response body if deleted """
        self.__response['status_code'] = NO_CONTENT
        self.__response['message'] = message if not message else '削除しました。'
        self.__response['errors'] = []
        return self.__response

    def set_delete_failed(self, data, message=''):
        """ get response body if delete failed """
        pass

    def fetch_success(self, data, message=''):
        """ get response body if fetched """
        self.__response['status_code'] = OK
        self.__response['message'] = message if not message else 'データ取得成功'
        self.__response['error'] = []
        return self.__response

    def set_fetch_failed(self, errors, message=''):
        """ get response body if fetch failed"""
        pass

    def fetch_no_data(self, message=''):
        """ get response if fetch no data """
        self.__response['status_code'] = NO_CONTENT
        self.__response['message'] = message if not message else 'データがありません。'
        self.__response['errors'] = []
        return self.__response
