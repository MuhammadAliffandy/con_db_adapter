import sqlite3
import psycopg2
import pymysql


class NewDatabaseConnection:
    def connection_database(self):
        pass

class SQLiteDatabaseConnection(NewDatabaseConnection):
    def connection_database(self, database_name):
        return sqlite3.connect(database_name)

class PostgreSQLDatabaseConnection(NewDatabaseConnection):
    def connection_database(self, host, database, user, password , port):
        return psycopg2.connect(host=host, database=database, user=user, password=password ,port=port)

class MySQLDatabaseConnection(NewDatabaseConnection):
    def connection_database(self, host, database, user, password , port ):
        return pymysql.connect(host=host, database=database, user=user, password=password , port = port)








