# Django + PostgreSQL Docker Setup

This repository is a monorepo setup that contains a base API with Django and connects to a PostgreSQL database. Everything is setup to be able to easily run containerized instances of the API and database for local development.

### Prerequisites

List of software to be installed:
- Python
- Docker Desktop

### API Setup

Using a virtual environment is recommended for consistent local development.

```bash
cd backend
python -m venv venv
```

As a one time setup, you will need to install all the necessary packages to use FastAPI with Postgres.

```bash
pip install djangorestframework "psycopg[binary]" 
```

Alternatively, if `requirements.txt` already exists, you can install from that.

```bash
pip install -r requirements.txt
```

For any new packages, save them in the `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

### Database Migrations

When something relating to the database changes, you will need to create a new migration file. If running the API in a container, you will need to use `docker-compose exec` to do so.

```bash
docker-compose exec python manage.py makemigrations
```

Migrations have to be applied to the database in order to take effect.


```bash
docker-compose exec python manage.py migrate
```

### Docker

To run local instances of the API and database, run the containers (rebuild if necessary).

```bash
docker-compose up [--build] [-d]
```

To stop the services, run the following:

```bash
docker-compose down [-v]
```