# proyecto-base  

## Tabla de contenido

- [Pre-requisitos para ejecución](#pre-requisitos-para-ejecución)
- [Estructura de cada microservicio](#estructura-de-cada-microservicio)
  - [Archivos de soporte](#archivos-de-soporte)
  - [Carpeta src](#carpeta-src)
  	- [Carpeta api](#carpeta-api)
    - [Carpeta config](#carpeta-config)
  	- [Carpeta transactions](#carpeta-transactions)
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
Cada microservicio utiliza Python y Flask para ejecutar el servidor. En general, dentro de cada uno de ellos hay una carpetas principal: `src`, así como algunos archivos de soporte. Para que comprenda lo anterior, dirijase a /transactionManagement.

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
- `/transactions`: Contiene los modulos definidos para el dominio de gestión de Transacciones.
- `/seedwork`: Contiene clases base que se usan como base para los dominios definidos.

#### Carpeta api
- `utils/decorators.py`: Contiene decoradores: **handle_exceptions**, que maneja excepciones específicas generando respuestas HTTP adecuadas junto con mensajes de error personalizados, y **db_session**, que garantiza la creación y cierre apropiados de sesiones de base de datos alrededor de la función decorada para mantener la integridad de las transacciones y evitar fugas de recursos. **is_authenticated** que valida si la petición contiene un token de autenticación.
- `utils/exceptions.py`: Define excepciones personalizadas utilizadas para manejar casos de error específicos en la aplicación. Cada excepción proporciona un mensaje descriptivo y hereda de la clase base Exception. Estas excepciones se utilizan para representar escenarios como parámetros inválidos, recursos inexistentes, falta de autorización, entre otros, facilitando la gestión uniforme de errores en la API.
- `transactions.py`: Define las rutas de la API utilizando Flask. Cada ruta tiene asignado un método HTTP y una función asociada que maneja la solicitud.

#### Carpeta config
- `db.py`: Proporciona una instancia para el acceso a las capacidades de la db.
- `uow.py`: Proporciona una abstracción de la unidad de trabajo.

#### Carpeta transactions
- `/`: Proporciona las capas de aplicación, dominio e infraestructura para el modulo de transacciones.

#### Carpeta seedwork
- Proporciona las capas de aplicación, dominio, infraestructura y presentación que contienen las bases que se usan para los dominios definidos.

## Ejecutar un microservicio
En cada microservicio se encontrará la documentación de despliegue en la sesión **Run with Makefile**, que incluye instrucciones específicas para ser ejecutado. En este orden de ideas, en la ruta transactionManagement encontrará un README.md donde se indica que la ejecución del docker se puede hacer a partir del comando `make run`.

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
- TOPIC: Nombre del topico al cual se va a conectar
- BROKER_HOST: Nombre del contenedor o servidor que contiene Apache Pulsar

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
		"_postman_id": "91aa6331-6442-4764-a467-1db15562556a",
		"name": "Transactions_DDD",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "12463581"
	},
	"item": [
		{
			"name": "http://localhost:3002/transactions/add",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"dni_landlord\":\"1040789546\", \r\n    \"dni_tenant\": \"34567921\",\r\n    \"monetary_value\": 1250000.9,\r\n    \"type_lease\": \"Arriendo Mensual\",\r\n    \"contract_initial_date\": \"20210923\",\r\n    \"contract_final_date\": \"2024-09-23\"   \r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:3002/transactions/add",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "3002",
					"path": [
						"transactions",
						"add"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://localhost:3002/transactions/addCommand",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"dni_landlord\":\"1040789546\", \r\n    \"dni_tenant\": \"34567921\",\r\n    \"monetary_value\": 1250000.9,\r\n    \"type_lease\": \"Arriendo Mensual\",\r\n    \"contract_initial_date\": \"20210923\",\r\n    \"contract_final_date\": \"2024-09-23\"   \r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://localhost:3002/transactions/addCommand",
					"protocol": "http",
					"host": [
						"localhost"
					],
					"port": "3002",
					"path": [
						"transactions",
						"addCommand"
					]
				}
			},
			"response": []
		}
	]
}
```