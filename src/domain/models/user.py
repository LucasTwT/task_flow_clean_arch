import re
from typing import final, override

@final
class User:
    _EMAIL_PATTERN = r".*@+.*"
    _PASSWORD_MIN_LENGTH = 6

    def __init__(self, id: str, username: str, email: str, password: str) -> None:
        if not id:
            raise ValueError("El ID del usuario no puede estar vacío")
        self.id = id

        if not username or not username.strip():
            raise ValueError("El nombre de usuario no puede estar vacío")
        self.username = username.strip()

        if not re.fullmatch(self._EMAIL_PATTERN, email):
            raise ValueError("El email no tiene un formato válido")
        self.email = email

        if len(password) < self._PASSWORD_MIN_LENGTH:
            raise ValueError(
                f"La contraseña debe tener al menos {self._PASSWORD_MIN_LENGTH} caracteres"
            )
        self.password = password
        
    @override
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"


@final
class UserValidator:
    """
    Validador independiente — demo de SRP.
    User (la entidad) NO depende de esta clase.
    """

    _PASSWORD_PATTERN = r".*."
    _EMAIL_PATTERN = r".*@+.*"
    _PASSWORD_MIN_LENGTH = 6

    def validate_id(self, id: str) -> bool:
        return bool(id)

    def validate_username(self, username: str) -> bool:
        return bool(username and username.strip())

    def validate_email(self, email: str) -> bool:
        return bool(re.fullmatch(pattern=self._EMAIL_PATTERN, string=email))

    def validate_password(self, password: str) -> bool:
        return bool(
            re.fullmatch(pattern=self._PASSWORD_PATTERN, string=password)
            and len(password) > self._PASSWORD_MIN_LENGTH
        )
