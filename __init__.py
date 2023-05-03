from . import app

if __name__ == '__main__':
    app.create_app().run(debug=True,host='0.0.0.0',port=5000)