from user_service import *


def main() -> None:
    validator = UserValidator()
    repository = UserRepository()
    notifier = UserNotifier()
    repository.save_user(UserData(username="Lucas", email="lucas@gmail.com", password="123123123", id="123"))
    print("Get user: ", repository.get_user("123"))
    print("Validate email: ",validator.validate_email("adfadfadfa"))
    print("Validate email:",validator.validate_email("lucas@gmail.com"))
    repository.save_user(UserData(username="jose", email="jose@gmail.com", password="ndflkansdflakdnfald", id="124"))
    print("Validate password: ",validator.validate_password("123"))
    print("Validate password: ",validator.validate_password("1231231"))
    notifier.send_email("jose@gmail.com")
    print("Get user: ", repository.get_user("124"))

if __name__ == "__main__":
    main()
