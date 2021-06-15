import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel();

# Create queue
channel.queue_declare(queue='task6')

for i in range(10):
    time.sleep(3)
    print("Producer send: " + 'Hello world: ' + str(i))
    channel.basic_publish(exchange='', routing_key='task6', body= 'Hello world: ' + str(i))

connection.close()
