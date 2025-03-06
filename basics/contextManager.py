# Without Context Manager
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()  # Must close manually


# With Context Manager
with open("example.txt", "w") as file:
    file.write("Hello, world!")  # File auto-closes after block execution


# Class-Based Context Manager
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):  # Runs when `with` starts
        self.file = open(self.filename, self.mode)
        return self.file  # Returns file object

    def __exit__(self, exc_type, exc_value, traceback):  # Runs when `with` ends
        self.file.close()
with FileManager("test.txt", "w") as f:
    f.write("Hello, Context Manager!")


# Using contextlib Module
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file  # Pass control to `with` block
    finally:
        file.close()  # Ensures file is closed

# Using the context manager
with open_file("test.txt", "w") as f:
    f.write("Hello, World!")


# Managing Files
with open("sample.txt", "w") as file:
    file.write("Python is awesome!")


# Managing Database Connections
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()  # Close connection automatically

with DatabaseManager("test.db") as db:
    cursor = db.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")


# Locking Resources in Multithreading
import threading

lock = threading.Lock()

with lock:  # Ensures safe access to shared resources
    print("Thread-safe execution")
