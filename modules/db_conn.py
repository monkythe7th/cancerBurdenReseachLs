import os
from flask import Flask,render_template, request, current_app
# from flask_mysqldb import MySQL
# from mysql import connector
# import yaml 
# noSQL db import for authentication: mongodb
from pymongo import MongoClient
# from flask_pymongo import PyMongo
from ..api import create
from werkzeug.security import generate_password_hash

# def FlaskDB_connection(app):

#     db = yaml.load(open('db.yaml'), Loader= yaml.FullLoader)
#     # #congfigure db
#     # conn = connector.connect( host = db['mysql_host'], user = db['mysql_user'], password = db['mysql_password'], database = db['mysql_db'])
#     # return conn
#     config = {
#         'MYSQL_HOST': db['mysql_host'],
#         'MYSQL_USER': db['mysql_user'],
#         'MYSQL_PASSWORD': db['mysql_password'],
#         'MYSQL_DB': db['mysql_db']
#     }
#     app.config = config

# def cursor():
#     pass

# ============================================
# connecting to noSQLdb: i.e. mongodb;
# ============================================
uri = "mongodb+srv://cluster0.7nocv.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
# client = MongoClient(os.environ['noSQL_DB_CONN'])
client = MongoClient("mongodb://localhost:27017/?directConnection=true")
# client = MongoClient(uri,
#                 tls=True,
#                 tlsCertificateKeyFile='modules/X509-cert-8985860075988249075.pem',
#                 server_api=ServerApi('1'))

def noSQLdb(collection='test'):
    db = client["les_can_reg"]
    col = db[collection]
    return col

def create_admin():
    admin = {
        'name': 'Ramoeletsi Ramoeletsi',
        'username': 'admin',
        'email': 'tester@test.com',
        'user_type': 'admin',
        'password': generate_password_hash('PassW0rd')
    }
    create.create('admin',admin)

if __name__ == '__main__':
    noSQLdb()
    create_admin()
    print(client.list_database_names())