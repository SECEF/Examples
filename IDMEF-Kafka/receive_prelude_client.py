#!/usr/bin/env python
# coding: utf-8

from pykafka import KafkaClient
import prelude

client_idmef = prelude.ClientEasy("MySensor")
client_idmef.start()

TOPIC_NAME = "Prelude_IDMEF"

client_kafka = KafkaClient(hosts="127.0.0.1:9092")
topic = client_kafka.topics[TOPIC_NAME]

consumer = topic.get_balanced_consumer(consumer_group='testgroup', auto_commit_enable=True, auto_commit_interval_ms=10000)

for message in consumer:
    if message is not None:
        idmef = prelude.IDMEF(message.value)
        client_idmef.sendIDMEF(idmef)
