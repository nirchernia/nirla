import smtplib


def send_custom_email(recipient, custom_message):
 
	to = recipient
	gmail_user = 'nirchernia@gmail.com'
	gmail_pwd = GMAIL_PWD
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Invite Link \n\n'
	print header
	
	unicoded_custom_message = unicode(custom_message)
	
	
	msg = header + unicoded_custom_message
	
	
	smtpserver.sendmail(gmail_user, to, msg)
	print 'done!'
	smtpserver.close()
	
	
	
	
	
	
	
