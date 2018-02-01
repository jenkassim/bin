# Docker
- Location of files stored on host : ` /var/lib/docker `

## Start up service
$ sudo systemctl start docker

## Create Dockerfile
- Reference how to write Dockerfile : https://docs.docker.com/engine/reference/builder/
```
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Set proxy server, replace host:port with values for your servers
ENV http_proxy host:port
ENV https_proxy host:port

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

```

## Requirements file
- Create requirements file to install into container

## Build the app
- Be in the directory level that has Dockerfile, requirements.txt and app files
`   $ docker build -t containername . `

- Check built images
`
    $ docker images
`

## Run the app
- Port 80 is set by Dockerfile EXPOSE variable
`
    $ docker run -p 4000:80 containername
`

- Content served in web page: http://0.0.0.0:80 or
`   
    $ http://localhost:4000
`

- Also able to cmd shell to view the same content
`
    $ curl http://localhost:4000
`

## Run the app in background
- Run app in background and terminal returns long container ID.
`
    $ docker run -d -p 4000:80 containername
    
    [
        290e82ae897b62645c5cf0a9f18c0aad15ee2e56865ea6ad476aca209c693bfe
    ]
`

- Get abbreviated container ID
`
    $ docker container ls
    [
        CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                  NAMES
290e82ae897b        demo                "python app.py"     About a minute ago   Up About a minute   0.0.0.0:4000->80/tcp   peaceful_bassi

    ]
`

- Stop background app running
`
    $ docker container stop <Container-ID>
`

- Kill background app running
`
    $ docker container kill <Container-ID>
`


## Container Commands
- List all running containers
`   $ docker container ls`
- List all containers including non running containers
`   $ docker container ls -a `
- Remove all containers
`   $ docker container rm $(docker container ls -a -q) `
- Remove specific container on machine
`   $ docker container rm <hash> `



## Image Commands

- Export built image to run it elsewhere.
- A registry is a collection of repos and a repo is a collection of images. The Docker CLI uses Docker's public registry by default
- List all images on the machine
`
    $ docker image ls -a
`
- Inspect images
`
    $ docker inspect <tag or id>
`


### Login with DockerID
`   $ docker login `

### Tag the image
- Local image with a repo on a registry : ` username/repository:tag `
- Tag is used to give images a versioning.
`
    $ docker tag <image> username/repository:tag
`

### Publish the image
- Upload tagged image to the repo
`
    $ docker push username/repository:tag
`

### Pull and run Image from remote repo
`
    $ docker run -p 4000:80 username/repository:tag
`

### Remove local repo docker image
`
    $ docker image rm <image id>
`

### Remove all images from the machine
`
    $ docker image rm $(docker image ls -a -q)


## Services
### Docker Compose
- Tool for defining and running multi-container Docker apps.
- Uses a YAML file to configure apps services and create/start all services from configuration.
`
    https://docs.docker.com/compose/compose-file/#dockerfile
`

- Require manual installation (check for latest version)
`
    $ sudo curl -L https://github.com/docker/compose/releases/download/1.19.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    $ chmod +x /usr/local/bin/docker-compose
`

- Add permission to visudo and ~./bashrc
`
    - In ~/.bashrc:
    alias docker-compose='sudo /usr/local/bin/docker-compose

    - In visudo (/etc/sudoers) :
    jenna_mk        ALL=(ALL)       NOPASSWD: /usr/bin/docker
    jenna_mk        ALL=(ALL)       NOPASSWD: /usr/local/bin/docker-compose
`

- Steps :

(a) Define app's environment with a Dockerfile so it can be reproduced anywhere. Define each service in a Dockerfile.
(b) Define the services and their relation to each other in the docker-compose.yml file.
(c) Start the app via docker-compose

### Run App with docker compose
- Starts Compose and runs your entire app
`
    $ docker-compose up
` 
- Start App to run in the background
`
    $ docker-compose up -d

    Then to stop the background app
    $ docker-compose stop
`
- Stop application by cmd or Ctrl-C in terminal
`
    $ docker-compose down
`
- Check for currently running apps
`
    $ docker-compose ps
`
- Run one-off commands for services
`
    $ docker-compose run <service-cmd>
    $ docker-compose run web env
`

- Removes all containers
`
    $ docker-compose rm -v
`
- Docker-compose command line references : ` https://docs.docker.com/compose/reference/ `



### Bind mounts
https://docs.docker.com/engine/admin/volumes/bind-mounts/#start-a-container-with-a-bind-mount
- To mount host machine's files or directory into a container.
- The file or directory is referenced by its full or relatives path on the host machine.

### Volume
- A new directory is created within Docker's storage directory on the host machine


## Docker with PostgreSQL














