# Laboratorio 4 - MOM

Para este laboratorio vamos a implemetar una cola sencilla utilizando rabbitMQ y una instancia de EC2 en AWS, la guia para el setup del lab esta en esta carpeta con la nombre de guide.pdf


# Cola de tareas

Al realizar el setup de nuestro lab, hemos creado consumidorTest.py y publicadorTest.py para testear nuestro MOM, ahora en la carpeta tambien podemos ver taskGenerator.py y client.py con el cual tenemos una app sencilla para publicar tareas a n clientes para eso solo debemos ejecutar el taskGenerator.py para generar nuestras tareas y client.py para consumirlas tal y como lo hicimos en el test
