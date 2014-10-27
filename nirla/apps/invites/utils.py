import smtplib


def send_custom_email(recipient, custom_message):
 
	to = recipient
	gmail_user = 'nirchernia@gmail.com'
	gmail_pwd = ''
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
	print header
	
	
	
	msg = header + custom_message
	smtpserver.sendmail(gmail_user, to, msg)
	print 'done!'
	smtpserver.close()