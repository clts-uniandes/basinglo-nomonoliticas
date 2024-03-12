# Contenidos Semana 6

Se generan los siguientes items para el entregable de esta semana, para el proyecto Propiedad de los Alpes:

1. Carpetas con el código fuente de cada microservicio propuesto para los experimentos de arquitectura:
   * bff-web: Contiene aplicación Backend For Front pensado para web. Requerido en uno de los experimentos. 
   * notifications: Servicio de notificaciones; operación parcial ya que una versión más completa está asociada a la ejecución de uno de los experimentos (Mantenibilidad 3).
   * propertiesManagement: Servicio de propiedades; requerido para Sagas y experimentación.
   * transactions: Servicio de transacciones;  requerido para Sagas y experimentación.
   * userManagement: Copia de servicio de gestión de usuarios y autenticación de los mismos; requerido en experimentos
2. Carpeta `Documentación` que trae documentación sobre las decisiones de arquitectura hechas y patrones + tácticas elegidos.
3. Carpeta `pulsar` para archivar esquemas Avro de mensajes que abstraen eventos de arquitectura. Se tendrá una versión completa cuando se habiliten Sagas.

Cada carpeta de microservicio incluye su propio README.md para instrucciones de montado y despliegue individual.