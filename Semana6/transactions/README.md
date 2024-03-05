# proyecto-base  

## Tabla de contenido

- [Pre-requisitos para ejecución](#pre-requisitos-para-ejecución)
- [Estructura de cada microservicio](#estructura-de-cada-microservicio)
  - [Archivos de soporte](#archivos-de-soporte)
  - [Carpeta src](#carpeta-src)
  	- [Carpeta api](#carpeta-api)
    - [Carpeta config](#carpeta-config)
  	- [Carpeta modules](#carpeta-modules)
  	- [Carpeta seedwork](#carpeta-seedwork)
- [Ejecutar un microservicio](#ejecutar-un-microservicio)
  - [Makefile](#makefile)
  - [Variables de entorno](#variables-de-entorno)
  - [Ejecutar el servidor](#ejecutar-el-servidor)
  - [Ejecutar desde Dockerfile](#ejecutar-desde-dockerfile)
- [Ejecutar Docker Compose](#ejecutar-docker-compose)
- [Ejecutar Colección de Postman](#ejecutar-colección-de-postman)


## Pre-requisitos para ejecución
- Docker
- Docker-compose
- Make
    - Las instrucciones pueden variar según el sistema operativo. Consulta [para Windows](https://gnuwin32.sourceforge.net/packages/make.htm). Si estás utilizando un sistema operativo basado en Unix, recomendamos usar [Brew](https://wiki.postgresql.org/wiki/Homebrew) con el commando `brew install make`.

## Estructura de cada microservicio
Cada microservicio utiliza Python y Flask para ejecutar el servidor. En general, dentro de cada uno de ellos hay una carpetas principal: `src`, así como algunos archivos de soporte. Para que comprenda lo anterior, dirijase a /userManagement.

#### Archivos de soporte
- `.env`: Archivo de plantilla Env utilizado para definir variables de entorno. Consulte la sección  **Variables de entorno**.
- `app.py`: Archivo principal que inicializa la lógica principal de la aplicación. Aquí se registan las rutas y la base de datos.
- `Dockerfile`: Definición para construir la imagen Docker del microservicio. Consulta la sección **Ejecutar desde Dockerfile**.
- `pytest.ini`: Archivo de configuración utilizado por pytest para personalizar el comportamiento de las pruebas, como la selección de complementos, el ajuste de opciones de informe y la exclusión de directorios específicos.
- `requiremets.txt`: Lista de dependencias de Python necesarias para la aplicación. Se utiliza comúnmente con herramientas como pip para instalar todas las dependencias necesarias en un entorno virtual.

### Carpeta src
Esta carpeta contiene el código y la lógica necesarios para declarar y ejecutar la API del microservicio, así como para la comunicación con la base de datos. Hay cuatro carpetas principales:
- `/api`: Define las rutas y los servicios del dominio, así como algunos archivos de soporte.
- `/config`: Esta carpeta contiene los archivos para la configuración de `db` y `uow`.
- `/modules`: Contiene los modulos definidos para el dominio de gestión de usuarios. Estos son auth y users.
- `/seedwork`: Contiene clases base que se usan como base para los dominios definidos.

#### Carpeta api
- `utils/decorators.py`: Contiene decoradores: **handle_exceptions**, que maneja excepciones específicas generando respuestas HTTP adecuadas junto con mensajes de error personalizados, y **db_session**, que garantiza la creación y cierre apropiados de sesiones de base de datos alrededor de la función decorada para mantener la integridad de las transacciones y evitar fugas de recursos. **is_authenticated** que valida si la petición contiene un token de autenticación.
- `utils/exceptions.py`: Define excepciones personalizadas utilizadas para manejar casos de error específicos en la aplicación. Cada excepción proporciona un mensaje descriptivo y hereda de la clase base Exception. Estas excepciones se utilizan para representar escenarios como parámetros inválidos, recursos inexistentes, falta de autorización, entre otros, facilitando la gestión uniforme de errores en la API.
- `auth.py` y `users.py`: Define las rutas de la API utilizando Flask. Cada ruta tiene asignado un método HTTP y una función asociada que maneja la solicitud.

#### Carpeta config
- `db.py`: Proporciona una instancia para el acceso a las capacidades de la db.
- `uow.py`: Proporciona una abstracción de la unidad de trabajo.

#### Carpeta modules
- `/auth`: Proporciona las capas de aplicación, dominio e infraestructura para el modulo de autenticación.
- `/users`: Proporciona las capas de aplicación, dominio e infraestructura para el modulo de users.

#### Carpeta seedwork
- Proporciona las capas de aplicación, dominio, infraestructura y presentación que contienen las bases que se usan para los dominios definidos.

## Ejecutar un microservicio
En cada microservicio se encontrará la documentación de despliegue en la sesión **Run with Makefile**, que incluye instrucciones específicas para ser ejecutado. En este orden de ideas, en la ruta userManagement encontrará un README.md donde se indica que la ejecución del docker se puede hacer a partir del comando `make run`.

### Makefile
El Makefile proporciona comandos convenientes para ejecutar el microservicio de forma fácil y rápida.

### Variables de entorno

El servidor Flask y las pruebas unitarias utilizan variables de entorno para configurar las credenciales de la base de datos y encontrar algunas configuraciones adicionales en tiempo de ejecución. A alto nivel, esas variables son:
- DB_USER: Usuario de la base de datos Postgres
- DB_PASSWORD: Contraseña de la base de datos Postgres
- DB_HOST: Host de la base de datos Postgres
- DB_PORT: Puerto de la base de datos Postgres
- DB_NAME: Nombre de la base de datos Postgres
- PYTHONUNBUFFERED: Habilita el debugging de python

Estas variables de entorno deben especificarse en `.env` de cada microservicio.

### Ejecutar el servidor
Una vez que las variables de entorno estén configuradas correctamente, para ejecutar el servidor utiliza el siguiente comando:
```bash
$> make run
```
En el caso que haga una modificación y requiera levantar todo de nuevo es recomentdado que ejecute **make clean_all** antes del anterio comando.

### Ejecutar desde Dockerfile
Para construir la imagen del Dockerfile en la carpeta, ejecuta el siguiente comando:
```bash
$> docker build -t <NOMBRE_DE_LA_IMAGEN> .
```
Y para ejecutar esta imagen construida, utiliza el siguiente comando:
```bash
$> docker run <NOMBRE_DE_LA_IMAGEN>
```

## Ejecutar Docker Compose
Para ejecutar todos los microservicios al mismo tiempo, utilizamos docker-compose para declarar y configurar cada Dockerfile de los microservicios. Para ejecutar docker-compose, utiliza el siguiente comando:
```bash
$> docker-compose -f "<RUTA_DEL_ARCHIVO_DOCKER_COMPOSE>" up --build

# Ejemplo
$> docker-compose -f "docker-compose.yml" up --build
```

## Ejecutar Colección de Postman
Importe la siguiente colección:
```
{
	"info": {
		"_postman_id": "b32f1f41-e581-4d87-9c7c-aa705f5d203f",
		"name": "DDD_without_cookies",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "6293622"
	},
	"item": [
		{
			"name": "Register user",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"username\": \"jorcasca\",\r\n    \"password\": \"jorcasca\",\r\n    \"email\": \"jorcasca@gmail.com\",\r\n    \"dni\": \"1107097248\",\r\n    \"fullName\": \"Jorge Eliecer Castaño Valencia\",\r\n    \"phoneNumber\": \"3166186895\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:3000/auth/signup",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "3000",
					"path": [
						"auth",
						"signup"
					]
				}
			},
			"response": []
		},
		{
			"name": "Authenticate user",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "{{USER_TOKEN}}",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"username\": \"jorcasca\",\n    \"password\": \"jorcasca\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:3000/auth/signin",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "3000",
					"path": [
						"auth",
						"signin"
					]
				}
			},
			"response": []
		},
		{
			"name": "Save personal info",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"id_credential\": \"05fca023-4710-4497-86d9-78f60db8b5dd\",\r\n    \"email\": \"jorcasca2@gmail.com\",\r\n    \"dni\": \"1234567890\",\r\n    \"fullName\": \"Jorge 2 \",\r\n    \"phoneNumber\": \"1234567890\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:3000/users/register",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "3000",
					"path": [
						"users",
						"register"
					]
				}
			},
			"response": []
		}
	],
	"variable": [
		{
			"key": "USER_TOKEN",
			"value": "{{USER_TOKEN}}"
		}
	]
}
```