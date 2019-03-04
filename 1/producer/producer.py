import pika
import random
import time
import sys



sys.stderr.write("Producer started ==============================")

def main_loop():
	while True:
		channel = connection.channel() 
		channel.queue_declare(queue='hello')
		data = "{}".format(random.randint(1, 10000)) 
		channel.basic_publish(exchange='', 
			routing_key='hello',
			body=data.encode())
		time.sleep(2)

while True:
	try:
		pika_url = pika.ConnectionParameters('rabbitmq', 5672)
		# pika_url = pika.('amqp://guest:guest@rabbitmq:5672')
		connection = pika.BlockingConnection(pika_url)
	except Exception as e:
		sys.stderr.write(str(e))
		time.sleep(1)
	try:
		main_loop()
	except Exception as e:
		sys.stderr.write(str(e))
		time.sleep(1)