# Check_IP

Check the WAN (Public IP) of your network, and notify if it changes via email. 
Save your current WAN IP at the last_ip.txt file in order for the script to be able to compare for changes. 
You can use the crontab to execute the file every hour or every half an hour. See more [here](https://www.raspberrypi.org/documentation/linux/usage/cron.md).

## Required

1. Python 3.6 or newer
2. re package
3. os package
4. smtplib package

You can install python packages from the command line with:
```

pip install package_name

Example

pip install urlib2

```

## Instructions for Settings

- from_address = Write the **email address** you want the email to be **sent from** (example@gmail.com inside the quotes).

- to_address = Write the **email address** you want the email to be **sent to** (example@gmail.com inside the quotes).

***If you want to be sent to the same address you can put the _same address_ to from_address and to_address.***
***You must allow your gmail account to trust third party application (Check if you have enabled trust less security apps***

- Subject = Write the Subject you want the email to have.

- Username = Write the username to be used as login at the gmail. For example for GMAIL the username is the same email address as the own you wrote at from_address.

- Password = Write the password that you have to login at the email.

- Change the directory to where you keep the last_ip.txt file
