import pika
import datetime
import time
import sys

sys.stderr.write("Consumer started ==============================")

def start_consuming():
	channel = connection.channel()
	channel.queue_declare(queue='hello')             
	def callback(ch, method, properties, body):
		now_time = datetime.datetime.now().timestamp()                 
		recieved = (body.decode())                 
		recieved_time = float(recieved)                 
		print("{} : {}".format(
			now_time-recieved_time,
			recieved)
			)             
	channel.basic_consume('hello', callback )             
	channel.start_consuming()

while True:
	try:
		pika_url = pika.ConnectionParameters('rabbitmq', 5672)
		#pika_url = pika.URL('amqp://rabbitmq:5672')
		connection = pika.BlockingConnection(pika_url)
	except Exception as e:
		sys.stderr.write(str(e))
		time.sleep(1)
	try:
		start_consuming()
	except Exception as e:
		sys.stderr.write(str(e))
		time.sleep(1)