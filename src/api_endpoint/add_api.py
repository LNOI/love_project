import sys
import functools
import logging

from typing import Callable

from fastapi import Request, status
from fastapi.responses import JSONResponse, Response


logger = logging.getLogger('app_logger')
err_logger = logging.getLogger('error_logger')


def short_api_log(func:Callable):
    @functools.wraps(func)
    async def api_log_decorator(*args, **kwargs):
        input_map = kwargs['input_map']
        input_map_copy = {}
        for key in input_map:
            if len(str(key[1])) < 200:
                input_map_copy[key[0]] = key[1]
            else:
                input_map_copy[key] = 'Value too long'
        logger.info('%s request: start: %s' % (func.__name__, str(input_map_copy)))
        try:
            response = await func(*args, **kwargs)
            if type(response) == Response:
                logger.info('%s request: finish: %s, %s' % (func.__name__, str(response.status_code), str(response)))
            else:
                logger.info('%s request: finish: %s' % (func.__name__, str(response)))
            return response
        except Exception as e:
            err_logger.error('%s request: error: %s' % (func.__name__, e), exc_info=True)
            return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=e)
    return api_log_decorator




def add_api() -> None:
    if "application_api" not in sys.modules:
        import src.api_endpoint.application_api
    if "until_sql" not in sys.modules:
        import src.api_endpoint.until_sql
  
    