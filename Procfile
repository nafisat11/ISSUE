web: gunicorn core.wsgi --log-file=- 
web: python manage.py collectstatic --no-input; gunicorn core.wsgi --log-file - --log-level debug