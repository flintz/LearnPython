ImportError: No module named django():
        manage.py shell
          import django # "ImportError: No module named django"
        find / -name Django
        PYTHONPATH=/path/to/django/parent/dir 
        charm>file>settings>Project>Project Interpreter select pythun virtenv
      class django.core.exceptions.improperlyconfigured requested setting default_index_tablespace():
        manage.py
          os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
        wsgi.py
          os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
        manage.py shell --settings=mysite.settings
