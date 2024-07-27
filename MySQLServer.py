import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='your_host',  # Replace with your MySQL server host
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )
        cursor = connection.cursor()

        # Create the database
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed to create database: {err}")
        finally:
            cursor.close()
            connection.close()
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    create_database()
