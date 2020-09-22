import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='chanchitoFeliz',
    password='holamundo',
    database ='prueba'
)

cursor = midb.cursor()

#cursor.execute('select * from Usuario')

sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)' 
values = ('micorreo@correo.com', 'Nombre Usuario', '45')

cursor.execute(sql, values)

midb.commit()

print(cursor.rowcount)