import pika

QUEUE_SIZE = 5

def callback(ch, method, properties, body):
        print(" [x] Received from consumer %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel();

# Create queue
channel.queue_declare(queue='hello', durable=True)

for i in range(10):
    print("Producer send: " + 'Hello world: ' + str(i))
    channel.basic_publish(exchange='', routing_key='hello', body= 'Hello world: ' + str(i), properties=pika.BasicProperties(delivery_mode=2))

channel.queue_declare(queue='response')
channel.basic_consume(queue='response', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

connection.close()