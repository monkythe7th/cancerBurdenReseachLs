from flask import Flask, render_template, redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from .modules import auth, ui, db_conn

def create_app():
    app = Flask(__name__)
    # db = SQLAlchemy()
    app.config.from_mapping(
        SECRET_KEY='dev',
        SESSION_TYPE='filesystem'
    )
    Session(app)
    # app.config.from_object(db_conn.Connection())
    
    db_conn.FlaskDB_connection(app)

    @app.route('/')
    @auth.login_required
    def index():
        # if g.user is None: return redirect(url_for('auth.login'))
        return render_template('index.html')

    app.register_blueprint(auth.bp)
    app.register_blueprint(ui.bp)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
