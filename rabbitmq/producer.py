import pika

QUEUE_NAME = "mailbox"

with pika.BlockingConnection() as connection:
    channel = connection.channel()
    channel.queue_decalre(queue=QUEUE_NAME)
    while True:
        