import uvicorn

from config import settings

if __name__ == "__main__":
    uvicorn.run(
        settings.app.app,
        host=settings.app.host,
        port=settings.app.port,
        log_config=settings.app.log_config_path,
        # reload=settings.uvicorn.reload,
    )
