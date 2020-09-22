import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='chanchitoFeliz',
    password='holamundo',
    database ='prueba'
)

cursor = midb.cursor()

#cursor.execute('select * from Usuario')

sql = 'update Usuario set email = %s where id = %s'
values = ('micorreo@correo.com', 4)

cursor.execute(sql, values)

midb.commit()

print(cursor.rowcount)