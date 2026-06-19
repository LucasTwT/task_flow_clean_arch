import re


class UserService:
    def validate_email(self, email: str, pat: str = r".*@+.*") -> bool:
        return True if re.fullmatch(pattern=pat, string=email) else False
    
    def validate_password(self, password: str, pat: str = r".*.") -> bool:
        """Por si en el futuro se quiere añadir un patrón extra aparte de la longitud minima"""
        return True if (re.fullmatch(pattern=pat, string=password) and len(password) > 6) else False
    
    def save_user(self, id: str, name: str, email: str, password: str, users: list[dict]) -> None:
        users.append({"id": id, "name": name, "email": email, "password": password})
    
    def send_email(self, email) -> None:
        print(f"Email enviado a {email}")

    def get_user(self, id, users: list[dict]) -> dict:
        for user in users:
            if user["id"] == id:
                return user            
        return {}
