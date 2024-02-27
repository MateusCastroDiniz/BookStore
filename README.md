# Bookstore app
A Bookstore app from Backend Python course from EBAC

# System Prerequisites
* Python >=3.9
* Poetry
* Docker + Docker-Compose

## Quick Start (on linux)
At the end of this step by step quick start your device must be able to run the project in <a href='localhost:8000/bookstore'>localhost:8000/bookstore</a> path.
1. Clone this project:
```shell
git clone git@github.com:MateusCastroDiniz/dCasa.git
```
2. Install dependences:
```shell
cd projeto_bookstore
poetry install
```
3. Run project:
```shell
make quick-start
```
4. Run tests:
```shell
make test
```

## Quick Start (Windows/MacOs)
At the end of this step by step quick start your device must be able to run the project in <a href='localhost:8000/bookstore'>localhost:8000/bookstore</a> path.
1. Clone this project:
```shell
git clone git@github.com:MateusCastroDiniz/dCasa.git
```
2. Install dependences:
```shell
cd projeto_bookstore
poetry install
```
3. Run local dev server:
```shell
poetry run python manage.py migrate
poetry run python manage.py runserver
```
4. Build the project with Docker:
```shell
docker-compose up -d --build
docker-compose exec web python manage.py migrate
```