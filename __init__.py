from . import app

if __name__ == '__main__':
    app.create_app().run(host="0.0.0.0")