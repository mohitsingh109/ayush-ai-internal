from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='ayush',
) # connection to broker

consumer.subscribe(['stock_values_1'])

for message in consumer:
    record = message.value
    partition = message.partition
    key = message.key
    # read it from topic
    # do some post processing
    # create a DB connection
    # create record (Schema object) object using kafka message
    # store it to database table
    print(partition, key, record)
