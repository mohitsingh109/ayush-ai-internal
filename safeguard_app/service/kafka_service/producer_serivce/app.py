from kafka import KafkaProducer
import random
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', retries=5) # connection with broker

for _ in range(100):
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    # pull data from twelve data
    # some calculation on window

    record = {
        "symbol": random.choice(symbols),
        "open": random.randint(1, 100),
        "high": random.randint(1, 100),
        "low": random.randint(1, 100),
        "close": random.randint(1, 100),
        "name":"ABC"
    }

    json_str = json.dumps(record)
    json_str = json_str.encode("utf-8")
    producer.send('stock_values', json_str) # Async call



producer.flush() # please push all the message to broker if not done
producer.close()