import pika
dirIP = "54.89.9.125"
portID = 5672

connection = pika.BlockingConnection(pika.ConnectionParameters(dirIP, portID, "/", pika.PlainCredentials("user","password")))
channel = connection.channel()
def callback(ch, method, properties, body):
        print(f'{body} is received')

channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)

channel.start_consuming()
