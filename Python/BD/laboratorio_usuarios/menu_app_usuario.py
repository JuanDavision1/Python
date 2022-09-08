from usuario import Usuario
from usuarioDao import usuarioDao
from logger_base import log
opcion = None
while opcion != 5:
    print('Opciones:')
    print('1.Listar usuarios')
    print('2.Agregar usuario')
    print('3.Modificar usuarios')
    print('4.Eliminar usuario')
    print('5.salir')
    opcion= int(input('Escribe tu opc 1-5:'))
    if opcion== 1:
        usuariosListados = usuarioDao.seleccionar()
        for usuario in usuariosListados:
            log.info(usuario)
    elif opcion== 2:
        username_var = input('escribe el user')
        pass_var = input('Escribe la contraseña')
        usuarionuevo = Usuario(username = username_var,password = pass_var)
        usuariosInsertados =usuarioDao.insertar(usuarionuevo)
        log.info(f'Usuarios insertados :{usuariosInsertados}')
    elif opcion == 3:
        id_user_var = int(input('Escribe el id a modificar'))
        username_var = input('escribe el user')
        pass_var = input('Escribe la contraseña')
        usuariocambiado = Usuario(id_usuario=id_user_var, username=username_var, password=pass_var)
        usuarioactualizado = usuarioDao.actualizar(usuariocambiado)
        log.info(f'Usuarios Actualizado :{usuarioactualizado}')
    elif opcion == 4:
        id_user_var =int(input('Ingresa el id a leminianar'))
        usuarioelimar= Usuario(id_usuario=id_user_var)
        usuarioEliminado = usuarioDao.eliminar(usuarioelimar)
        log.info(f'usuario Eliminado:{usuarioEliminado}')

    else:
        log.info('salimos de la aplicacion')


