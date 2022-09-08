import psycopg2
#permite conectar a la base de datos de postgres
#transaccion es ejectuar varias consultas sobre la base de datos pero estas consultas modifican el estado de la base de datos
#dentro de la transaccion todos los queris se realizan correctamente pero si falla uno se hace roolback

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)
#cursor permite ejecutar sentencias sql en postgres
try:
    with conexion:
        # el uso de with cierra el recurso
        with conexion.cursor() as cursor:
            """""
            SENTENCIA SELECT
            # el porcentaje s sierv para pasarle y asignarle el valor a la sentencia
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada =input('Proporciona los ids\'s a buscar:(separado por comas)')
            llaves_primarias = (tuple(entrada.split(',')),)
            #id_persona = int(input('Proporciona el valor id_persona:'))
            cursor.execute(sentencia,llaves_primarias)
            #el fetchall permite recuperar todos los resgistros de la sentencia que se ha ejectado
            registros= cursor.fetchall()
            for registro in registros:
                print(registro)
            #recuperar solo un registro
            registros = cursor.fetchone()
            print(registros)
            
            SENTENCIA INSERT
            
            sentencia = 'INSERT INTO persona(nombre, apellido,email) VALUES(%s,%s,%s)'
            #siempre pasar tuplas
            # para insertar varios valores toca hacer una tupla de tuplas

            valores=(('Carlos','Lara','clara@gmail.com'),
                     ('gg','rr','eerew@gmail.com'),
                     ('ii','pp','iii@gmail.com'))
            #cambia el excute por el excute many
            #cursor.execute(sentencia, valores) para un solo registro
            cursor.executemany(sentencia, valores)# para varios registross
            registros_insertados = cursor.rowcount
            #roll back es cuando un registro falla ninguno se guarda en la base de datos
            print(f'Registros insertados: {registros_insertados}')
            
            #SENTENCIA UPDATE
            sentencia ='UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona =%s'

            valores =(('Juan Carlos','Juerez','jc@gmail.com',input('ingrese id a modificar perro')),
                      ('hh Carlos','dghgf','jc@gmail.com',input('ingrese id a modificar perro')),
                      ('oo Carlos','gghf','jc@gmail.com',7))
            cursor.executemany(sentencia,valores)
            registros_modificados = cursor.rowcount
            print(f'Registros actualizados : {registros_modificados}')
            """
            #SENTENCIA DELETE
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
#debe ser una tupla
            entrada=input('Ingrese  los id a eliminar(separado por comas)')
            valores=(tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados= cursor.rowcount
            print(f'Registros Eliminados : {registros_eliminados}')
except Exception as e:
    print(f'Ocurrio un error  {e}')
finally:
    #cerrar conexion a base de datos

    conexion.close()