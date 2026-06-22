import re
from typing import final

@final
class UserValidator:
    _PASSWORD_PATTERN = r".*."
    _EMAIL_PATTERN = r".*@+.*"
    _PASSWORD_MIN_LENGTH = 6

    def validate_email(self, email: str) -> bool:
        return True if re.fullmatch(pattern=self._EMAIL_PATTERN, string=email) else False

    def validate_password(self, password: str) -> bool:
        return True if (re.fullmatch(pattern=self._PASSWORD_PATTERN, string=password) and len(password) > self._PASSWORD_MIN_LENGTH) else False


