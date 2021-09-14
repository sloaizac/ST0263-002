
import pika
import sys
import constants

dirIP = constants.SERVER_ADDRESS
portID = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(dirIP, portID, "/", pika.PlainCredentials("user","password")))
channel = connection.channel()

channel.queue_declare(queue='my_app', durable=True)

message = ' '.join(sys.argv[1:]) or "default task"
channel.basic_publish(exchange='my_exchange',
                      routing_key='test',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2,
                      ))
print (" [x] Sent %r" % (message,))
connection.close()
