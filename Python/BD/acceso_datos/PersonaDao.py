import  cursor_del_pool
from Persona import Persona
from conexion import conexion
from logger_base import log

class personaDao:
    '''
    DAO(DATA ACCESS OBJECT)
    CRUD(CREATE,READ,UPDATE,DELETE)
    '''
    _SELECCIONAR ='SELECT * FROM persona '
    _INSERTAR ='INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
    _ACTUALIZAR ='UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona =%s '

    @classmethod
    def seleccionar(cls):
        with cursor_del_pool as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            print(f'aqui 2')
            personas = []
            for registro in registros:
                print(f'aqui 3')
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def Insertar(cls,persona):
        with cursor_del_pool as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'Persona a insertada:    {persona}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with cursor_del_pool as cursor:
                valores = (persona.nombre, persona.apellido, persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona actualizada=>{persona}')
                return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with cursor_del_pool as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Persona eliminado=>{persona}')
                return cursor.rowcount

if __name__ == '__main__':
    # insertar registro
  #  persona22 = Persona(nombre='jdjd', apellido='fff', email='gggf@')
   # persona_insertadas = personaDao.Insertar(persona22)
   # log.debug(f'Personas insertadas{persona_insertadas}')
    # actualizar registro
   # persona71 = Persona('Fresa','jueres','ñññ@fsmfk',9)
    #persona_actualizada = personaDao.actualizar(persona71)
   # log.debug(f'Persona Actualizada{persona_actualizada}')
#eliminar
  #  persona71 = Persona(id_persona=11)
   # persona_eliminada = personaDao.eliminar(persona71)
  #  log.debug(f'Persona eliminada{persona_eliminada}')


#select
    personashola = personaDao.seleccionar()
    for persona in personashola:
         log.debug(persona)