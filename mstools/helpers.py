import inspect
import logging
from functools import wraps
from timeit import default_timer as timer
from django.conf import settings


logger = logging.getLogger(settings.METRICS_LOGGER_NAME)


def time_it_and_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        is_method = False

        try:
            is_method = inspect.getfullargspec(func).args[0] == 'self'
        except: # noqa
            pass

        if is_method:
            full_func_name = '%s.%s.%s' % (func.__module__, args[0].__class__.__name__, func.__name__)
        else:
            full_func_name = '%s.%s' % (func.__module__, func.__name__)

        start = timer()
        func_res = func(*args, **kwargs)
        end = timer()

        data = {
            'metrics':  'time_it',
            'func_name': full_func_name,
            'duration': end - start,
            'func_args': args,
            'func_kwargs': kwargs,
        }

        logger.info('#time_it_and_log', extra=data)
        return func_res
    return wrapper
