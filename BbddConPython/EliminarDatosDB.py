import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='chanchitoFeliz',
    password='holamundo',
    database ='prueba'
)

cursor = midb.cursor()

#cursor.execute('select * from Usuario')

sql = 'delete from Usuario where id = %s'
values = (4, )

cursor.execute(sql, values)
midb.commit()