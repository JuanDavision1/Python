from conexion import conexion
from logger_base import log
class cursordelpool:
    def __init__(self):
        self._conexion = None
        self._cursor = None
        #llamada a un recurso
    def __enter__(self):
        #obetenr la conexion
        log.debug('inicio del metodo with __enter__')
        self._conexion = conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    # hacer roolback o regresar el objeto de la conexion
    def __exit__(self, tipo_excepcion, valor_excepcion, detaller_excepcion):
        log.debug(f'Se ejecuta metodo __extit')
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepciony se hace roolback: {valor_excepcion}{tipo_excepcion}{detaller_excepcion}')
        else:
            self._conexion.commit()
            log.debug(f'commit de la transaccion')
            self._cursor.close()
            conexion.liberarConexion(self._conexion)
if __name__ == '__main__':
  with cursordelpool() as cursor:
     log.debug('dentro del bloque with')
     cursor.execute('SELECT * FROM persona')
     log.debug(cursor.fetchall())
