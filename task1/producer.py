import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel();

# Create queue
channel.queue_declare(queue='hello')

for i in range(10):
    print("Producer send: " + 'Hello world: ' + str(i))
    channel.basic_publish(exchange='', routing_key='hello', body= 'Hello world: ' + str(i))

connection.close()





