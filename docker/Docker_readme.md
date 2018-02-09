# Docker
`/var/lib/docker/image/devicemapper/imagedb/content/sha256`
- Location of files stored on host : ` /var/lib/docker `
- Docker Image is an inert, immutable file that's a snapshot of a container.
- Image are created with the `build` command and produces a container when started with `run`.

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

## Build the app
- Be in the directory level that has Dockerfile, requirements.txt and app files
```
   $ docker build -t <image-name> <dir-to-Dockerfile>
```

- Check built images
```
    $ docker images
```

## Clean-up Docker entirely and start fresh
- If need to have clean slate of Docker environment, remove the Docker files and restart service
```
    $ rm -rf /var/lib/docker
    $ systemctl restart docker
```

# Running Docker
## Run the app
- Port 80 is set by Dockerfile EXPOSE variable
```
    $ docker run -p 4000:80 containername

    - Run app in background and terminal returns long container ID.
    $ docker run -d -p 4000:80 containername
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

- List all running containers
```
   $ docker container ls
   $ docker ps
```
- List all containers including non running containers
```
   $ docker container ls -a
   $ docker ps -a
```

- Remove all containers
`
   $ docker container rm $(docker container ls -a -q)
`
- Remove specific container on machine
`
   $ docker container rm <hash>
`



## Image Commands
- Export built image to run it elsewhere.
- A registry is a collection of repos and a repo is a collection of images. The Docker CLI uses Docker's public registry by default
- List all images on the machine
```
    $ docker image ls -a
```

- Inspect images
`
    $ docker inspect <tag or id>
    $ docker history <image-id>:latest
`

##### Repository Images
- Login with DockerID :
`   $ docker login `
- Pull an image from a repo :
`   $ docker pull `

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

##### Pull and run Image from remote repo
`
    $ docker run -p 4000:80 username/repository:tag
`

##### Remove Docker image
- Image cannot be removed via id if multiple image of same name, different tag exist. Image will need to be removed via name instead of id.

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
### Docker Compose
- Tool for defining and running multi-container Docker apps.
- Uses a YAML file to configure apps services and create/start all services from configuration.
`
    https://docs.docker.com/compose/compose-file/#dockerfile
`

- Require manual installation (check for latest version)
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

### Run App with docker compose
- Check is defined port in docker-compose.yml is already running other services and either change the port or stop the service.


- Starts Compose and runs your entire app
```
    $ docker-compose up
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
- A storage driver handles the details about the way these layers interact with each other.
- Each layer stored in its own directory in host local storage aread : `/var/lib/docker/<storage-drive>/layers/`


### Bind mounts
https://docs.docker.com/engine/admin/volumes/bind-mounts/#start-a-container-with-a-bind-mount
https://docs.docker.com/storage/storagedriver/
- To mount host machine's files or directory into a container.
- The file or directory is referenced by its full or relatives path on the host machine.

### Volume
- A new directory is created within Docker's storage directory on the host machine


## Docker with PostgreSQL














