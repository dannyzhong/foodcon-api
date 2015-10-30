import MySQLdb as mdb
import sys

class db_utils:
    def __init__(self, _username, _password, _db_name, _host):
        self.username = _username
        self.password = _password
        self.db_name = _db_name
        self.host = _host
        
    def mysql_connection(self):
        try:
            self.con = mdb.connect(self.host, self.username, self.password,self.db_name)
            self.cursor = self.con.cursor()
        except mdb.Error as error:
            print 'Error: %s ' %error + '\nStop.\n'
            self.cursor.close()
            self.con.close()
            sys.exit()
            
    def close_connection(self):
        self.cursor.close()
        self.con.close()
    
    def get_vendor(self, id):
        self.mysql_connection();
        self.cursor.execute("SELECT VERSION()")
        result = self.cursor.fetchone()
        self.close_connection()
        return result
         
        