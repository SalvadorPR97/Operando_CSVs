# Resume Maker
## Onestic Backend Test

I developed a script that allows, having three csv files called "customers.csv", "products.csv" y "orders.csv" and with columns names predefined, get
another three csv files with more information about our customers.

We can find four executables:

### Script:
For it works, we need to have the three files in a subfolder called "csv" with the correct names ("customers.csv", "products.csv" y "orders.csv") or introduce
by the terminar the absolute route where you can find the files. After executing it, you can find the new files in the same route where the "main.py" is.


### Testing:
We can find in the root route the files for testing different situations, we can check if the dictionaries are well built or if the result that we get in the
final files are correct. We just have to execute by terminal the file "test.py" having the original csv files in the subfolder "csv".


### Api:
Actually, its function es similar to the script, but we can give the csv files by the url writing its name followed by "/" in the following order: "customers.csv", "products.csv" y "orders.csv" having the file in the same route than "main.py". (WIP) Still working to make the api works by remote.


### Front:
The app has been developed using Flask. With this app, you can upload easier your csv files, you need to upload them in the correct order that is specified in
top of the input and click in the "download" button. If everything is okay with files, the download of a zip file with the new csv files will start.
The app is dockerized so you can run it in another system, you can find it making pull to the next route: xalvix/resume-maker. 
The command to execute the image is: docker run -p 5000:5000 xalvix/resume-maker



# Resume Maker
## Prueba Onestic Backend

Se ha desarrolado un script que permite, pasándole tres ficheros csv llamados "customers.csv", "products.csv" y "orders.csv" y con unas columnas predefinidas, obtener otros tres ficheros csv con datos que relacionan los ficheros entre sí.

Tenemos 4 ejecutables:

### Script:
Para que este funcione, tendremos que tener los ficheros en una subcarpeta llamada "csv" con los nombres adecuados("customers.csv", "products.csv" y "orders.csv")o bien, introducir en la terminal la ruta absoluta donde se encuentran los archivos. Tras la ejecución, los ficheros los encontraremos en la ruta donde tenemos el main.py.

### Testing:
Podemos encontrar en el directorio raiz los ficheros de test con los que realizar distintas comprobaciones, desde ver si se cargan los ficheros correctamente hasta si los resultados son los esperados. Tendremos que ejecutar por terminal el fichero test.py teniendo los ficheros csv en una subcarpeta llamada "csv".

### Api:
Actualmente, su función es similar al script, pero los ficheros los pasaremos a url por su nombre seguidos de "/" en el orden: "customers.csv", "products.csv" y "orders.csv" teniéndolos en la misma ruta que el main.py. (Aún en desarrollo) Se está trabajando para que funcione de forma remota.

### Front:
Se trata de una app desarrollada con Flask para más comodidad a la hora de aportar los archivos, solo tendrá que respetarse el orden que aparece especificado encima de cada input y hacer click en el boton de download. Si todo está bien con los archivos, empezará la descarga de un fichero zip con los tres ficheros csv resultantes. 
La app está dockerizada para poder ejecutarla en cualquier sistema, la imagen la podemos encontrar haciendo pull al siguiente enlace: xalvix/resume-maker. 
El comando para ejecutar la imagen sería: docker run -p 5000:5000 xalvix/resume-maker



