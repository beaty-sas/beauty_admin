python migrate_db.py;
gunicorn -c gunicorn-conf.py server:app;
