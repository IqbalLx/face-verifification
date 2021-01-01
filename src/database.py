import sqlite3 as sqlite
from sqlite3 import Error

import os
import glob

import config

"""
File untuk mengatur seluruh komunikasi script 
dengan database menggunakan SQLite
"""

class Database():
    def __init__(self):
        self.conn = sqlite.connect(config.DB_PATH)
        self.curs = self.conn.cursor()

    def create_table(self):
        self.curs.execute(config.CREATE_TABLE_QUERY)

    def show(self):
        self.curs.execute(config.SHOW_QUERY)
        data = self.curs.fetchall()
        
        return data
    
    def insert_user(self, ids, name):
        self.curs.execute(config.INSERT_DATA_QUERY, (ids, name))
        self.conn.commit()
    
    def update_name(self, ids, new_name):
        self.curs.execute(config.UPDATE_DATA_QUERY, (new_name, ids))
        self.conn.commit()

    def get_name(self, ids):
        try:
            self.curs.execute(config.SELECT_NAME_QUERY, (ids,))
            name = self.curs.fetchone()
        except Error:
            name = "Not Found"
            
        return name
    
    def delete(self, ids):
        self.curs.execute(config.DELETE_DATA_QUERY, (ids,))
        self.conn.commit()

        datapaths =  glob.glob(config.DATA_ROOT+"/people."+str(ids)+"*")
        for path in datapaths:
            os.remove(path)
    
    def close(self):
        self.conn.close()

