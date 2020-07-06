import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='valeriy',
    passwd=''
)

mycursor = mydb.cursor()


def work_with_db():
    while (command := input('Enter SQL > ')) != "exit":
        try:
            execute_command(command)
        except mysql.connector.errors.InternalError:
            print('Error command, try again.')
            pass
        except mysql.connector.errors.InterfaceError:
            pass
        except mysql.connector.errors.ProgrammingError:
            print('Error command, try again.')
            pass
    else:
        mydb.commit()
        print('Work is completed')
        mydb.close()


def execute_command(command):
    list_of_str = []
    mycursor.execute(command)
    command_results = mycursor.fetchall()
    d = [list(i) for i in command_results]
    for i in d:
        results1 = list(map(str, i))
        list_of_str.append(results1)
    for i in list_of_str:
        print(', '.join(i))


work_with_db()
