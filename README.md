https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_many/
https://docs.djangoproject.com/en/2.0/topics/pagination/

Steps taken

#### Install Django:

``` sudo pip3 install django==1.11 ```

#### Create a project:

``` django-admin startproject unitracker . ```

#### In settings.py:

``` ALLOWED_HOSTS = [os.environ.get('C9_HOSTNAME')] ```

#### In the terminal:

``` python3 manage.py runserver $IP:$C9_PORT ```

#### Show Home in Favourites, in .bash_aliases - add the following:

``` alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT" ```

#### Create a .gitignore file and add the following:

``` *.sqlite3 ```

#### Transfer the files from the accounts app created previously and update the settings.py:

```
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
```

```
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.CaseInsensitiveAuth']
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

In env.py:

```
import os

os.environ.setdefault("STRIPE_PUBLISHABLE", "")
os.environ.setdefault("STRIPE_SECRET", "")
os.environ.setdefault("DATABASE_URL", "")
os.environ.setdefault("SECRET_KEY", "")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "")
```

Install Bootstrap:

```