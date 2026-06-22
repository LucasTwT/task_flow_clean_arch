from repositories import UserRepository, UserData
from notifiers import UserNotifier, EmailNotifier, SMSNotifier, PushNotifier
from validators import UserValidator

def main() -> None:
    validator = UserValidator()
    repository = UserRepository()

    repository.save_user(UserData(username="Lucas", email="lucas@gmail.com", password="123123123", id="123"))
    print("Get user: ", repository.get_user("123"))
    print("Validate email: ", validator.validate_email("adfadfadfa"))
    print("Validate email: ", validator.validate_email("lucas@gmail.com"))

    repository.save_user(UserData(username="jose", email="jose@gmail.com", password="ndflkansdflakdnfald", id="124"))
    print("Validate password: ", validator.validate_password("123"))
    print("Validate password: ", validator.validate_password("1231231"))
    print("Get user: ", repository.get_user("124"))

    notifiers: list[UserNotifier] = [
        EmailNotifier(),
        SMSNotifier(),
    ]

    for notifier in notifiers:
        notifier.send(to="jose@gmail.com", message="Tarea completada")

    notifiers.append(PushNotifier())

    for notifier in notifiers:
        notifier.send(to="lucas@empresa.com", message="Nuevo proyecto asignado")


if __name__ == "__main__":
    main()
