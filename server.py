from app import startup_app


if __name__ == '__main__':
    app = startup_app()
    app.run(host='0.0.0.0', debug=True)
