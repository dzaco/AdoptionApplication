from flask import Blueprint , render_template, request
main = Blueprint('main' , __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/adopt', methods = ['POST'])
def adopt():
    data = request.form
    data = data.values()
    animals = manageAnimals(data)
    return render_template('adopt.html', animals=animals)



# ACTIVE:x;KIDS:x;TIMEALONE:x;OTHERANIMS:x|SIZE:x;COST:x;HOUSESIZE:x;LIFELENGHT:x


MAX_POINTS = 4


def activeCommand(answer):
    switcher = {
        1: "DELETE FROM copy WHERE features LIKE '%ACTIVE:2%' OR '%ACTIVE:3%'",
        2: "DELETE FROM copy WHERE features LIKE '%ACTIVE:3%'",
        3: ""
    }
    return switcher.get(answer, "invalid answer")

def kidsCommand(answer):
    switcher = {
        1: "DELETE FROM copy WHERE features LIKE '%KIDS:0%'",
        2: ""
    }
    return switcher.get(answer, "invalid answer")

def timeAloneCommand(answer):
    switcher = {
        1: ("DELETE FROM copy WHERE features LIKE '%TIMEALONE:1%' or '%TIMEALONE:2%'"),
        2: ("DELETE FROM copy WHERE features LIKE '%TIMEALONE:1%'"),
        3: ""
    }
    return switcher.get(answer, "invalid answer")

def allergicCommand(answer):
    switcher = {
        1: "DELETE FROM copy WHERE features LIKE '%ALLERGIC:1%'",
        2: ""
    }
    return switcher.get(answer, "invalid answer")

def sizeCommand(answer):
    switcher = {
        1: "UPDATE copy SET score = score + 1 WHERE features LIKE '%SIZE:3%'",
        2: "UPDATE copy SET score = score + 1 WHERE features LIKE '%SIZE:2%'",
        3: "UPDATE copy SET score = score + 1 WHERE features LIKE '%SIZE:1%'"
    }
    return switcher.get(answer, "invalid answer")

def costCommand(answer):
    switcher = {
        1: "UPDATE copy SET score = score + 1 WHERE features LIKE '%COST:1%'",
        2: "UPDATE copy SET score = score + 1 WHERE features LIKE '%COST:2%'",
        3: "UPDATE copy SET score = score + 1 WHERE features LIKE '%COST:3%'"
    }
    return switcher.get(answer, "invalid answer")

def houseSizeCommand(answer):
    switcher = {
        1: "UPDATE copy SET score = score + 1 WHERE features LIKE '%HOUSESIZE:1%'",
        2: "UPDATE copy SET score = score + 1 WHERE features LIKE '%HOUSESIZE:2%'",
        3: "UPDATE copy SET score = score + 1 WHERE features LIKE '%HOUSESIZE:3%'"
    }
    return switcher.get(answer, "invalid answer")

def lifeLenghtCommand(answer):
    switcher = {
        1: "UPDATE copy SET score = score + 1 WHERE features LIKE '%LIFELENGHT:1%'",
        2: "UPDATE copy SET score = score + 1 WHERE features LIKE '%LIFELENGHT:2%'",
        3: "UPDATE copy SET score = score + 1 WHERE features LIKE '%LIFELENGHT:3%'"
    }
    return switcher.get(answer, "invalid answer")

def manageAnimals(data):
    import sys
    sys.path.append("..")
    from Models import database
    import sqlite3 as db

    data = list(data)

    database.copyDB()

    database.command(activeCommand(int(data[0])))
    database.command(kidsCommand(int(data[1])))
    database.command(timeAloneCommand(int(data[2])))
    database.command(allergicCommand(int(data[3])))

    # size
    if int(data[4]) == 1:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%|SIZE:3%'")
        database.command("UPDATE copy SET score = score + 1 WHERE features LIKE '%|SIZE:2%'")
    if int(data[4]) == 2:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%|SIZE:2%'")
        database.command("UPDATE copy SET score = score + 1 WHERE features LIKE '%|SIZE:3%'")
        database.command("UPDATE copy SET score = score + 1 WHERE features LIKE '%|SIZE:1%'")
    if int(data[4]) == 3:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%|SIZE:1%'")
        database.command("UPDATE copy SET score = score + 1 WHERE features LIKE '%|SIZE:2%'")

    # cost
    if int(data[5]) == 1:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%COST:1%'")
    if int(data[5]) == 2:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%COST:1%'")
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%COST:2%'")
    if int(data[5]) == 3:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%COST:1%'")
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%COST:2%'")
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%COST:3%'")

    # house size
    if int(data[6]) == 1:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%HOUSESIZE:1%'")
    if int(data[6]) == 2:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%HOUSESIZE:1%'")
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%HOUSESIZE:2%'")
    if int(data[6]) == 3:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%HOUSESIZE:1%'")
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%HOUSESIZE:2%'")
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%HOUSESIZE:3%'")

    # life lenght
    if int(data[7]) == 1:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%LIFELENGHT:1%'")
    if int(data[7]) == 2:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%LIFELENGHT:2%'")
        database.command("UPDATE copy SET score = score + 1 WHERE features LIKE '%LIFELENGHT:1%'")
    if int(data[7]) == 3:
        database.command("UPDATE copy SET score = score + 2 WHERE features LIKE '%LIFELENGHT:3%'")
        database.command("UPDATE copy SET score = score + 1 WHERE features LIKE '%LIFELENGHT:2%'")

    database.command('UPDATE copy SET score = (score * 100) / 8')

    d = db.connect('animals.db')
    cur = d.cursor()
    cur.execute('''SELECT * FROM copy ORDER BY score DESC''')
    results = cur.fetchall()
    print(results)
    d.close()

    return results

# import sys
# sys.path.append("..")
from Models import database
#
# database.addNewAnimal(0, 'testname' , 'testbreed',
#                       'ACTIVE:1;KIDS:1;TIMEALONE:3;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'leniuch', 'pic', '0')
#
# database.addNewAnimal(1, 'testname' , 'testbreed',
#                       'ACTIVE:2;KIDS:1;TIMEALONE:3;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'srednio leniuch', 'pic', '0')
#
# database.addNewAnimal(2, 'testname' , 'testbreed',
#                       'ACTIVE:3;KIDS:1;TIMEALONE:3;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'aktywny', 'pic', '0')
#
# database.addNewAnimal(3, 'testname' , 'testbreed',
#                       'ACTIVE:1;KIDS:0;TIMEALONE:3;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'agresywny - nie moze z dziecmi', 'pic', '0')
#
# database.addNewAnimal(4, 'testname' , 'testbreed',
#                       'ACTIVE:1;KIDS:1;TIMEALONE:3;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'na luzie z dziecmi', 'pic', '0')
#
# database.addNewAnimal(5, 'testname' , 'testbreed',
#                       'ACTIVE:1;KIDS:1;TIMEALONE:3;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'moze siedziec dlugo sam', 'pic', '0')
#
# database.addNewAnimal(6, 'testname' , 'testbreed',
#                       'ACTIVE:1;KIDS:1;TIMEALONE:1;ALLERGIC:1|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'nie moge w ogole byc sam', 'pic', '0')
#
# database.addNewAnimal(7, 'testname' , 'testbreed',
#                       'ACTIVE:1;KIDS:1;TIMEALONE:3;ALLERGIC:0|SIZE:1;COST:1;HOUSESIZE:1;LIFELENGHT:2',
#                       'ma wlosy', 'pic', '0')

# import sqlite3 as db
#
# d = db.connect('animals.db')
# c = d.cursor()
# c.execute('SELECT * FROM copy')
# print(c.fetchall())
# d.commit()
# d.close()



# database.copyDB()
#
# database.getAll()











