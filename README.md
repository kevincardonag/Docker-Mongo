# Docker-Mongo

Autores:

Kevin Cardona Giraldo 1810032 ;
Santiago Guarin Aristizabal 1810045

Para poner en funcionamiento el proyecto, seguir los pasos:

1. Clonar el repositorio:

2. Entrar a la raiz de repositorio
   	 
3. Ejecute el comando: 
	
	- docker-compose up -d

4. ejecute el comando: 
	
	- docker exec -it docker_mongo mongo


NOTA:
	Para seleccionar la base de datos:
 
		- use articles

	Nombre de la colección:
	
	- db.articles_collection


** TERCERA ENTREGA - ENDPOINT CON FUSEKI **

	** PASO A PASO INICIARLIZAR FUSEKI ** (OPCIÓN 1) 
1) Instalar  la libreria  de java para ubuntu con el comandos:
	- sudo apt-get install default-jre
2) Entrar a la carpeta del repositorio:
 	- cd apache-jena-fuseki-3.10.0
3) Inicializar Fuseki con el archivo ttl que contiente la información del estudio del cancer:
	- ./fuseki-server --file=json-to-ttl.ttl /estudio-cancer
4) En el navegador ingresar a la url:
	- http://localhost:3030/dataset.html

	** USAR SCRIPT FUSEKI.SH ** (opción 2)

1) Otorgar permiso al archivo fuseki.sh:
	- chmod +x fuseki.sh
2) Ejecutar:
	- ./fuseki.sh
3) En el navegador ingresar a la url:
	- http://localhost:3030/dataset.html

** A CONTINUACIÓN PODREMOS  EJECUTAR LAS SIGUIENTES CONSULTAS **


