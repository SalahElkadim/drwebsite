web: gunicorn drwebsite.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn drwebsite.wsgi
web: gunicorn drwebsite.wsgi:application --bind 0.0.0.0:$PORT
