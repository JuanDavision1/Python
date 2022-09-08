from cursor_del_pool import cursordelpool
from logger_base import log
from usuario import Usuario


class usuarioDao:
    _SELECT = 'SELECT * FROM "Usuarios"'
    _INSERT = 'INSERT INTO "Usuarios"(username,password) VALUES(%s,%s) '
    _UPDATE = 'UPDATE "Usuarios" SET username= %s, password= %s WHERE id_usuario = %s'
    _DELETE = 'DELETE FROM "Usuarios" WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with cursordelpool() as cursor:
            log.debug('Seleccionando Usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            listaUser = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                listaUser.append(usuario)
            return listaUser
    @classmethod
    def insertar(cls,usuario):
        with cursordelpool() as cursor:
            log.debug(f'Usuario a insertar:{usuario}')
            valores =(usuario.username, usuario.password)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount

    @classmethod
    def actualizar(cls,usuario):
        with cursordelpool() as cursor:
            log.debug(f'usuario a actualizar:{usuario}')
            valores = (usuario.username,usuario.password,usuario.id_usuario)
            cursor.execute(cls._UPDATE,valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,usuario):
        with cursordelpool() as cursor:
            log.debug(f'Usuario eliminado:{usuario}')
            valores =(usuario.id_usuario,)
            cursor.execute(cls._DELETE,valores)
            return cursor.rowcount







if __name__ == '__main__':
    # insertar registro
    # usuario11 = Usuario(username='holman',password=9999)
    # usuario_insertadas = usuarioDao.insertar(usuario11)
     #log.debug(f'Personas insertadas{usuario_insertadas}')

    # actualizar registro NO SIRVEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
     #usuariot22 = Usuario(3,"Fresa",11111)
     #persona_actualizada = usuarioDao.actualizar(usuariot22)
     #log.debug(f'Persona Actualizada{persona_actualizada}')
    # eliminar NO SIRVEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
     persona71 = Usuario(id_usuario=4)
     persona_eliminada = usuarioDao.eliminar(persona71)
     log.debug(f'Persona eliminada{persona_eliminada}')
     usuarito = usuarioDao.seleccionar()
     for recorrer in usuarito:
        log.debug(recorrer)



