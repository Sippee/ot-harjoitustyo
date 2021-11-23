import sqlite3 as sl

def delete_db():
    con = sl.connect('data/data.db')
    cursor = con.cursor()

    cursor.execute('''drop table if exists user;''')

    con.commit()

def create_db():
    con = sl.connect('data/data.db')
    cursor = con.cursor()

    cursor.execute('''create table user (username text primary key, password text);''')

    con.commit()

if __name__ == "__main__":
    delete_db()
    create_db()