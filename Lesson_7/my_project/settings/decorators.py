import sys
from my_project.settings.client_log_config import logger as logger_client
from my_project.settings.server_log_config import logger as logger_server
import traceback
import inspect

if sys.argv[0].find('client') == -1:
    logger = logger_server

else:
    logger = logger_client
    

def log(func_to_log):
    # функция декоратор
    def log_server(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        logger.info(f'Была вызвана функция {func_to_log.__name__} с параметрами {args}, {kwargs}.'
                     f'Вызов из модуля {func_to_log.__module__}. Вызов из'
                     f' функции {traceback.format_stack()[0].strip().split()[-1]}.'
                     f'Вызов из функции {inspect.stack()[1][3]}')
        return ret
    return log_server
