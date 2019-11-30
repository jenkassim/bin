# Docker
# Table of Content

## Installation

## Create Docker Environment
- [Start up service](#start-up-service)
- [Create Dockerfile](#create-dockerfile)
- [Requirements file](#requirements-file)
- [Create / Build an Image](#create-/-build-an-image)
- [Check running host services](#check-running-host-services)
- [Check status](#check-status)
- [Tagging](#tagging)

## Running Docker
- [Run the container](#run-the-container)
- [Container Commands](#container-commands)
- [Image Commands](#image-commands)
- [Environment Arguments](#env-arguments)

## Services
- [Docker Compose](#docker-compose)
- [Run Docker Compose](#run-docker-compose)

## Clean up Docker Environment
- [Clean-up Docker entirely and start fresh](#cleanup-to-freshstart)
- [Prune Containers](#prune-containers)
- [Prune Images](#prune-images)
- [Prune Everything](#prune-everything)

## Images & Layers

## [Storage Drivers](#Storage-Drivers)

## [Data Volumes](#data-volumes)
## [Bind Mounts](#bind-mounts)


- Docker representation :
    - Docker Image == Class
    - Docker Container == Instance

`/var/lib/docker/image/devicemapper/imagedb/content/sha256`
- Location of files stored on host : ` /var/lib/docker `
- Docker Image is an inert, immutable file that's a snapshot of a container.
- Image are created with the `build` command and produces a container when started with `run`.
- Images are bound to containers, so remove containers before removing images

# Installation
- https://docs.docker.com/docker-for-mac/install/
- https://docs.docker.com/docker-for-windows/install/
- https://docs.docker.com/toolbox/toolbox_install_mac/
- https://docs.docker.com/toolbox/toolbox_install_windows/
- https://docs.docker.com/engine/installation/linux/centos/
- https://docs.docker.com/engine/installation/linux/fedora/
- https://docs.docker.com/engine/installation/linux/linux-postinstall/

# Login
```
    $ docker login
```
- Saves user auth to : `~/.docker/config.json`
- Windows : `%USERPROFILES%/.docker/config.json`

- Tag docker image to user account
```
    $ docker image tag <image-name> <username>/<image-tage>:<version-tag>
```

- Push to docker repo
```
    $ docker image push <username>
```


# Create Docker Environment
## Start up service
```
$ sudo systemctl start docker
```

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
```
    $ pip freeze > requirements.txt
```

## Create / Build an Image
- Be in the directory level that has Dockerfile, requirements.txt and app files
```
   $ docker image build -t <image-name>:<tag-version> <dir-to-Dockerfile>
   $ docker build -t <image-name> -f <docker-filename> <directory>
```

- Check built images
```
    $ docker images
    or
    $ docker image ls -a
    or
    $ docker image inspect <image-name>
```

- When building images, docker will create an individual docker layer for each step.
- This layers will be stored as cache for subsequent builds with same layer requirements.
```
    Step 3/8 : WORKDIR /app
    ---> Running in 091262a89e39
    Removing intermediate container 091262a89e39
```

- Changes to Dockerfile, will re-build changed layer commands and all layers after it.

## Push to DockerHub
- Login to dockerhub, authentication stored in config.json file
- Push and pull from dockerhub:
```
    $ docker login
    $ docker image push <username>/<image-name>
    $ docker pull <username>/<image-name>:<tag-name>
```

## Cleanup to freshstart
- If need to have clean slate of Docker environment, remove the Docker files and restart service
```
    $ rm -rf /var/lib/docker
    $ systemctl restart docker
```

## Check for host running services
- If host has services running on the same port as Docker defined ports, need to stop host services. (Or change Docker setting port)
- Unix check for running services
```
    $ sudo service <service> status
    $ sudo service postgresql status

    $ ps aux
```
- Stop running services
```
    $ sudo service <service> stop
```

## Check status
- Check for current running containers
```
    $ docker container ls
    $ docker ps
```
- Check for all available containers
```
    $ docker container ls -a
    $ docker ps -a
```

- Check for current running images
```
    $ docker image ls
```

- Check for all available images on machine
```
    $ docker image ls -a
    $ docker images
```
## Tagging
- Re-tag images with a different name
```
    $ docker image tag <tag-name> <new-tag-name>
    $ docker image tag jenkassim/web1 web1
```

# Running Docker
## Run the container
- Container is an instance of an image
- Port 80 is set by Dockerfile EXPOSE variable
```
    $ docker run -p 4000:80 <image-name>

    - Run app in background and terminal returns long container ID.
    $ docker run -d -p 4000:80 <image-name>

    - Run app with volume connected
    $ docker run -d -p 8888:8888 -v <host-directory>:<container-directory>
```
- Use `container run` if used with management tags / flags.
```
    $ docker container run -it -p <by-port-on-dockerhost>:<by-port-on-docker-container><docker-image>

    $ docker container run -it -p 5000:5000 -e FLASK_APP=app.py web1
```
- `by-port-on-docker-container` should match the App port declared in Dockerfiles.
- On windows system (Docker Toolbox), need to use Docker Machine IP which is used instead of localhost
```
    $ docker-machine ip
```

- Content served in web page: http://0.0.0.0:80 or http://localhost:4000

- Also able to cmd shell to view the same content
`
    $ curl http://localhost:4000
`

| Run commands | Syntax | Usage |
--------------|--------|-------|
| `-e` | Define input parameter (environment variable) in container | $ docker container run -p 5000:5000 -e FLASK_APP=app.py |
| `-it` | Run container interactively with terminal usage | $ docker container run -it -p 5000:5000 |
| `-rm` | Immediately remove container after it's been stopped | $ docker container run -it -rm -p 5000:5000 |
| `-d` | Run container in background | $ docker container run -it -d -p 5000:5000 |
| `--name` | Declare name for container | $ docker container run -p 5000:5000 --name web1 |
| `-v` | Defines Path on host:Path where the files will be mounted on the container. Mount current working directory into the `app` folder in the container| $ docker container run -p 5000:5000 -v $PWD:/app web1 |
| `--user` | Run as specific users (files created as user instead of root) | $ docker container exec --user "$(id -u):$(id -g)" web1 touch abc.txt|

## Container Commands
- Containers are instances of an image (runtime object) and encapsulates an environment to run apps.
- An image can have multiple containers (instances)

##### Get abbreviated container ID
```
    $ docker container ls
    [
        CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS                  NAMES
290e82ae897b        demo                "python app.py"     About a minute ago   Up About a minute   0.0.0.0:4000->80/tcp   peaceful_bassi

    ]
```

- Stop background app running
`
    $ docker container stop <Container-ID>
`
- Kill background app running
`
    $ docker container kill <Container-ID>
`

- Kill all running containers
```
    $ docker kill `docker ps -aq`
```

- Stop all running containers
```
    $ docker stop $(docker ps -aq)
```
- Remove all containers
```
   $ docker container rm $(docker container ls -a -q)
   $ docker-compose down
```
- Remove specific container on machine
```
   $ docker container rm <hash>
```
- View size of running container
```
    $ docker ps -s
```

## Image Commands
- Built Images can be exported to run it elsewhere.
- A registry is a collection of repos and a repo is a collection of images. The Docker CLI uses Docker's public registry by default
- List all images on the machine
```
    $ docker image ls -a
```

- Inspect images and layers within image
```
    $ docker inspect <tag or id>
    $ docker history <image-id>
```

##### Repository Images
- Login with DockerID :
`   $ docker login `
- Pull an image from a repo :
`   $ docker pull `

##### Pull and run Image from remote repo
```
    $ docker run -p 4000:80 username/repository:tag
    Output: http://localhost/
```

##### Tag the image
- Local image with a repo on a registry : ` username/repository:tag `
- Tag is used to give images a versioning.
`
    $ docker tag <image> username/repository:tag
`

##### Publish the image
- Upload tagged image to the repo
`
    $ docker push username/repository:tag
`

##### Remove Docker image
- Image cannot be removed via id if multiple image of same name, different tag exist. Image will need to be removed via name instead of id.
- Remove created containers before removing Images used in the containers

- To remove local docker image
`
    $ docker image rm <image id>
`

- To remove all images from the machine by image-id
`
    $ docker image rm $(docker image ls -a -q)
`

- Image with child(dependent) images cannot be removed, would destroy local build cache. To remove those images manually execute for each individual image:
```
    $ docker image ls -a
    $ docker rmi <image-name>:<tag>
```
- To remove all together:
`
    $ docker rmi $(docker images --format '{{.Repository}}:{{.Tag}}')
`
- Using prune command:
`
    $ docker image prune -a
`

## Environment Variables





## Services
- A service only runs one image but codifies the way it is run - what ports to use, how many container replicas, etc.
- Service are defined via `docker-compose.yml` file.


### Docker Compose
- Tool for defining and running multi-container Docker apps.
- Uses a YAML file to configure apps services and create/start all services from configuration.
`
    https://docs.docker.com/compose/compose-file/#dockerfile
`

##### Docker-Compose manual installation (check for latest version)
```
    $ sudo curl -L https://github.com/docker/compose/releases/download/1.19.0-rc2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    $ chmod +x /usr/local/bin/docker-compose
```

- Add permission to visudo and ~./bashrc
```
    - In ~/.bashrc:
    alias docker-compose='sudo /usr/local/bin/docker-compose

    - In visudo (/etc/sudoers) :
    user        ALL=(ALL)       NOPASSWD: /usr/bin/docker
    user        ALL=(ALL)       NOPASSWD: /usr/local/bin/docker-compose
```

- Steps :

(1) Define app's environment with a Dockerfile so it can be reproduced anywhere. Define each service in a Dockerfile.

(2) Define the services and their relation to each other in the docker-compose.yml file.

(3) Start the app via docker-compose

### Run Docker Compose
- Check is defined port in docker-compose.yml is already running other services and either change the port or stop the service.


- Starts Compose and runs your entire app
- Creates a new container for app with each up command
```
    $ docker-compose up
```

- Use to Start / Stop app in existing containers(avoid duplicate containers for same image built)
```
    $ docker-compose start
    $ docker-compose stop
```

- Start App to run in the background
```
    $ docker-compose up -d

    - Then to stop the background app
    $ docker-compose stop
```

- Stop application by cmd or Ctrl-C in terminal
```
    $ docker-compose down
```

- Check for currently running apps
```
    $ docker-compose ps
```

- Run one-off commands for services(will create a new container for cmd)
```
    $ docker-compose run <service-cmd>
    $ docker-compose run web env
```

- Run arbitrary commands in existing services containers(avoid duplicated containers)
```
    $ docker-compose exec <service-cmd>
    $ docker-compose exec web python manage.py migrate
```

- Removes all containers
```
    $ docker-compose rm -v
```
- Docker-compose command line references : ` https://docs.docker.com/compose/reference/ `

#### Docker-Compose Run / Exec
- `docker run` : Manipulates <b>images</b> that exists or accessible from localhost. A temp docker container is created and stopped after the command has finished running.
- `docker exec` : Operates an existing <b>container</b>


## Docker-compose file definition
##### Image
- Image name/repo, if not found on local machine Docker will look for it in Docer Hub and automatically downloads.

##### Environment
- Sets additional environment variables (overwrites existing ones) when container starts

##### Working_dir
- Cmd to do a cd to working_dir path when container starts

##### Command
- Runs whatever command specified when container starts.

##### Volumes
- Map a path from local machine to Docker container. Some examples of paths might be mapped are code repo directory, database files, log directories, etc.
- Changes inside containers which aren't mapped to host will disappear once containers are stopped.

##### Ports
- Option to expose container ports. Also can specify port forwarding from host machine to container.
- E.g: "8000:80" will forward port 8000 of host to port 80 of container.

##### Links
- Define other containers that the service links to.
- Used to start a network communication between db container and web-server container.
- Linked services will be reachable at the hostname identical to the alias, or the service name if no alias was specified.
- E.g: When connecting to a db, localhost port will be fixed but container port will change everytime restart / remove container. Link can be use to make sure db is always connected even though container port is unknown.

##### Depends_on
- Start services in dependency order. All Depends_on services will be created / started before its own service.




### Data Volumes (DV)
https://docs.docker.com/storage/volumes/
- Data written to container that is not stored in a `data volume` will be deleted when container is deleted.
- Data volume is a directory / file in host filesystem that is mounted directly into a container.
- Multiple DV can be mounted into a single container
- Multiple containers can share one or more DV.
- Location of DV are outside host local storage area
- If source code is not on a volume, Docker layer will need to be re-built everytime there's code changes to be reflected. This is if the source code is copied into the Dockerfile / yml file.

### Start a container with a volume
- If start container wihout existing volume, Docker will auto create it.
```
    $ docker run -d --name <container-name> --mount source=<vol-name>, target=/app nginx:latest
```

- Verify that volume was created & mounted
```
    $ docker inspect <container-name>
    [
        "Mounts": [
            {
                "Type": "volume",
                "Name": <vol-name>,
                "Source": "/var/lib/docker/volumes/<vol-name>/_data",
                "Destination": "/app",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
    ]
```

- Stop container and remove volume
```
    $ docker container stop <container-name>
    $ docker container rm <container-name>
    $ docker volume rm <vol-name>
```

### Start a service with volumes
-

##### Create a Volume
```
    $ docker volume create <volume-name>
```
##### List Volumes
```
    $ docker volume ls
```
##### Inpect a volume
```
    $ docker volume inspect <volume-name>
```
##### Remove a volumne
```
    $ docker volume rm <volume-name>
```
#####Stop container & Remove volume and its data container
```
    $ docker-compose down -v
```

### Bind mounts
https://docs.docker.com/engine/admin/volumes/bind-mounts/#start-a-container-with-a-bind-mount
- To mount host machine's files or directory into a container.
- Sits outside of Docker area and dependent on host machine.

## CleanUp Docker
- Run Docker's garbage collection
### Prune Containers
- When containers are stopped, it's not automatically removed unless used `--rm` flag.
```
    $ docker container prune
```

### Prune Images
- Clean up unused images.
- Only cleans up <b>dangling</b> images, one that is not tagged and not referenced by any container.
- Dangling images are usually caused by intermediate images used during update / re-built of images (docker build or pull)
- Dangling images have tag `<none>:<none>` in docker images -a
```
    $ docker image prune
```

- To remove images which are not used by existing containers
- Also able to limit filtered expression.
```
    $ docker image prune -a
    $ docker image prune -a --filter "until=24h"
        - prune images created more than 24hours ago
```

- Clean dangling images
```
    $ docker images -f "dangling=true" -q
    $ docker rmi $(docker images -f "dangling=true" -q)
```
### Prune Volumes
- Volumes can be used by one or more containers and takes up space on Docker host. Volumes are never removed automatically.
```
    $ docker volume prune
```
- Reference : https://docs.docker.com/engine/reference/commandline/volume_prune/

### Prune Everything
- Prunes everything including volume(> v17.06.1) if specified.
```
    $ docker system prune
    $ docker system prune --volumes
```

# Images & Layers
- Image built up from series of layers, each layer represents an instruction in the image's dockerfile(`image layers`).
- Layers stacked on top of each other and only differs each by one set of instructions.
```
    FROM ubuntu:15.04
    COPY . /app
    RUN make /app
    CMD python /app/app.py
```
    `From` - Creates a layer from
    `Copy` - Adds files from your Docker client's current directory
    `Run`  - Builds application using `make` command
    `Cmd`  - What command to run within the container

# Containers & Layers
- Each container has a `writable layer` on top of other instructions layers, called the `container layer`. Stores changes (data state) to it's own container (ie writing new files, modifying existing files, deleting files)
- `Writeable Layer` removes when container is deleted.

## Storage Drivers
https://docs.docker.com/storage/storagedriver/
- Manages contents of `image layer` and `writable container layer` and how they interact together.
- Allows to create data in the `writeable layer` of the container. Files won't be persisted after container is deleted and both read and write speeds are low.
- Each layer stored in its own directory in host local storage aread : `/var/lib/docker/<storage-drive>/layers/`
- List contents of local storage area
```
    $ sudo ls /var/lib/docker/containers
```

# Reference
- https://docs.docker.com/storage/storagedriver/