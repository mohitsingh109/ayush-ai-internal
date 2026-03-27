from kafka import KafkaProducer
import random
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', retries=5, acks="all") # connection with broker

for _ in range(100):

    # pull data from twelve data
    # some calculation on window

    record = {
      "analysis": 9565964
    }

    json_str = json.dumps(record)
    json_str = json_str.encode("utf-8")
    producer.send('stock_analysis', json_str) # Async call



producer.flush() # please push all the message to broker if not done
producer.close()