- [Qué vamos a valorar](#qué-vamos-a-valorar)
- [Introducción](#introducción)
  - [Casos de uso a cubrir](#casos-de-uso-a-cubrir)
    - [Reporte 1](#reporte-1)
    - [Reporte 2](#reporte-2)
    - [Reporte 3](#reporte-3)
- [Requisitos mínimos de la prueba](#requisitos-mínimos-de-la-prueba)
- [Para nota](#para-nota)
- [¿Cómo entregar la prueba?](#cómo-entregar-la-prueba)

# Qué vamos a valorar

Desde nuestro punto de vista no existen pruebas bien hechas o pruebas mal hechas. Nos interesa entender cómo piensas, cómo afrontas los problemas y cómo adquieres conocimientos. Si tienes cualquier duda estamos a tu disposición.

Vamos a valorar que la solución planteada esté bien documentada y que seamos capaces de ejecutar tu solución “sin pensar”.

Vamos a valorar **mucho** cómo has llegado a la solución que nos propones. Documenta el proceso que has seguido y las urls de las páginas o libros que has utilizado.

No establecemos qué lenguaje, herramienta o framework tienes que utilizar, elige el camino que prefieras y dinos por qué lo has elegido. En nuestro día a día, los lenguajes que usamos son Python, PHP y JS, para nosotros es más sencillo validar tu prueba en alguno de estos lenguajes.

Si por tus conocimientos no eres capaz de realizar el 100% de la prueba, ¡no te frustres! Llega hasta el punto que seas capaz. Explica las decisiones que has tomado y los problemas que te has encontrado.

# Introducción

Trabajamos como backend developer en la empresa Papas ACME, S.A. El departamento financiero aún tiene la necesidad de a partir de la información que tiene de clientes, productos e informes poder generar una serie de reportes. Por desgracia, el departamento no está excesivamente digitalizado y continúan trabajando con XLS, tras negociar con ellos hemos conseguido que exporten sus datos a ficheros CSV.

Esta es la estructura que hemos definido conjuntamente para cada una de las entidades.

| Fichero | customers.csv | products.csv | orders.csv |
|---------|---------------|--------------|------------|
| Que contiene | Información de clientes |Información de productos |Información de pedidos| 
| Columnas del fichero: |-`id` ID numérico que identifica al cliente <br>- `firstname` Nombre<br>-`lastname` Apellidos |-`id` ID numérico que identifica el producto<br>-`name` Nombre del producto<br>-`cost` Precio del producto en euros|-`id` ID numérico que identifica el pedido<br>-`customer` ID del cliente que hizo el pedido<br>-`products` Listado de ID’s de productos que ha comprado un cliente en el pedido.
|Fichero|[customers.csv](customers.csv)|[products.csv](products.csv)|[orders.csv](orders.csv)|
 
## Casos de uso a cubrir

Nuestros compañeros del departamento, nos presentan tres casos de uso que generarán distintos reportes de información a partir de unos ficheros que se suben a la plataforma.

### Reporte 1

El equipo de ventas quiere saber el total de cada pedido. Debe generar un fichero llamado “order_prices.csv” con las siguientes columnas: 

id: ID del pedido

total: Total del pedido en euros

### Reporte 2

El equipo de marketing quiere saber que clientes han comprado cada producto. Debe generar un fichero llamado “product_customers.csv” con las siguientes columnas: 

id: ID del producto

customer_ids: Lista de todos los ID’s que han comprado ese producto (Separados por un espacio)

### Reporte 3

 Para evaluar a los clientes, necesitamos un fichero que contenga todos los pedidos ordenados descendentemente por el total en euros:

Debe generar un fichero llamado “customer_ranking.csv" con las siguientes columnas: 

id: ID del cliente

name: Nombre del cliente

lastname: Apellidos del cliente

total: Total en euros que el cliente ha comprado en productos.

Las columnas deben ir correctamente identificadas con el nombre de cada columna en la primera fila de los ficheros.

# Requisitos mínimos de la prueba

* Desarrolla una aplicación que utilizando como parámetros de entrada los tres ficheros suministrados customers.csv, products.csv y orders.csv genere los tres reportes solicitados.

* No es necesario que construyas un frontend, es una prueba de backend. Es suficiente con tener un comando en consola que recoja la entrada y genere los archivos de salida.

* Decíamos en el primer apartado de la prueba que vamos a valorar como documentes la prueba, puedes crear un fichero readme.md con los pasos que tenemos que dar para ejecutar tu prueba en local.

# Para nota

Además de los requisitos mínimos para la prueba, hemos definido una serie de requisitos adicionales para que puedas lucirte

* **Testing.** No es imprescindible, pero si vienes con nosotros vas a tener que aprender a testear tu código, puede ser un buen momento para empezar.

* **API.** Implementar la aplicación como un API que permita subir los ficheros, generar los resultados y descargarlos.

* **Docker.** Nos gustaría que toda la prueba y sus dependencias se ejecutaran dentro de un contenedor y así nuestros compañeros de departamento solo necesitarán Docker en su día a día.

* **Frontend.** Cómo decíamos no es un requisito, pero si te animas seguro que para nuestros compañeros es más sencillo utilizar la aplicación a través de un formulario web.

# ¿Cómo entregar la prueba?

Tendrás que publicar tu prueba en un repositorio público, github por ejemplo.

Documenta en el repositorio el proceso que has seguido y las fuentes que has utilizado para documentarte, es decir, redacta una pequeña memoria explicando los pasos que has dado, los problemas que te has encontrado y cómo los has solventado.

