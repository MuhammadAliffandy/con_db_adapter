import sqlite3
import psycopg2
import pymysql


class DatabaseConnection:
    def connect(self):
        pass

class SQLiteDatabaseConnection(DatabaseConnection):
    def connect(self, database_name):
        return sqlite3.connect(database_name)

class PostgreSQLDatabaseConnection(DatabaseConnection):
    def connect(self, host, database, user, password , port):
        return psycopg2.connect(host=host, database=database, user=user, password=password ,port=port)

class MySQLDatabaseConnection(DatabaseConnection):
    def connect(self, host, database, user, password , port ):
        return pymysql.connect(host=host, database=database, user=user, password=password , port = port)








