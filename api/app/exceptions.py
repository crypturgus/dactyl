class NotAuthenticatedError(Exception):
    def __init__(self, message="User is not authenticated"):
        super().__init__(message)


class UserNotFoundError(Exception):
    def __init__(self, message="User not found"):
        super().__init__(message)


class SomethingWentWrongError(Exception):
    """Exception raised when something goes wrong."""

    def __init__(self, message="Something went wrong"):
        self.message = message
        super().__init__(self.message)
