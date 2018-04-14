import pika
from pika import BlockingConnection


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


connection = BlockingConnection(pika.ConnectionParameters('odroid64'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print("[x] Sent 'Hello World!'")

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
