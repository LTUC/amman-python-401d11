```Docker documentation```:
```
https://docs.docker.com/engine/reference/commandline/cli/
```

- to show you a list of commands available 
    ```
    docker help 
    ``` 
- to run already existed image pulled from docker hub called 'hello-world'
    ```
    docker run hello-world
    ``` 
- it will run already existed image pulled from docker hub called 'ubuntu' that contains ubuntu installed as OS
    ```
    docker run -it ubuntu bash
    ```

-  to exit the container
    ```
    exit 
    ```
- to build the docker image
    ```
    docker build .
    ``` 



## how should you  start :
1- create **Dockerfile** (to build the image ) with this content

```
FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```
2- create ```docker-compose`.yml``` (to build the container):
```
version: '3'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```
3- create your project (in our case django project)

4- 
    ```
     pip freeze > requirements.txt
    ```

5- ```docker-compose up``` 

to build the docker container and run the image and pull the project inside it 

-----
## to sign in to docker from CLI and push docker image :
1-
 ```
docker login
``` 


2- 
 ```
 docker tag <image name> <DOCKERHUB_USERNAME>/<container name> 
 ```


3- 
 ``` 
docker  push <DOCKERHUB_USERNAME>/<container name>
```
