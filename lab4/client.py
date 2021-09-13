import pika
import time

dirIP = "54.89.9.125"
portID = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(dirIP, portID, "/", pika.PlainCredentials("user","password")))
channel = connection.channel()

channel.queue_declare(queue='my_app', durable=True)
print ('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))
    time.sleep(100)
    print (" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume("my_app",callback)

channel.start_consuming()
