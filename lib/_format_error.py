from traceback import format_exception as _fmt
from sys import exc_info as _exc


def get_error():
    """Get an Error"""
    exc = _exc()
    if exc[0] is None:
        return None
    return ''.join(a for a in _fmt(exc[0], exc[1], exc[2]))
