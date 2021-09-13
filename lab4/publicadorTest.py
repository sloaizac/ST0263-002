import pika

dirIP = "54.89.9.125"
portIP = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(dirIP, portIP, '/', pika.PlainCredentials('user', 'password')))
channel = connection.channel()
numTask = input("Número de la tarea: ")
channel.basic_publish(exchange='my_exchange', routing_key='test', body='El numero de la tarea es: ' + numTask)

print(f"Numéro de tarea {numTask} enviada con éxito")
#print("Runnning Producer Application...")
#print(" [x] Sent 'Hello World...!'")

connection.close()
