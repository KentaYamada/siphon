import json
from flask import Response


class ResponseBody(Response):
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

    # Default response message
    RESPONSE_MESSAGES = {
        OK: '処理成功しました',
        CREATED: '登録しました',
        NO_CONTENT: '削除しました',
        MOVED_PARMANENTLY: '',
        BAD_REQUEST: '不正なリクエストです',
        UNAUTHORIZED: '認証されていません',
        FORBIDDEN: '',
        NOT_FOUND: '要求されたリソースは見つかりませんでした',
        CONFLICT: '変更に失敗しました',
        INTERNAL_SERVER_ERROR: 'サーバープロプログラムでエラーが発生しました',
        SERVICE_UNAVAILABLE: 'サーバーへのアクセスが制限されています'
    }

    def __init__(self):
        super().__init__()
        self.__response = {
            'errors': [],
            'message': '',
            'status_code': None
        }

    def set_success_response(self, status_code, data=None, message=''):
        super().status_code = status_code
        self.__response['status_code'] = status_code
        if data is not None:
            self.__response.update(data)
        if not message and status_code in self.RESPONSE_MESSAGES.keys():
            self.__response['message'] = self.RESPONSE_MESSAGES[status_code]
        else:
            self.__response['message'] = message
        super().set_data(json.dumps(
            self.__response, ensure_ascii=False,
            encoding='utf8', indent=2
        ))

    def set_fail_response(self, status_code, errors=None, message=''):
        super().status_code = status_code
        self.__response['status_code'] = status_code
        self.__response['errors'] = errors
        if not message and status_code in self.RESPONSE_MESSAGES.keys():
            self.__response['message'] = self.RESPONSE_MESSAGES[status_code]
        else:
            self.__response['message'] = message
        super().set_data(json.dumps(
            self.__response, ensure_ascii=False,
            encoding='utf8', indent=2
        ))
