# IDMEF-Kafka

Cette preuve de concept utilise la libIdmef pour forger des messages IDMEF, les transporter au travers d'un Kafka pour les envoyer à Prelude OSS.

Nous partons du principe que tous les éléments sont installés et configurés:
* [Apache Kafka](http://davidssysadminnotes.blogspot.fr/2016/01/installing-apache-kafka-and-zookeeper.html)
* [Prelude OSS](https://www.prelude-siem.org/projects/prelude/wiki/InstallingPrelude)
* [LibIDMEF](https://github.com/Prelude-SIEM/libidmef)
* [PyKafka](https://pypi.python.org/pypi/pykafka) pour la manipulation du cluster Kafka depuis Python
