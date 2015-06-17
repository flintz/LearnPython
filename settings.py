 # Settings DB sqlite3
Engine : ‘...sqllite3’           # Edit name DB
Name : ‘patch’

# Setings DB postgreSQL
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'taskbuster_db',
'USER': 'taskuser',
'PASSWORD': 'fipujiqa66',
'HOST': '127.0.0.1',
'PORT': '5432',
              
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-Ru'
TEMPLATE_DIR
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
  STATIC_ROOT = os.path.join(BASE_DIR, "static/") #./manage.py collectstatic
)
