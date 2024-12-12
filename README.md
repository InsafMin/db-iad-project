# Async Library Management System with FastAPI, SQLAlchemy Postgres, Alembic, Docker
___
This is a prototype of a simple Web REST API built with [FastAPI](https://fastapi.tiangolo.com/) and an async Postgres database. To connect to the database, [SQLAlchemy 2.0](https://docs.sqlalchemy.org/en/20/) and [Asyncpg](https://magicstack.github.io/asyncpg/current/) are used. [Alembic](https://alembic.sqlalchemy.org/en/latest/index.html) is used for migrations.

To set up the connection to the database and launch the API, use docker-compose.
## Getting Started
___
### Installing
First, make sure you have the latest version of Docker.

Then, to get this repository from GitHub and open the project folder, do this:
```
git clone https://github.com/InsafMin/library_management_api
cd library_management_api
```
### Applying Database Migrations
Before launching the docker container, you need to apply all migrations
* Create new migration:
```
docker-compose run backend alembic revision --autogenerate -m "New migration"
```
This will try to capture the newest changes automatically.
Check that the changes were correctly mapped by looking into 
the revision file in `/app/alembic/versions`.
* Apply migrations:
```
docker-compose run backend alembic upgrade head
```
### Launch with Docker
To work with this section you must have docker and docker-compose tools installed. To run the program, spin up the containers with:
```
docker-compose up
```
If this is the first time bringing up the project, you need to build the images first:
```
docker-compose up --build
```
### Web Routes & Documentation
All routes are available on /docs. In your browser, navigate to
```
http://0.0.0.0:8000/docs
```
