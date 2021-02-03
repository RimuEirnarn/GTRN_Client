_CLIENT_ERROR = {"200": "Connection Timed Out",
                 "201": "Invalid Authentication",
                 "202": "I'm not a server",
                 "203": "I'm leaving up"
                 }
_SERVER_ERROR = {"100": "Connection Timed Out",
                 "101": "Game is Full",
                 "102": "Invalid Key",
                 "103": "Version not Supported",
                 "104": "Server no longer serving"
                 }


class Error(Exception):
    """Exception for Server and Client"""
    def __init__(self, code, arg=None):
        if code in _CLIENT_ERROR:
            self.code = str(code)
            if arg is None:
                self.arg = _CLIENT_ERROR[self.code]
            super().__init__(f"[ERRNO {self.code}] {self.arg}")
        if code in _SERVER_ERROR:
            self.code = str(code)
            if arg is None:
                self.arg = _SERVER_ERROR[self.code]
            super().__init__(f"[ERRNO {self.code}] {self.arg}")
        else:
            raise NotImplementedError(f"Code {code} was not Implemented.")


def abort(code):
    """Abort Operation and raise an Error"""
    raise Error(code)