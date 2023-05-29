from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from mysql import connector
import yaml 


def Connection():

    db = yaml.load(open('db.yaml'), Loader= yaml.FullLoader)
    #congfigure db
    conn = connector.connect( host = db['mysql_host'], user = db['mysql_user'], password = db['mysql_password'], database = db['mysql_db'])
    return conn
