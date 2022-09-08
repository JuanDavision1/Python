import psycopg2 as bd
# transaccion es ejectuar varias consultas sobre la base de datos pero estas consultas modifican el estado de la base de datos
# dentro de la transaccion todos los queris se realizan correctamente pero si falla uno se hace roolback

conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)'
            valores =('juan','sdfsfz','kuuusdmd')
            cursor.execute(sentencia,valores)
            sentencia = 'UPDATE persona SET nombre= %s, apellido = %s, email=%s WHERE id_persona = %s'
            valores =('pedrito','dd','kfkf@kfmkf',11)
            cursor.execute(sentencia,valores)


except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se hizo rollback  {e}')
finally:
    # cerrar conexion a base de datos
    print('Termina la Transaccion')
    conexion.close()