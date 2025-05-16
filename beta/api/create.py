from ..modules.db_conn import *

def create(c,item):
    return noSQLdb(c).insert_one(item).inserted_id