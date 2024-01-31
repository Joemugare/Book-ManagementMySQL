# db.py
import mysql.connector
from config import DB_CONFIG

def connect():
    connection_params = DB_CONFIG.copy()
    database_name = connection_params.pop('database', None)

    # Specify the 'mysql_native_password' authentication plugin
    return mysql.connector.connect(
        **connection_params,
        database=database_name,
        auth_plugin='mysql_native_password'
    )

def close_connection(connection):
    connection.close()

def create_books_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        published_year INT
    )
    """)
    conn.commit()
    close_connection(conn)

def add_book(title, author, published_year):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO books (title, author, published_year)
    VALUES (%s, %s, %s)
    """, (title, author, published_year))
    conn.commit()
    close_connection(conn)

def get_all_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    close_connection(conn)
    return books

def delete_book(book_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    conn.commit()
    close_connection(conn)
