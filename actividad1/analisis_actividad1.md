1.	¿Qué responsabilidades distintas conviven en el archivo app.py?
En el archivo app.py coexisten de manera acoplada cuatro responsabilidades arquitectónicas distintas:
Persistencia de datos: Se gestiona el almacenamiento temporal a través de una lista estructurada en memoria
Enrutamiento y Control: Se definen los puntos de acceso y la interceptación de peticiones HTTP mediante los decoradores @app.route.
Lógica de Negocio: Se ejecutan operaciones de validación implícitas, tales como el cálculo incremental de identificadores únicos y la conversión de tipos de datos al añadir registros.
Presentación (Vista): Se realiza el renderizado de la interfaz de usuario insertando cadenas de texto HTML embebidas directamente en el valor de retorno de las funciones.

2. ¿Qué problemas podría enfrentar un equipo de cinco personas trabajando sobre este código?
El principal obstáculo operativo sería la alta incidencia de conflictos de fusión (merge conflicts) en el sistema de control de versiones, debido a que todo el equipo estaría modificando concurrentemente el mismo archivo físico (app.py). 
Adicionalmente, la ausencia de modularidad impide la distribución eficiente del trabajo en paralelo (por ejemplo, separar el diseño de las vistas del desarrollo lógico), elevando el riesgo de que los cambios introducidos por un desarrollador desestabilicen accidentalmente las funcionalidades de los demás.

3. ¿Qué ocurre si se desea cambiar el almacenamiento de una lista en memoria a una base de datos?
Debido al fuerte acoplamiento y a la inexistencia de una separación de capas, la migración hacia un motor de base de datos relacional obligaría a modificar directamente las funciones controladoras de las rutas en app.py. 
Esto implicaría reescribir los bloques de código destinados a la inserción y consulta en cada endpoint que interactúe con la variable productos, incrementando la probabilidad de introducir errores en la capa de presentación al alterar la lógica de persistencia.  

5. ¿Cómo se realizarían pruebas unitarias sobre la lógica de productos sin levantar el servidor?
Bajo esta estructura, la ejecución de pruebas unitarias puras es sumamente compleja. Debido a que las rutinas de manipulación del catálogo se encuentran ligadas de forma nativa al contexto de las solicitudes HTTP (request) y al ciclo de vida de la aplicación Flask, 
no es viable aislar e invocar estas funciones de manera independiente sin inicializar el entorno del framework o recurrir a técnicas avanzadas de simulación (mocking) para emular el comportamiento del servidor web.  
