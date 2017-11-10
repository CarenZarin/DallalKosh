# DallalKosh

## Development

+ Create a directory to contain the while project files (e.g. `Project`) and change your current directory to this one.

```bash
mkdir Project
cd Project
```

+ Clone this repository

```bash
git clone git@github.com:CarenZarin/DallalKosh.git
# Or
git clone https://github.com/CarenZarin/DallalKosh.git
```

+ Create a virtual environment (Read here if you don't know what a virtual environment is)

```bash
virtualenv --python python3 .
source bin/activate
```

+ Go to the project directory

```bash
cd DallalKosh
```

+ Install the project dependencies

```bash
pip install -r requirements.txt
```

+ Change the following line in `lib/python3.6/site-packages/guardian/compat.py`

```python
# Change line 13 to the following line
from django.conf.urls import *
```

+ Run the migration task

```bash
python manage.py makemigrations
python manage.py migrate
```

+ Run the development server

```bash
python manage.py runserver
```
