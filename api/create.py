from ..modules.db_conn import *

def create(item):
    return noSQLdb().insert_one(item).inserted_id