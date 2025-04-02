import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="НовыйПароль",
        database="human_friends",
        port=3306
    )

def add_animal(name, type_, commands, birth_date):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO home_animals (name, type, commands, birth_date) VALUES (%s, %s, %s, %s)",
                   (name, type_, ",".join(commands), birth_date))
    db.commit()
    db.close()
