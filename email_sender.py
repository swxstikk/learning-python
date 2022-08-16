import smtplib

# Store your email credentials below

email = "email@email.com"
email_password = "Password"

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(email, email_password)
    subject = "Auto-generated mail using Python"
    body = "This mail was sent from a Python script written by your_name"
    message = f"Subject:{subject}\n\n{body}"
    smtp.sendmail(email,"recipient@email.com",message)
