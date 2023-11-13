release: python manage.py makemigrations && python manage.py migrate
web: gunicorn rest_api_codealong.wsgi:application