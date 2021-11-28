# LAB 0 -  CREAR AWS EMR CLAUSTER


## Prerrequisitos

 - claves ssh de AWS EC2
 

## GUIA

 - Crear s3 bucket (usar solo letras minusculas en el nombre)

Crear AWS EMR:
		
 - Entramos a AWS **EMR** 
 - Seleccionamos **crear clúster** 		
 - Vamos a opciones avanzadas 		
 - Seleccionamos la version **emr-6.3.1**
 - Seleccionamos las siguientes aplicaciones para nuestro clúster:
   Sqoop 1.4.7, Hive 3.1.2, Hue 4.9.0, Spark 3.1.1, JupyterHub 1.2.0,
   Zeppelin 0.9.0, Tez 0.9.2, Livy 0.7.0, HCatalog 3.1.2
 - Habilitamos hive table metadata y spark table metadata en AWS GLUE data catalog
 - Añadimos la sigiente configuración en software settings para
   guardar nuestros jupyter notebooks y luego continuamos con los
   valores por default:

		[ {
        "Classification": "jupyter-s3-conf",
        "Properties": {
            "s3.persistence.enabled": "true",
            "s3.persistence.bucket": "s3bucketname"
        }}]
		
	

 - En redes y hardware cambiamos el hardware de las instacias hacia
   m4.xlarge y seleccionamos la opcion spot, continuamos
  

 - Le damos un nombre a nuestro clúster y seleccionamos el par de claves
   ssh anteriormente creadas y pulsamos crear clúster, debemos esperar alrededor de 25 min para la creacion de nuestro clúster



![image](https://user-images.githubusercontent.com/35736499/143790242-b1964d9d-febf-457b-9390-7beeba1b0adf.png)
