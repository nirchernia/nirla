import smtplib


def send_custom_email(recipient, custom_message):
 	
 	unicoded_custom_message = unicode(custom_message)
 	
 	
	TO = recipient
	SUBJECT = 'Invite Link'
	TEXT = unicoded_custom_message
	
	gmail_user = 'nirchernia@gmail.com'
	gmail_pwd = GMAIL_PWD
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (gmail_user, TO, SUBJECT, TEXT)
	#header = 'To:' + TO + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Invite Link \n\n'
	#print header
	print message
	
	
	
	#msg = header + unicoded_custom_message
	
	
	
	smtpserver.sendmail(gmail_user, TO, message)
	print 'done!'
	smtpserver.close()
	
	
	
	
	#notes:
	# previously the message was being constructed using a join on the TO and it still managed to work with some mail clients
	#", ".join(TO)