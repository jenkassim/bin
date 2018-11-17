# Cockpit

### Installation
```
    $ sudo dnf install cockpit
```

- Open firewall:
```
    $ sudo firewall-cmd --add-service=cockpit
    $ sudo firewall-cmd --add-service=cockpit --permanent
```

### Settings

- In /usr/lib/systemd/system/cockpit.socket, change stream to 127.0.0.1:
```
    [Unit]
    Description=Cockpit Web Service Socket
    Documentation=man:cockpit-ws(8)

    [Socket]
    ListenStream=127.0.0.1:9090

    [Install]
    WantedBy=sockets.target
```

- Enable service:
```
    $ sudo systemctl start cockpit.service
```

- Go to web browser : http://127.0.0.1:9090/

Server: localhost.localdomain
Username: root
Password: password

https://developers.redhat.com/blog/2016/11/15/cockpit-your-entrypoint-to-the-containers-management-world/