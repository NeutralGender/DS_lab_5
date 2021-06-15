import pika, sys, os

QUEUE_SIZE = 5

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel();

    channel.queue_declare(queue='hello', durable=True)

    # receive function
    def callback(ch, method, properties, body):
        channel.queue_declare(queue='response')
        channel.basic_publish(exchange='', routing_key='response', body=body + b' response', properties=pika.BasicProperties(delivery_mode=2))
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
    
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
