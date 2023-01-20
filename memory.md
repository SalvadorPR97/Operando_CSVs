# Memory

During the test, I found diferent problems to solve. I divided them according to the process:

### Script
The first problem was deciding the way to follow: using pandas, dictionaries, dictionaries with the id's as keys... Finally, I decided to last option so it's
easier to access using the keys.
Some problems were found but specially with the data type and sorting the dictionaries, searching in some webs and official documentation I could solve it.

### Testing
Consulting the official documentation and some webs, this part could be done without bigger problems.

### Api
The actual problem is the way of upload the csv files by url if you don't have the api in your system.
(WIP) Actually doesn't work rometely, I still working on it.

### Front
The bigger problem was trying to upload the files, they convert to "filestorage" type and make dificult to work with them. The solution was temporaly saving the files, wotking with them and deleting them at the end. For the download, I decided to make it in a zip file to make it easier for the user.

### Docker
It was my first time using DockerHub, so I followed the oficial documentation and some forum and I just had a little problem with the image's name to upload it.

The most important webs and videos y consulted to solve the problems can be found in the file [label](bibliography.txt).



# Memoria

Durante el desarrollo de la prueba se han encontrado diferentes problemas a los que se les ha buscado solución.
Al comienzo de la prueba se probó a hacerla por diferentes vías: usando pandas, usando diccionarios, diccionarios donde las keys sean los id's... 
y se decidió utilizar diccionarios con los id's como keys para poder acceder por las claves. Se han separado los problemas según el proceso:

### Script
Se encontraron varios problemas sobretodo con el tipo de dato y ordenar el diccionario, se solucionó buscando en diferentes webs y documentación oficial.

### Testing
Se consultó la documentación y algunas webs y se pudo realizar sin problemas mayores.

### Api
(WIP) No se ha conseguido actualmente que funcione de forma remota, se seguirá reuniendo información y testeando.

### Front
El principal problema ocurrió subiendo los archivos que se convertien en "filestorage" y dificultaba trabajar con ellos. Se pudo solucionar guardando los archivos
que se suben, trabajando con ellos y después eliminándolos. Para descargar los archivos se recurrió a descargarlos como un zip para comodidad del usuario.

### Docker
Al ser la primera vez utilizando DockerHub, hubo problemas creando la imagen para subirla al repositorio, se consultó la documentación oficial y algunos foros
para solucionarlo.

Las principales webs y videos consultados se pueden encontrar en el fichero [label](bibliography.txt)