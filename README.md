## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [Setup](#setup)
* [Additional informations](#additional-informations)
## General info
CrowVOD is an online application created with Python 3.6 and Django 3.1 that allows user to buy and watch a movie. 

## Requirements:
```
Python version 3.6
Django version 3.1
```
## Setup:

First of all, clone the repository. 
```
$ git clone https://github.com/antivancrow/vod
```

To install required python packages:
```
$ pip install -r requirements.txt
```

To launch the project run command:
```
$ python manage.py runserver
```

And then open the page below in an Internet browser. 
```
$ http://127.0.0.1:8000 
```

### Docker

You can run project from docker:
```
docker build . -t vod
docker run -p 8000:8000 -it vod
```

## Additional informations
List with all available movies:
```
$ http://127.0.0.1:8000
```
Log in to the application:
```
$ http://127.0.0.1:8000/login
```
Movie ID in a database
```
$ http://127.0.0.1:8000/{id}
```
This page plays the movie. 
```
$ http://127.0.0.1:8000//{id}/watch
```
Admin panel
```
$ http://127.0.0.1:8000/admin 
```

Credentials for user:
```
username: test, password: Zaq12wsx?
``` 
