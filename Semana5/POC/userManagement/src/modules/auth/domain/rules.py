from src.seedwork.domain.rules import BusinessRule

class PasswordIsValid(BusinessRule):
    password: str

    def __init__(self, password, message='Password must have at least 8 characters'):
        super().__init__(message)
        self.password = password

    def is_valid(self) -> bool:
        return len(self.password) >= 8
