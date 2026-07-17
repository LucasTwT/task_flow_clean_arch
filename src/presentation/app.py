from fastapi import FastAPI

from presentation.routers import user_router, project_router, task_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="TaskFlow API",
        description="API de gestión de tareas con colaboración — Clean Architecture",
        version="0.1.0",
    )

    app.include_router(user_router.router, prefix="/api/v1")
    app.include_router(project_router.router, prefix="/api/v1")
    app.include_router(task_router.router, prefix="/api/v1")

    return app


app = create_app()
