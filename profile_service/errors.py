class DataBaseException(Exception):
    pass


class UsernameAlreadyExists(DataBaseException):
    pass


class UsernameNotFound(DataBaseException):
    pass


class IdNotFound(DataBaseException):
    pass

class EmailAlreadyExists(DataBaseException):
    pass
