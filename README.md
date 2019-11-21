# SimpleSurvey
一个简单的survey系统，使用Django, Bootstrap, DataTables, jQuery等语言和库开发。

### Environment

- Python3
- django
- gunicorn
- mysqlclient
- MySQL 
- Nginx

### Docker

```
$ cd /usr/src 
$ mkdir app && cd app
$ git clone https://github.com/xshen1898/SimpleSurvey.git
$ cd SimpleSurvey/docker
$ docker-compose up -d
$ docker exec -it simplesurvey /bin/bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

### Screenshot

![create_question](https://raw.githubusercontent.com/xshen1898/SimpleSurvey/master/survey/static/images/create_question.png "create_question")
