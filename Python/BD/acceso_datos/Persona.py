from logger_base import log
class Persona:
    def __init__(self,id_persona=None, nombre=None,apellido= None,email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email


    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self,id_persona):
        self._id_persona = id_persona
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def id_persona(self,nombre):
        self._nombre = nombre
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def id_persona(self,apellido):
        self._apellido = apellido
    @property
    def email(self):
        return self._email

    @email.setter
    def id_persona(self,email):
        self._email= email

    def __str__(self):
        return f'''
        Id persona:{self._id_persona}
        Nombre:{self._nombre}
        Apellido:{self._apellido}
        Email:{self._email}
        '''


if __name__ == '__main__':
    peronsa1 = Persona(1,'ddd','lff','lñddflñlfdk')
    log.debug(peronsa1)
#simular un insert
    persona1 = Persona( nombre='dfsdf',apellido='dfsdf',email='sddfsdfdf')
    log.debug(persona1)

#simular delete
    persona1 = Persona(id_persona=1)
    log.debug(persona1)