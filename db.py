# db.py
import mysql.connector
from contextlib import contextmanager
import os

@contextmanager
def connect():
    connection_params = {
        'host': os.environ.get('DB_HOST', 'localhost'),
        'user': os.environ.get('DB_USER', 'root'),
        'password': os.environ.get('DB_PASSWORD', 'Qunta729'),
        'database': os.environ.get('DB_DATABASE', 'library'),
        'port': os.environ.get('DB_PORT', '3306'),
        'auth_plugin': 'mysql_native_password'
    }

    conn = mysql.connector.connect(**connection_params)
    try:
        yield conn
    finally:
        conn.close()

def create_books_table():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                published_year INT
            )
            """)
        conn.commit()

def add_book(title, author, published_year):
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO books (title, author, published_year)
            VALUES (%s, %s, %s)
            """, (title, author, published_year))
        conn.commit()

def get_all_books():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
    return books

def delete_book(book_id):
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        conn.commit()
