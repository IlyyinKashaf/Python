import smtplib

email = 'testingmaail1234@gmail.com'
password = 'fxyqnwzydocvtdha'
recipient = 'ilyyinkashaf688@gmail.com'

message = """Subject: Test Email

Hello, this is a test email.
"""

try:
    # Connect to Gmail's SMTP server (port 587 for TLS)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade to secure connection
        server.login(email, password)
        server.sendmail(email, recipient, message)
        print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")