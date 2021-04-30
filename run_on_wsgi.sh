#USANDO WSGI

uwsgi --http 0.0.0.0:8000 --WSGI-file firs_step_3.py 

#o usando gunicorn

gunicorn firs_step_3:__hug_wsgi__