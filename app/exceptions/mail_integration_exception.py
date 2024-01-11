
class MailIntegrationException(Exception):

    def __init__(self, cause) -> None:
        message = "An error occurred during mail sending process"
        self.cause = cause
        super().__init__(message)