# coding: utf-8

import datetime
import iodef

from mail_sender import MailSender


msg = iodef.IODEF()
report_time = datetime.datetime.now()
report_id = 42

msg.set("formatid", "ip-blacklist-{0}".format(report_id))
msg.set("version", "1.00")
msg.set("lang", "fr")

msg.set("incident(0).purpose", "reporting")
msg.set("incident(0).restriction", "private")
msg.set("incident(0).incident_id.name", "exemple-iodef")
msg.set("incident(0).report_time", str(report_time))
msg.set("incident(0).description", "Liste d'IP connues malveillantes")

msg.set("incident(0).assessment.occurrence", "actual")
msg.set("incident(0).assessment.impact(0).type", "admin")
msg.set("incident(0).assessment.impact(0).completion", "succeeded")
msg.set("incident(0).assessment.impact(1).type", "recon")
msg.set("incident(0).assessment.impact(1).completion", "succeeded")

msg.set("incident(0).event_data(0).flow(0).system(0).category", "source")
msg.set("incident(0).event_data(0).flow(0).system(0).node.address(0).category", "ipv4-addr")
msg.set("incident(0).event_data(0).flow(0).system(0).node.address(0).address", "192.0.2.53")
msg.set("incident(0).event_data(0).flow(0).system(0).description", "Source de nombreuses attaques")
msg.set("incident(0).event_data(0).expectation.action", "contact-sender")

msg.set("incident(0).event_data(1).flow(0).system(0).category", "source")
msg.set("incident(0).event_data(1).flow(0).system(0).node.address(0).category", "ipv4-addr")
msg.set("incident(0).event_data(1).flow(0).system(0).node.address(0).address", "192.0.2.16")
msg.set("incident(0).event_data(1).flow(0).system(0).description", "Source de nombreux scan ce mois")
msg.set("incident(0).event_data(1).flow(1).system(0).category", "source")
msg.set("incident(0).event_data(1).flow(1).system(0).node.address(0).category", "ipv4-addr")
msg.set("incident(0).event_data(1).flow(1).system(0).node.address(0).address", "192.0.2.241")
msg.set("incident(0).event_data(1).flow(1).system(0).description", "Serveur IRC C2")
msg.set("incident(0).event_data(1).expectation.action", "block-host")

incident_file = 'incident-{0}-{1}-{2}.json'.format(str(report_time.date()),
                                                   report_time.time().strftime('%Hh%Mm'),
                                                   report_id)

with open(incident_file, 'w') as fd:
    fd.write(msg.toJSON())

mail_sender = MailSender('my.smtp.server', 42, 'noreply@my-siem.net')

subject = u"Rapport de sécurité"
message = u"""
Ceci est un mail automatique, merci de ne pas y répondre.

Vous trouverez ci-joint le dernier rapport d'incident de sécurité.
"""

mail_sender.send('myemail@mycie.net', subject, message, incident_file)
