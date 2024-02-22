# proyecto-base  

## Tabla de contenido

- [Pre-requisitos para cada microservicio](#pre-requisitos-para-cada-microservicio)
- [Estructura de cada microservicio](#estructura-de-cada-microservicio)
  - [Archivos de soporte](#archivos-de-soporte)
  - [Carpeta src](#carpeta-src)
  	- [Carpeta domain](#carpeta-domain)
	- [Carpeta tests](#carpeta-tests)
- [Ejecutar un microservicio](#ejecutar-un-microservicio)
  - [Makefile](#makefile)
  - [Variables de entorno](#variables-de-entorno)
  - [Ejecutar el servidor](#ejecutar-el-servidor)
  - [Ejecutar pruebas](#ejecutar-pruebas)
  - [Ejecutar desde Dockerfile](#ejecutar-desde-dockerfile)
- [Ejecutar Docker Compose](#ejecutar-docker-compose)
- [Ejecutar Colección de Postman](#ejecutar-colección-de-postman)
- [Ejecutar evaluador github action workflow](#ejecutar-evaluador-github-action-workflow)
- [Resultados Entrega 1](#resultados-entrega-1)
  - [Covertura](#covertura)
  - [Evaluador](#evaluador)

## Pre-requisitos para cada microservicio
- Python ~3.10
- Docker
- Docker-compose
- Postman
- PostgreSQL
    - Las instrucciones pueden variar según el sistema operativo. Consulta [la documentación](https://www.postgresql.org/download/). Si estás utilizando un sistema operativo basado en Unix, recomendamos usar [Brew](https://wiki.postgresql.org/wiki/Homebrew).

## Estructura de cada microservicio
Cada microservicio utiliza Python y Flask para ejecutar el servidor, y pytest para ejecutar las pruebas unitarias. En general, dentro de cada uno de ellos hay una carpetas principal: `src`, así como algunos archivos de soporte.

#### Archivos de soporte
- `.coveragerc`: Este archivo configura las opciones de cobertura de código, permitiendo especificar qué archivos o directorios deben ser incluidos o excluidos de los informes de cobertura.
- `.env`: Archivo de plantilla Env utilizado para definir variables de entorno. Consulte la sección  **Variables de entorno**.
- `app.py`: Archivo principal que inicializa la lógica principal de la aplicación. Aquí se registan las rutas y la base de datos.
- `Dockerfile`: Definición para construir la imagen Docker del microservicio. Consulta la sección **Ejecutar desde Dockerfile**.
- `pytest.ini`: Archivo de configuración utilizado por pytest para personalizar el comportamiento de las pruebas, como la selección de complementos, el ajuste de opciones de informe y la exclusión de directorios específicos.
- `requiremets.txt`: Lista de dependencias de Python necesarias para la aplicación. Se utiliza comúnmente con herramientas como pip para instalar todas las dependencias necesarias en un entorno virtual.

### Carpeta src
Esta carpeta contiene el código y la lógica necesarios para declarar y ejecutar la API del microservicio, así como para la comunicación con la base de datos. Hay dos carpetas principales, así como algunos archivos de soporte:
- `/domain`: Define las rutas y los servicios del dominio, así como algunos archivos de soporte.
- `/tests`: Esta carpeta contiene las pruebas para los componentes principales del microservicio que han sido declarados en la carpeta `/domain`
- `model.py`: Contiene un modelo del dominio que realiza la configuración básica de una tabla e incluye las columnas `createdAt` y `updatedAt`.
- `scheme.py`: Define los esquemas de datos utilizados en la aplicación para validar las solicitudes entrantes y las respuestas salientes.
- `db.py`: Configura la conexión a la base de datos utilizando SQLAlchemy. Se define la URL de conexión utilizando las variables de entorno proporcionadas o los valores por defecto, y se crea el motor de la base de datos y la sesión local para interactuar con ella.

#### Carpeta domain
- `decorators.py`: Contiene dos decoradores: **handle_exceptions**, que maneja excepciones específicas generando respuestas HTTP adecuadas junto con mensajes de error personalizados, y **db_session**, que garantiza la creación y cierre apropiados de sesiones de base de datos alrededor de la función decorada para mantener la integridad de las transacciones y evitar fugas de recursos.
- `exceptions.py`: Define excepciones personalizadas utilizadas para manejar casos de error específicos en la aplicación. Cada excepción proporciona un mensaje descriptivo y hereda de la clase base Exception. Estas excepciones se utilizan para representar escenarios como parámetros inválidos, recursos inexistentes, falta de autorización, entre otros, facilitando la gestión uniforme de errores en la API.
- `routes.py`: Define las rutas de la API utilizando Flask. Cada ruta tiene asignado un método HTTP y una función asociada que maneja la solicitud. Las funciones decoradas con handle_exceptions gestionan posibles errores de manera uniforme, devolviendo respuestas adecuadas junto con los códigos de estado HTTP correspondientes.
- `services.py`: Contiene funciones para la lógica de negocio de la API, validación de datos y manejo de excepciones.
- `utils.py` Proporciona funciones utilitarias esenciales para la aplicación.

#### Carpeta tests
- `factory.py`: Proporciona funciones para crear modelos de dominio ficticios y generar grandes cantidades de prueba. Utiliza la biblioteca Faker para generar datos simulados.
- `test_<dominio>.py`: Proporciona funciones de pruebas de los servicios del dominio.

## Ejecutar un microservicio
En cada microservicio se encontrará la documentación de despliegue en la sesión **Run with Makefile**, que incluye instrucciones específicas para ser ejecutado.

### Makefile
El Makefile proporciona comandos convenientes para ejecutar el microservicio de forma fácil y rápida.

### Variables de entorno

El servidor Flask y las pruebas unitarias utilizan variables de entorno para configurar las credenciales de la base de datos y encontrar algunas configuraciones adicionales en tiempo de ejecución. A alto nivel, esas variables son:
- DB_USER: Usuario de la base de datos Postgres
- DB_PASSWORD: Contraseña de la base de datos Postgres
- DB_HOST: Host de la base de datos Postgres
- DB_PORT: Puerto de la base de datos Postgres
- DB_NAME: Nombre de la base de datos Postgres

Estas variables de entorno deben especificarse en `.env` de cada microservicio.

### Ejecutar el servidor
Una vez que las variables de entorno estén configuradas correctamente, para ejecutar el servidor utiliza el siguiente comando:
```bash
$> make run
```
En el caso que haga una modificación y requiera levantar todo de nuevo es recomentdado que ejecute **make clean_all** antes del anterio comando.

### Ejecutar pruebas
Para ejecutar las pruebas unitarias de los microservicios y establecer el porcentaje mínimo de cobertura del conjunto de pruebas en 70%, ejecuta el siguiente comando:
```bash
$> make test_all
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
