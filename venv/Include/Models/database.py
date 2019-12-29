import sqlite3 as db

# ID, Name, Breed, Features, Description, Pic Path, score (int)


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



def getAll():
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

#addNewAnimal(1, 'dlugosz', 'jamnik', 'ACTIVE:1;KIDS:1;TIMEALONE:3;OTHERANIMS:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#             'typical jamnik', 'jamnik.jpg')

# SELECT * FROM animals WHERE features LIKE '%ACTIVE:1%' OR '%ACTIVE:2%'

# getAll()

# ('ACTIVE:x;KIDS:x;TIMEALONE:x;OTHERANIMS:x|SIZE:x;COST:x;HOUSESIZE:x;LIFELENGHT:x')

# det
# aktywny?
# 1 - leniwy, 2 - normalny ,3 - aktywny
# dzieci?
# 0 - nie moze z dziecmi,1 - moze z dziecmi
# dlugo sam w domu?
# 1 - ktos musi byc ciagle w domu , 2 - <6h ,3 >6h
# inne zwierze?
# 0 - nie moze (agresywny), 1 - na luzie moze z innymi
#
# ndet
# romiar?
# 1 - malutki, 2 - normalny, 3 - gigant
# koszt?
# 1 - <100, 2 - <200 , 3 - <400
# duzy dom?
# 1 - male mieszkanko, 2 - duze mieszkanko,  3 - wielka chata
# dlugosc zycia?
# 1 - 1-10, 2 - 10-20, 3 - 20+



