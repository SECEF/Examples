#!/usr/bin/env python
# coding: utf-8

from pykafka import KafkaClient
import idmef


TOPIC_NAME = "Prelude_IDMEF"

client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics[TOPIC_NAME]

MSG = {"alert.analyzer(0).name": "AnalyzerExample",
       "alert.analyzer(0).manufacturer": "ACME",
       "alert.analyzer(0).class": "Authentification",
       "alert.analyzer(0).node.name": "centos7",
       "alert.analyzer(0).node.address(0).category": "ipv4-addr",
       "alert.analyzer(0).node.address(0).address": "192.168.1.2"}

with client.get_producer() as producer:
    msg = idmef.IDMEF()

    for key in MSG:
        msg.set(key, MSG[key])

    msg.set("alert.classification.text", "Remote Login")
    msg.set("alert.source(0).node.address(0).category", "ipv4-addr")
    msg.set("alert.source(0).node.address(0).address", "14.245.54.67")
    msg.set("alert.source(0).service.iana_protocol_number", "6")
    msg.set("alert.source(0).service.iana_protocol_name", "tcp")
    msg.set("alert.source(0).service.port", "12055")
    msg.set("alert.target(0).node.address(0).category", "ipv4-addr")
    msg.set("alert.target(0).node.address(0).address", "192.168.1.2")
    msg.set("alert.target(0).user.category", "os-device")
    msg.set("alert.target(0).user.user_id(0).type", "target-user")
    msg.set("alert.assessment.impact.severity", "medium")
    msg.set("alert.assessment.impact.completion", "failed")
    msg.set("alert.assessment.impact.type", "admin")
    msg.set("alert.assessment.impact.description", "Someone tried to login as root from 14.245.54.67 port 12055 using the password method")

    producer.produce(msg.toJSON())
