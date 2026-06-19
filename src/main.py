from user_service import UserService

def main() -> None:
    users: list[dict] = [{"id": "123", "name": "Lucas", "email": "lucas@gmail.com", "password": "1234"}]
    service = UserService()
    print("Get user: ", service.get_user("123", users))
    print("Validate email: ",service.validate_email("adfadfadfa"))
    print("Validate email:",service.validate_email("lucas@gmail.com"))
    service.save_user("124", "Jose", "jose@gmail.com", "123123123",  users)
    print("Validate password: ",service.validate_password("123"))
    print("Validate password: ",service.validate_password("1231231"))
    service.send_email("jose@gmail.com")
    print("Get user: ",service.get_user("124", users))

if __name__ == "__main__":
    main()