from flask import Flask, render_template, redirect, url_for, g
from .modules import auth, ui

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        # if g.user is None: return redirect(url_for('auth.login'))
        # return render_template('screening.html')
        # return render_template('auth.html')
        # return redirect(url_for('ui.patient_demographic'))
        return render_template('index.html')

    app.register_blueprint(auth.bp)
    app.register_blueprint(ui.bp)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
