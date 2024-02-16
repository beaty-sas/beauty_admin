import uvicorn

from beauty_admin.app import create_app
from beauty_admin.conf.logging import LOG_CONFIG
from beauty_admin.conf.settings import settings

app = create_app()

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=settings.PORT,
        log_level=settings.LOG_LEVEL.value.lower(),
        log_config=LOG_CONFIG,
        loop='uvloop'
    )
