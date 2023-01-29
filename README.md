Blog de cine y serie creado con Django

El blong cuenta con: 3 Models : Peliculas - Series - Estrenos inicialmente se cargan los tres modelos con informacion de cada uno. -Se crean vistas para cada modelo. -Se crea una base de datos en SQL que contiene la informacion de los modelos. -Cada comodelo tiene un Formulario para ingresar datos a todos los atributos asignados. -Se crea un usuario para ADMING como un superusuario desde donde se ingrean datos, se craan usuarios y las autorizaciones pertientes a cada uno. -El blog cuenta con una función de BUSCAR por nombre de Pelicula en la pagina de peliculas. -Se crea un modelo BASE para HTML que heredan las demas vistas. -Cada vista tiene un Template con las caracteristicas particulares de la misma más la herencia base.
Se agregas las opciones de login, logout, registro de usuarios y editar datos de usuarios.
Cada modelo tiene la opcion para ver detalle, así como eliminar y editar para el cual deben estar registrados.
Se agraga un avatar  o foto para el perfil.
