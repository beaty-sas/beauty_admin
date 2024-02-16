from beauty_admin.conf.settings import settings
from beauty_models.beauty_models.migrate_db import migrate_db

if __name__ == '__main__':
    migrate_db(sqlalchemy_database_uri=str(settings.sqlalchemy_database_uri))
