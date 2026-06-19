import structlog
import logging
from django.core.exceptions import ImproperlyConfigured

logger = structlog.get_logger()

def get_logger(name):
    return structlog.get_logger(name)

def log_error(request, error, context=None):
    logger.error(
        'Error occurred',
        error=str(error),
        context=context or {},
        path=request.path if request else None,
        method=request.method if request else None,
        user=request.user.username if request and request.user.is_authenticated else None,
    )

def log_info(message, context=None):
    logger.info(
        message,
        context=context or {},
    )

def log_warning(message, context=None):
    logger.warning(
        message,
        context=context or {},
    )

def log_debug(message, context=None):
    logger.debug(
        message,
        context=context or {},
    )
