# Django开发环境部署

## 创建python虚拟环境

`mkdir django && cd django`

使用命令`python -m venv ./venv`在当前目录的venv目录下创建python的虚拟环境

```shell
#当前目录结构
../django
`-- venv
    |-- bin
    |-- include
    |-- lib
    `-- lib64 -> lib
```

虚拟环境创建完成后需要使用命令`source ./venv/bin/activate`去激活虚拟环境

## 创建django项目

### 安装django

使用pip包管理器安装django库`pip install django`

### 创建django-project

使用命令`django-admin startproject dashborad`创建一个名为dashboard的django-project

进入到项目目录中`cd dashborad`

```shell
#当前目录结构
./
|-- dashborad
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-36.pyc
|   |   |-- settings.cpython-36.pyc
|   |   |-- urls.cpython-36.pyc
|   |   `-- wsgi.cpython-36.pyc
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

### 创建django-app

使用命令`django-admin startapp app`创建一个名为app的django-app

```shell
#当前目录结构
./
|-- app
|   |-- admin.py
|   |-- apps.py
|   |-- __init__.py
|   |-- migrations
|   |   `-- __init__.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- dashborad
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-36.pyc
|   |   |-- settings.cpython-36.pyc
|   |   |-- urls.cpython-36.pyc
|   |   `-- wsgi.cpython-36.pyc
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

## 连接mysql数据库

### 创建数据库

MariaDB [(none)] > CREATE DATABASE dashboard;

### 修改django数据库配置

```shell
#打开dashborad下的settings.py文件
vim ./dashborad/settings.py
#修改数据库连接配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashborad',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 安装pymysql连接库

使用pip包管理器安装django库`pip install pymysql`

```shell
#打开dashborad下的__init__.py文件
vim ./dashborad/__init__.py
#添加配置
import pymysql
pymysql.install_as_MySQLdb()
```
## 修改django的访问权限
```shell
#打开dashborad下的settings.py文件
vim ./dashborad/settings.py
ALLOWED_HOSTS = ['*']
```



```shell
#初始化django数据表
python manage.py migrate
#创建django-admin的超级用户
python manage.py createsuperuser
#运行django项目
python manage.py runserver 0.0.0.0:8000
```

开启浏览器后输入URL：http://127.0.0.1:8000/admin/

即可访问admin后台管理页面