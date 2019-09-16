#! /usr/bin/python3

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen

import re
import smtplib

# setup login credentials

# Settings

# from_address = Write the email address you want the email to be sent from ( example@gmail.com inside the quotes )

# to_address = Write the email address you want the email to be sent to (example@gmail.com inside the quotes)

# If you want to be sent to the same address you can put the same address to from_address and to_address

# Subject = Write the Subject you want the email to have

# Username = Write the username to be used as login at the gmail. For example for GMAIL the username is the same email address as the own you wrote at from_address 

# Password = Write the password that you have to login at the email

from_address = 'Write Your Email Address'
to_address = 'Write your email address'
subject = 'Subject of Email'
username = 'Username or Email to Log in'
password = 'Password to Login'

# Check WAN IP address
url = 'http://checkip.dyndns.org'

# Open URL and read the contents
request = urlopen(url).read().decode('utf-8')

# Extract IP address
ourIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", request)
ourIP  = str(ourIP)

# Function to send Email
def send_email(ourIP):
	#Body of email
	body_text =  ourIP # the body of the email
	msg = '\r\n'.join(['To: %s' % to_address,
			   'From: %s' % from_address,
			   'Subject: %s' % subject,
			   '', body_text]) # Initialize the message
	#Send email
	server = smtplib.SMTP('smtp.gmail.com:587') # Open server
	server.ehlo() # Send identification to server
	server.starttls() # Our security for transmission of credentials
	server.ehlo() # Send identification to server
	server.login(username,password) # Login to server
	server.sendmail(from_address, to_address, msg) # Send email 
	server.quit() # Log out and quit the session

# Change the directory to where you keep the last_ip.txt file
with open('/home/pi/Desktop/Check-IP/last_ip.txt', 'rt') as last_ip:
	last_ip = last_ip.read() # Read the text file with old WAN IP and compare

# Check if IP is changed
if last_ip  != ourIP: 
	# change path to where you keep the last_ip.txt file
	with open('/home/pi/Desktop/Check-IP/last_ip.txt', 'wt') as last_ip:
		last_ip.write(ourIP)
	send_email('WAN IP changed to' + ourIP) # send email if IP is different
