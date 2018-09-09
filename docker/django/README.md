# Docker Installation 
Tutorial: https://www.stavros.io/posts/how-deploy-django-docker/

- Stop other postgresql ports in use:
```
    $ sudo systemctl stop postgresql
```

- Create docker-compose file
- Use dc file :
```
    $ docker-compose exec web django-admin.py startproject <project>
```
- Note: 'run' command is a one-off cmd for services, will create a container for each executed cmd.
- start/up will use first created container
- Use exec to excute command within container


- Change django-admin ownership from root to user
```
    $ sudo chown -R $USER:$USER .
```

- Move django files and folders so that manage.py is in the same folder dir as dc.yml file

- Django Files Settings.py file:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': ,
        'HOST': 'db',
        'PORT': 5432,
    }
}
```
- Set Postgresql env settings
```
$ POSTGRES_PASSWORD="pleaseUseAStr0ngPassword"
$ POSTGRES_USER="postgres"
$ echo $POSTGRES_PASSWORD
pleaseUseAStr0ngPassword
$ echo $POSTGRES_USER
postgres
```



- Run dc command from top level dir of project
```
    $ docker-compose up / start
```

- To run manage.py command
```
    $ docker-compose exec web python manage.py runserver 8000
    $ docker-compose exec web python manage.py migrate
```

- Create superuser
```
    $ docker-compose exec web python manage.py createsuperuser
```

## Create App
- Create an App
```
    $ docker-compose exec web python manage.py startapp <MyApp>
```
- Add new App to settings.py file under INSTALLED_APPS
- Add new app to url in <project/url.py>
- Run the server

