import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel();

channel.exchange_declare(exchange='logs', exchange_type='fanout')

for i in range(10):
    channel.basic_publish(exchange='logs', routing_key='', body='Hello World: ' + str(i))

connection.close()









