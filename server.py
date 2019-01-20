from os import environ
from app import startup_app


if __name__ == '__main__':
    # set development env
    environ['APP_TYPE'] = 'development'
    app = startup_app()
    app.config.from_object('app.config.DevelopmentConfig')
    # print(app.__dict__)
    app.run()
