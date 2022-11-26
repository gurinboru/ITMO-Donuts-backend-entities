class DataBaseException(Exception):
    pass


class EmailAlreadyExists(DataBaseException):
    pass


class IdNotFound(DataBaseException):
    pass
