import sqlite3 as db

# ID, Name, Breed, Features, Description, Pic Path


def command(command):
    database = db.connect('animals.db')
    cursor = database.cursor()
    cursor.execute(command)
    database.commit()
    database.close()


def selectStatement(command):
    database = db.connect('animals.db')
    cursor = database.cursor()
    cursor.execute(command)
    result = cursor.fetchall()
    print(result)
    database.commit()
    database.close()
    return result



def printAll():
    database = db.connect('animals.db')
    cursor = database.cursor()
    cursor.execute('''SELECT * FROM animals''')
    result = cursor.fetchall()
    print(result)
    database.commit()
    database.close()
    return result


def addNewAnimal(animal_id, name, breed, features, description, picture_path):
    database = db.connect('animals.db')
    cursor = database.cursor()
    cursor.execute("INSERT INTO animals VALUES (?, ?, ?, ?, ?, ?)",
                   (animal_id, name, breed, features, description, picture_path))
    database.commit()
    database.close()


# database = db.connect('animals.db')
# cursor = database.cursor()
# cursor.execute('''CREATE TABLE animals
#              (id INTEGER, name text, breed text, features text, description text, picturePath text)''')
# database.commit()
# database.close()

#addNewAnimal(1, 'mariusz', 'husky', 'agresywny; leniwy', 'bardzo ladny piesek', 'pies.jpg')

#printAll()