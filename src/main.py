from repositories import UserRepository, UserData
from notifiers import UserNotifier, EmailNotifier, SMSNotifier, PushNotifier
from validators import UserValidator
from task import Task, RecurringTask, MilestoneTask

"""
SOLID Principles:
- SRP (Single Responsibility Principle)
- OCP (Open/Closed Principle)
- LSP (Liskov Substitution Principle)

  TODO: Implement the remaining principles

-ISP (Interface Segregation Principle)
- DIP (Dependency Inversion Principle)
"""


def main() -> None:
    """
    SRP (Single Responsibility Principle) - Each class has a single responsibility.
    """
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

    """
    OCR (Oplen/Closed Principle) - Open for extension, closed for modification.
    Notifiers can be extended with new types without modifying existing code.
    """

    notifiers: list[UserNotifier] = [
        EmailNotifier(),
        SMSNotifier(),
    ]

    for notifier in notifiers:
        notifier.send(to="jose@gmail.com", message="Tarea completada")

    notifiers.append(PushNotifier())

    for notifier in notifiers:
        notifier.send(to="lucas@empresa.com", message="Nuevo proyecto asignado")

    """
    LSP (Liskov Substitution Principle) - Subtypes must be substitutable for their base types.
    Task subclasses can be used wherever a Task is expected, without altering the correctness of the program.
    """

    reccurrent_task = RecurringTask(task_name="Revisar correo", interval=1)
    milestone_task = MilestoneTask(task_name="Lanzar producto", milestone="Lanzamiento oficial")
    reccurrent_task.finish()
    print(reccurrent_task.get_task_info())
    print(milestone_task.get_task_info())
    print(isinstance(reccurrent_task, Task))
    print(isinstance(milestone_task, Task))

if __name__ == "__main__":
    main()
