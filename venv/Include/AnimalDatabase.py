import sqlite3 as db


# ID / Imie / Rasa / Lista cech (string) / Description / pic path


def Command(command):
    database = db.connect("animals.db")
    cursor = database.cursor()
    cursor.execute(command)
    database.commit()
    database.close()


def addNewAnimal(animal_id, name, breed, features, description, picture_path):
    database = db.connect("animals.db")
    cursor = database.cursor()
    cursor.execute("INSERT INTO animals VALUES (?, ?, ?, ?, ?, ?)",
                   (animal_id, name, breed, features, description, picture_path))
    database.commit()
    database.close()


addNewAnimal(1, 'Frodo', 'Husky', 'fajny', 'ladny piesek', 'pies.jpg')