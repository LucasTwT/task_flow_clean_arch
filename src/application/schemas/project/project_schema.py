from pydantic import BaseModel


class CreateProjectRequestSchema(BaseModel):
    name: str
    description: str = ""


class CreateProjectResponseSchema(BaseModel):
    id: str
    name: str
    owner_id: str
    description: str
    is_archived: bool


class ProjectResponseSchema(BaseModel):
    id: str
    name: str
    owner_id: str
    description: str
    is_archived: bool


class ArchiveProjectRequestSchema(BaseModel):
    project_id: str


class ArchiveProjectResponseSchema(BaseModel):
    id: str
    name: str
    is_archived: bool
