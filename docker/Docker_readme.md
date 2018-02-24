# Docker
# Table of Content
## Create Docker Environment
- [Start up service](#start-up-service)
- [Create Dockerfile](#create-dockerfile)
- [Requirements file](#requirements-file)
- [Create / Build an Image](#create-/-build-an-image)
- [Check running host services](#check-running-host-services)
- [Check status](#check-status)

## Running Docker
- [Run the container](#run-the-container)
- [Container Commands](#container-commands)
- [Image Commands](#image-commands)

## Services
- [Docker Compose](#docker-compose)
- [Run Docker Compose](#run-docker-compose)
- [Storage driver](#storage-driver)
- [Data Volumes](#data-volumes)
- [Bind Mounts](#bind-mounts)

## Clean up Docker Environment
- [Clean-up Docker entirely and start fresh](#cleanup-to-freshstart)
- [Prune Containers](#prune-Containers)
- [Prune Images](#prune-Images)
- [Prune Everything](#prune-Everything)


`/var/lib/docker/image/devicemapper/imagedb/content/sha256`
- Location of files stored on host : ` /var/lib/docker `
- Docker Image is an inert, immutable file that's a snapshot of a container.
- Image are created with the `build` command and produces a container when started with `run`.
- Images are bound to containers, so remove containers before removing images

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
   $ docker build -t <image-name> <dir-to-Dockerfile>
```

- Check built images
```
    $ docker images
    or
    $ docker image ls -a
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

- Content served in web page: http://0.0.0.0:80 or http://localhost:4000

- Also able to cmd shell to view the same content
`
    $ curl http://localhost:4000
`

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

- Stop all running containers
```
    $ docker stop $(docker ps -aq)
```
- Remove all containers
```
   $ docker container rm $(docker container ls -a -q)
```
- Remove specific container on machine
```
   $ docker container rm <hash>
```

## Image Commands
- Built Images can be exported to run it elsewhere.
- A registry is a collection of repos and a repo is a collection of images. The Docker CLI uses Docker's public registry by default
- List all images on the machine
```
    $ docker image ls -a
```

- Inspect images
```
    $ docker inspect <tag or id>
    $ docker history <image-id>:latest
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


## Services
- A service only runs one image but codifies the way it is run - what ports to use, how many container replicas, etc.
- Service are defined via `docker-compose.yml` file.


### Docker Compose
- Tool for defining and running multi-container Docker apps.
- Uses a YAML file to configure apps services and create/start all services from configuration.
`
    https://docs.docker.com/compose/compose-file/#dockerfile
`

##### Require manual installation (check for latest version)
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

- Run one-off commands for services
```
    $ docker-compose run <service-cmd>
    $ docker-compose run web env
```

- Removes all containers
```
    $ docker-compose rm -v
```
- Docker-compose command line references : ` https://docs.docker.com/compose/reference/ `


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

## Images and layers
- Image is built up from series of layers, each layer represents an instruction in image Dockerfile.
- New container adds a writeable layer on top of the underlying image layers, called "container layer". Any changes made to running container ( add / modify / delete files) are written to the container layer.
- Deleting a container removes the container layer but the underlying image remains unchanged.
- Each container has its own container layer, multiple containers can share access to the same underlying image and have their own data state.

- Get approx size of container
```
    $ docker ps -s
    [
        size         : on disk used for writable layer of each container
        virtual size : read-only image data used by container + writeable layer size
    ]
```

### Storage driver
https://docs.docker.com/storage/storagedriver/
- A storage driver handles the details about the way these layers interact with each other.
- Each layer stored in its own directory in host local storage aread : `/var/lib/docker/<storage-drive>/layers/`

- Only files to be modified will be copied into the writeable layers. When files in container is modified, the storage driver performs a `copy-on-write` operation.

- For write-heavy apps, do not store data in container, instead use Docker volumes which are independent on the running container.


### Data Volumes (DV)
https://docs.docker.com/storage/volumes/
- Data written to container that is not stored in a `data volume` will be deleted when container is deleted.
- Data volume is a directory / file in host filesystem that is mounted directly into a container.
- Multiple DV can be mounted into a single container
- Multiple containers can share one or more DV.
- Location of DV are outside host local storage area

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