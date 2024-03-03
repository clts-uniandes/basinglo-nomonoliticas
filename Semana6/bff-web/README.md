# Descripción del proyecto

Este proyecto es una aplicación sencilla para representar el patrón Backend For FrontEnd. En este caso, está pensada para uso de aplicaciones
web. Donde se ofrecen las operacion que encontrará dentro del archivo Postman Collections adjunto a este README. En particular:

- Crear transacción - tipo compra (operación asíncrona)
- Consultar transacciones (síncrona) - IN DEVELOPMENT
- Login a plataforma (síncrona)
- Chequeo de salud.

Para más información, consultar el Postman Collections ya mencionado.

# Iniciar servidor FastAPI (local)

Prerequisito: Python 3.10 en adelante, e instalador de paquetes pip.

1. (Recomendado) Cree un entorno virtual Python para instalar las dependencias del proyecto con venv: `python -m venv .envname`
2. Active el entorno según su OS. Para el caso Windows: ``. Más información de otros OS en: https://docs.python.org/3/library/venv.html#how-venvs-work
3. Instale las dependencias con pip: `pip install -r requirements.txt` o `pip3 install -r requirements.txt`, según su entorno
4. Arranque el servidor usando vunicorn: `uvicorn main:app --host 0.0.0.0 --port 8000`

# Iniciar con docker-compose (recomando si no cuenta con un nodo Pulsar gestionado)

Instale Docker en su sistema, luego `docker-compose up`.

# Conectarse a consola de comandos de un container

`docker exec -it <container-id> bash`

Puede usar Docker Desktop para facilitar la recuperación del id, o usar `docker ps -a` para recuperar el id. Por ejemplo, (busque `bff-web-broker_pulsar-x`
en caso de usar Docker Compose.

# Requerimientos Apache Pulsar

Sea que levante de forma individual la aplicación (local o container solitario) o con docker-compose, debe tener en cuenta las siguientes precauciones:

1. Apache Pulsar toma mucho más tiempo en cold start, comparado al servidor BFF-FastAPI. Este último es casi instantáneo en unidades SSD (un par de
   segundos) mientras que Pulsar toma hasta 10 segundos (más si usa un disco duro). La suscripción de FastAPI fallará si el cluster de Pulsar no está listo
   por este tema. En caso de usar compose, simplemente reinicie el nodo BFF. `docker restart bff-web-bff-web-x`. Donde x es asignado por Compose.
2. Dependiendo de que configuración maneje en Pulsar, sus topicos pueden ser borrados automáticamente (). De ser así, verifique que su tópico esté listo
   siguiendo los comandos descritos en la sección "Comandos pulsar-admin"

# Comandos pulsar-admin

Los siguientes comandos están disponible por defecto en pulsar-admin, herramienta precarcada en folder `bin` de una instalación Apache Pulsar.

Crear tenant Pulsar:

`bin/pulsar-admin tenants create my-tenant`

Crear namespace:

`bin/pulsar-admin namespaces create my-tenant/my-namespace`

Crear tópico particionado; no recomendado en entornos de prueba ya que no podrá hacer peek al tópico:

`bin/pulsar-admin topics create-partitioned-topic my-tenant/my-namespace/my-topic -p numberofpartitions`

Crear tópico no particionado:

`bin/pulsar-admin topics create persistent://my-tenant/my-namespace/my-topic`

Listar tópicos particionados:

`bin/pulsar-admin topics list-partitioned-topics apache/pulsar`

Listar tópicos (no particionados):
`bin/pulsar-admin topics list apache/pulsar`

Tenga en cuenta que por defecto Pulsar puede eliminar tópicos no particionados para ahorro de espacio.

Más información en https://pulsar.apache.org/docs/3.1.x/admin-api-topics/
