# Django1


## manage.py / asgi.py / wsgi.py

|No|변경 전|변경 후|
|---|---|---|
|01|os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstproject.settings')|os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.settings')|


## settings.py

|No|변경 전|변경 후|
|---|---|---|
|01|ROOT_URLCONF = 'firstproject.urls'|ROOT_URLCONF = 'config.urls'|
|02|WSGI_APPLICATION = 'firstproject.wsgi.application'|WSGI_APPLICATION = 'config.wsgi.application'|
|03|BASE_DIR = Path(__file__).resolve().parent.parent|BASE_DIR = Path(__file__).resolve().parent.parent.parent|
