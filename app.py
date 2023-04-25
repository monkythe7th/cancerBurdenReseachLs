from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('demographic.html')

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
