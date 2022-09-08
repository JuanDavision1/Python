import logging as log
#HANDLER MANEJADOR
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s %(message)s]',
                datefmt='%I:%M:%S %p',
                handlers= [
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('MENSAJE A NIVEL DE INFO')
    log.warning('Mensaje a nivel warning')
    log.error('MENSAJE A NIVEL DE error')
    log.critical('MENSAJE A NIVEL DE critico')
