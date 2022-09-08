from logger_base import log
# sirve para la conexion de los logs
import psycopg2 as bd
# para conexxion a la base de daros
from psycopg2 import pool
#sirve para la conexion a la base de datos
import sys
# para las excepciones

class conexion:
    # este es el nombre de la base de datos ya creada

    _DATABASE ='test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST= '127.0.0.1'
    #pool de conexiones:
    # es un objeto que administra los objetos de conexion a la base de datos
    #se pueden tener uno o mas y cada pool administra un numero determinado de objetos hacia la bd
    #es mejor tener disponibles onjetos de conexion
    #cuando un cliente necesite algo de la bd lo obtiene del pool y cuando termina lo libera para que alguien mas lo use
    _Minimo_conexiones = 1
    # es mejor tener este limite de conexiones a la base de datos
    _Maximo_conexiones = 5
    _pool = None
    @classmethod
    def obtenerpool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._Minimo_conexiones,cls._Maximo_conexiones,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port= cls._DB_PORT,
                                                      database = cls._DATABASE )
                log.debug(f'creacion del pool exitosa{cls._pool} ')
                return cls._pool

            except Exception as  e:
                log.error(f'Ocurrio un error {e}')
                sys.exit()
        else:
            return cls._pool
    @classmethod
    def ObtenerConexion(cls):
        # con el getconn solicitamos un objeto del pool de conexiones
       conexion = cls.obtenerpool().getconn()
       log.debug(f'Conexion obtenida del pool :{conexion}')
       return conexion

    #liberar un objeto de conexion cuando no se usa
    @classmethod
    def liberarConexion(cls,conexion):
        #con el putcoon pone el objeto conexion en el pool de conexiones para que otro lo use
        cls.obtenerpool().putconn(conexion)
        log.debug(f'Liberamos la conexion al pool {conexion}')
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerpool().closeall()




if __name__ == '__main__':
    conexion1 = conexion.ObtenerConexion()
    conexion.liberarConexion(conexion1)
    conexion2 = conexion.ObtenerConexion()
    conexion3 = conexion.ObtenerConexion()
    conexion.liberarConexion(conexion3)
    conexion4 = conexion.ObtenerConexion()
    conexion5 = conexion.ObtenerConexion()
    conexion.liberarConexion(conexion5)
    conexion6 = conexion.ObtenerConexion()

