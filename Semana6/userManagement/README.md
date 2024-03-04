# USERS MICROSERVICE

## Microservice structure
```bash
├── Dockerfile
├── README.md
├── __init__.py
├── app.py
├── pytest.ini
├── requirements.txt
└── src
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── auth.py
    │   ├── users.py
    │   └── utils
    │       ├── __init__.py
    │       ├── decorators.py
    │       └── exceptions.py
    ├── config
    │   ├── __init__.py
    │   ├── db.py
    │   └── uow.py
    ├── modules
    │   ├── __init__.py
    │   ├── auth
    │   │   ├── __init__.py
    │   │   ├── application
    │   │   │   ├── __init__.py
    │   │   │   ├── commands
    │   │   │   │   ├── __init__.py
    │   │   │   │   ├── base.py
    │   │   │   │   └── register_credential.py
    │   │   │   ├── dto.py
    │   │   │   ├── handlers.py
    │   │   │   ├── mappers.py
    │   │   │   └── queries
    │   │   │       ├── __init__.py
    │   │   │       ├── authenticate_user.py
    │   │   │       └── base.py
    │   │   ├── domain
    │   │   │   ├── __init__.py
    │   │   │   ├── entities.py
    │   │   │   ├── events.py
    │   │   │   ├── factories.py
    │   │   │   ├── repositories.py
    │   │   │   └── rules.py
    │   │   └── infrastructure
    │   │       ├── __init__.py
    │   │       ├── dto.py
    │   │       ├── exceptions.py
    │   │       ├── factories.py
    │   │       ├── mappers.py
    │   │       ├── repositories.py
    │   │       └── utils.py
    │   └── users
    │       ├── __init__.py
    │       ├── application
    │       │   ├── __init__.py
    │       │   ├── commands
    │       │   │   ├── __init__.py
    │       │   │   ├── base.py
    │       │   │   └── save_personal_information.py
    │       │   ├── dto.py
    │       │   ├── handlers.py
    │       │   └── mappers.py
    │       ├── domain
    │       │   ├── __init__.py
    │       │   ├── entities.py
    │       │   ├── events.py
    │       │   ├── factories.py
    │       │   └── repositories.py
    │       └── infrastructure
    │           ├── __init__.py
    │           ├── dto.py
    │           ├── exceptions.py
    │           ├── factories.py
    │           ├── mappers.py
    │           └── repositories.py
    └── seedwork
        ├── __init__.py
        ├── application
        │   ├── __init__.py
        │   ├── commands.py
        │   ├── dto.py
        │   ├── handlers.py
        │   └── queries.py
        ├── domain
        │   ├── __init__.py
        │   ├── entities.py
        │   ├── events.py
        │   ├── exceptions.py
        │   ├── factories.py
        │   ├── mixins.py
        │   ├── repositories.py
        │   └── rules.py
        ├── infraestructure
        │   ├── __init__.py
        │   └── uow.py
        └── presentation
            ├── __init__.py
            └── api.py
```

## Microservice documentation
### Endpoints
- `POST /auth/signup` - Create a new Credential and User
- `POST /auth/signin` - Generate a new token from user
- `PATCH /users/register` - Create a new User (used for testing)

## Requirements
- Python = 3.10
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

# Make sure that you have a postgres database running

# run users microservice tests
docker run users pytest
```
