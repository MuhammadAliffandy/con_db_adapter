from library.new_db_connection import SQLiteDatabaseConnection
from library.new_db_connection import PostgreSQLDatabaseConnection
from library.new_db_connection import MySQLDatabaseConnection

class AdapterDatabaseConnection():

    def __init__(self, new_connection_system):
        self.new_connection_system = new_connection_system

    def connect(self):
        return self.new_connection_system.connection_database()


class DatabaseConnectionFactory:

    def __init__ (self,db_type = None):
        self.db_type = db_type

    def create_connection(self):
        if self.db_type == 1:
            return AdapterDatabaseConnection(SQLiteDatabaseConnection).connect()
        elif self.db_type == 2 :
            return AdapterDatabaseConnection(PostgreSQLDatabaseConnection).connect()
        elif self.db_type == 3 :
            return AdapterDatabaseConnection(MySQLDatabaseConnection).connect()
        else:
            raise ValueError("Invalid database type")


print('===== SILAHKAN PILIH DATABASE CONNECTION ANDA =====\n')

db_list = ['1. SQLITE' , '2. POSTGRESQL' , '3. MYSQL']

for data in db_list:
    print(data)

answer = int(input('\nMasukkan type databasenya (pilih angka) : '))

if( answer < 4 and answer > 0):
    print(f'Database Status : {DatabaseConnectionFactory(answer)}')
else:
    print('Keyword yang anda masukkan salah')