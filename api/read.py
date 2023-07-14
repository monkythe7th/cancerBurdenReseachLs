from ..modules.db_conn import *

def read(c,item = None):
    col = noSQLdb(c)
    if item:
        x = col.find_one(item)
        return x
    else:
        return col.find_one()

def get_all(c):
    return noSQLdb(c).find()