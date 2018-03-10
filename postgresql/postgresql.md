#Postgresql
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-centos-7
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
## Enable
```
    $ sudo systemctl enable postgresql

    - Created symlink /etc/systemd/system/multi-user.target.wants/postgresql.service → /usr/lib/systemd/system/postgresql.service.
```

## Start / Stop service
- Start service
```
    $ sudo systemctl start service postgresql
```

- Stop service
```
    $ sudo systemctl stop service postgresql
```

- Check for services running
```
    $ sudo service postgresql stop
    [
        Redirecting to /bin/systemctl stop postgresql.service
    ]

```

## Init DB
```
    $ sudo postgresql-setup --initdb --unit postgresql
    [
        * Initializing database in '/var/lib/pgsql/data'
        * Initialized, logs are in /var/lib/pgsql/initdb_postgresql.log
    ]
```

## Installation creates a user called 'postgres' with normal user password
- To login to the database, user of the same name as database need to be switched to using methods:
```
    $ sudo -i -u postgres
    $ psql
        or
    $ sudo -u postgres psql
```

## Create New Role

## Create Database

## How-to-use
- Login as linux user
```
    $ sudo -i -u <username>
```

- Enable virtual env
```
    $ workon <venv>
```



