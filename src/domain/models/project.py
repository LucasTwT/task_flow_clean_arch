from datetime import datetime


class Project:
    def __init__(
        self,
        id: str,
        name: str,
        owner_id: str,
        description: str = "",
        created_at: datetime | None = None,
    ) -> None:
        if not id:
            raise ValueError("El ID del proyecto no puede estar vacío")
        self.id = id

        if not name or not name.strip():
            raise ValueError("El nombre del proyecto no puede estar vacío")
        if len(name) > 100:
            raise ValueError("El nombre del proyecto no puede exceder 100 caracteres")
        self.name = name.strip()

        if not owner_id:
            raise ValueError("El proyecto debe tener un owner")
        self.owner_id = owner_id

        self.description = description.strip() if description else ""
        self.created_at = created_at or datetime.now()
        self.is_archived: bool = False

    def archive(self) -> None:
        self.is_archived = True

    def restore(self) -> None:
        self.is_archived = False

    def __repr__(self) -> str:
        return f"Project(id={self.id!r}, name={self.name!r})"
