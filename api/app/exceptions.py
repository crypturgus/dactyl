class NotAuthenticatedError(Exception):
    def __init__(self, message="User is not authenticated"):
        super().__init__(message)


class UserNotFoundError(Exception):
    def __init__(self, message="User not found"):
        super().__init__(message)
