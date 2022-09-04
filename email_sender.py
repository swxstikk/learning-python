import smtplib

"""

Store your email credentials below
Go to your google account settings -> generate login token
Paste the login token in the 'email_password' variable'.

WARNING: Do not let anyone else have access to this login token as it gives them full control
over your google account.

"""

email = "email@email.com"
email_password = "Password"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email, email_password)
    subject = "Auto-generated mail using Python"
    body = "This mail was sent from a Python script written by your_name"
    message = f"Subject:{subject}\n\n{body}"
    smtp.sendmail(email, "recipient@email.com", message)
