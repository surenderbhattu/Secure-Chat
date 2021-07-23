import sqlite3
from sqlite3 import Error

conn = ""

def create_connection():
    global conn
    try:
        conn = sqlite3.connect("./users.db")
        print("Connected to Database !")
    except Error as e:
        print(e)

def send_image(sender, recipient,image):
    query = "INSERT INTO images(sender,recipient,image) VALUES('" + str(
        sender) + "','" + str(recipient) + "','" + str(image) + "')"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    print("Image Sent")

def send_email(sender, recipient, message):
    query = "INSERT INTO emails(sender,recipient,message) VALUES('" + str(
        sender) + "','" + str(recipient) + "','" + str(message) + "')"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    print("Email Sent")

def get_messages():
    cur = conn.cursor()
    cur.execute("SELECT * FROM emails")
    rows = cur.fetchall()
    return rows

def get_images():
    cur = conn.cursor()
    cur.execute("SELECT * FROM images")
    rows = cur.fetchall()
    return rows

def register_user(email, password):
    query = "INSERT INTO users(email,password) VALUES('" + \
        str(email) + "','" + str(password) + "')"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    print("User registered with ID ", cur.lastrowid)

def select_users():
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    return rows


def create_user_table():
    query = "CREATE TABLE IF NOT EXISTS users ( id integer PRIMARY KEY, email text NOT NULL, password text); "
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

def create_emails_table():
    query = "CREATE TABLE IF NOT EXISTS emails ( sender text NOT NULL, recipient text NOT NULL, message text); "
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)

def create_images_table():
    query = "CREATE TABLE IF NOT EXISTS images ( sender text NOT NULL, recipient text NOT NULL, image text); "
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)