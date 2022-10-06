
# CinList 
![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?)
![GitHub Hacktoberfest combined status](https://img.shields.io/github/hacktoberfest/2022/akshayitzme/cinlist?)
![GitHub contributors](https://img.shields.io/github/contributors/akshayitzme/cinlist?)
![Stars](https://img.shields.io/github/stars/akshayitzme/cinlist?logo=appveyor)
![Forks](https://img.shields.io/github/forks/akshayitzme/cinlist?logo=appveyor)
![Issues](https://img.shields.io/github/issues/akshayitzme/cinlist?logo=appveyor)

## Installation

**Method:1 Using Poetry**
``` pip install poetry```
```bash
poetry install
```
**Method: 2 Using pip**

 ```bash
 pip install -r requirements.txt
 ```

## Running
**Method: 1 Gunicorn**
```bash
gunicorn config.wsgi
```

**Method: 2 Django Development Server**
```bash
python manage.py runserver
```
