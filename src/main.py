from repositories import UserRepository, UserData
from validators import UserValidator
from notifiers import EmailNotifier, SMSNotifier, PushNotifier
from notifiers import UserNotifier
from task import Task, RecurringTask, MilestoneTask
from repository_isp import TaskDTO, InMemoryTaskReader
from task_service_dip import TaskData, ITaskRepository, PostgresTaskRepository, TaskService

def main() -> None:
    # SRP — Single Responsibility Principle
    # Cada clase tiene UNA sola razón para cambiar.
    # UserValidator valida, UserRepository persiste.
    print("SRP")

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

    # OCP — Open/Closed Principle
    # Abierto a extensión, cerrado a modificación.
    # Se puede agregar WhatsAppNotifier sin tocar nada existente.
    print("\nOCP")

    notifiers: list[UserNotifier] = [
        EmailNotifier(),
        SMSNotifier(),
    ]

    for notifier in notifiers:
        notifier.send(to="jose@gmail.com", message="Tarea completada")

    # Extensión: se agrega PushNotifier sin modificar EmailNotifier ni SMSNotifier
    notifiers.append(PushNotifier())

    for notifier in notifiers:
        notifier.send(to="lucas@empresa.com", message="Nuevo proyecto asignado")

    # LSP — Liskov Substitution Principle
    # Subtipos reemplazables por su base.
    # Cualquier código que espera Task funciona con subtipos.
    print("\nLSP")

    tareas: list[Task] = [
        RecurringTask(task_name="Revisar correo", interval=1),
   MilestoneTask(task_name="Lanzar producto", milestone="Lanzamiento oficial"),
    ]

    tareas[0].finish()
    for tarea in tareas:
        print(tarea.get_task_info())

    # ISP — Interface Segregation Principle
    # Interfaces chicas y específicas.
    # InMemoryTaskReader implementa solo y solo ITaskReader.
    print("\nISP")

    sample_tasks = [
        TaskDTO(id="1", title="Hacer ejercicio", description="", owner_id="lucas", is_completed=True),
        TaskDTO(id="2", title="Estudiar SOLID", description="", owner_id="lucas"),
        TaskDTO(id="3", title="Comprar", description="", owner_id="jose"),
    ]

    reader = InMemoryTaskReader(sample_tasks)

    print("Tareas completadas:", [t.title for t in reader.get_completed()])
    print("Tareas de lucas:", reader.count_by_owner("lucas"))
    print('Búsqueda "estu":', [t.title for t in reader.search_by_title("estu")])

    # DIP — Dependency Inversion Principle
    # Depender de abstracciones, no implementaciones.
    # TaskService recibe ITaskRepository por constructor.
    print("\nDIP")

    # Producción: repositorio PostgreSQL
    pg_repo = PostgresTaskRepository()
    service = TaskService(pg_repo)
    service.create_task(TaskData(id="1", title="Aprender DIP", owner_id="lucas"))

    # Tests: repositorio en memoria — TaskService no cambia
    class InMemoryTaskRepository(ITaskRepository):
        def __init__(self) -> None:
            self._tasks: dict[str, TaskData] = {}

        def save(self, task: TaskData) -> None:
            self._tasks[task.id] = task
            print(f"[MEMORIA] Tarea '{task.title}' guardada")

        def get_by_id(self, task_id: str) -> TaskData | None:
            return self._tasks.get(task_id)

    test_service = TaskService(InMemoryTaskRepository())
    test_service.create_task(TaskData(id="2", title="Test sin DB", owner_id="tester"))

if __name__ == "__main__":
    main()
