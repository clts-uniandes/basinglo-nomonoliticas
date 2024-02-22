# USERS MICROSERVICE

## Microservice structure
```bash
├───src/
│   ├───domain/
│   │   ├───decorators.py
│   │   ├───exceptions.py
│   │   ├───routes.py
│   │   ├───services.py
│   │   └───utils.py
│   ├───tests/
│   ├───db.py
│   ├───models.py
│   ├───schema.py
├───.env
├───app.py
├───Dockerfile
├───requirements.txt
└───README.md
```
### Structure description
- `domain` - contains all the business logic of the microservice
- `domain/decorators.py` - contains decorators for the microservice
- `domain/exceptions.py` - contains custom exceptions for the microservice
- `domain/routes.py` - contains all the routes of the microservice
- `domain/services.py` - contains all the services of the microservice
- `domain/utils.py` - contains all the utilities of the microservice
- `test` - contains all the tests of the microservice
- `db.py` - contains the database connection of the microservice
- `models.py` - contains the model of the microservice
- `schema.py` - contains the schemas of the microservice
- `.env` - contains the environment variables of the microservice
- `app.py` - contains the main application of the microservice
- `Dockerfile` - contains the docker configuration of the microservice
- `requirements.txt` - contains the dependencies of the microservice
- `README.md` - contains the documentation of the microservice

## Microservice documentation
### Endpoints
- `POST /users` - Create a new User
- `POST /users/auth` - Generate a new token from user
- `PATCH /users/<id>` - Update a user
- `GET /users/me` - Get information User. Necesary a token into headers
- `POST /users/reset` - reset the database
- `GET /users/ping` - returns the health of the microservice

## Requirements
- Python >= 3.9
- PostgreSQL >= 12
- Docker

## How to run
It's recommended to use the Makefile commands to run the microservice. If you don't have `make` installed, you can run the commands manually.

First, you have to make sure that you have a `.env` file in the root directory of the microservice.
Then, you have to fill the environment variables with the correct values and a postgres database running.

### Run with Makefile
To run the microservice with the Makefile, you have to run the following commands:
```bash
# run users microservice with Makefile (listening on port 8002)
cd ..
make run_users
```
### Run with Docker
To run the microservice with Docker, you have to run the following commands:
```bash
# build users microservice
docker build -t users .

# Make sure that you have a postgres database running

# run users microservice
docker run -p 3000:8000 users python app.py
```

## How to test
It's recommended to use the Makefile commands to test the microservice. If you don't have `make` installed, you can run the commands manually.

### Test with Makefile
To test the microservice with the Makefile, you have to run the following commands:
```bash
# run users microservice tests with Makefile
cd ..
make users_tests
```
### Test with Docker
To test the microservice with Docker, you have to run the following commands:
```bash
# build users microservice
docker build -t users .

# Make sure that you have a postgres database running

# run users microservice tests
docker run users pytest
```
