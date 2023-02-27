import logging

#se usa para ir trazando lo que hace el programa
logging.basicConfig(level=logging.INFO)
logging.debug('debug')
logging.info('arrancando programa')
logging.warning('cuidadito')
logging.error('error')
logging.critical('critical')

