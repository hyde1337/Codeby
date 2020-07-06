import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    database='mysql',
    user='valeriy',
    passwd=''
)
products = [('батон нарезной', '21 руб'),
            ('масло подсолнечное', '60 руб'),
            ('крупа гречневая', '80 руб'),
            ('молоко', '54 руб'),
            ('яйцо куриное', '55 руб'),
            ('кетчуп', '75 руб'),
            ('сок томатный', '92 руб'),
            ('макароны', '30 руб'),
            ('зеленый горошек', '92 руб'),
            ('селёдка', '92 руб')]

mycursor = mydb.cursor()
mycursor.execute('create database first')
mycursor.execute('use first')
mycursor.execute('create table products (id INT AUTO_INCREMENT, name VARCHAR (255), price VARCHAR (255), '
                 'PRIMARY KEY(id))')
ins_tab = 'insert into products (name, price) VALUES (%s, %s)'
mycursor.executemany(ins_tab, products)


mydb.commit()
print('Database \'first\' was create')
mydb.close()
