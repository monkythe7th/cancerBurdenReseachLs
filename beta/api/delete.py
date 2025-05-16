from ..modules.db_conn import *

def delete(c,item):
    return noSQLdb(c).delete_one(item)
