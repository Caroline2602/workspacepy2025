import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class Mail:
    def __init__(self, smtp_server, port, user, password):
        self.smtp_server = smtp_server
        self.port = port
        self.user = user
        self.password = password

    def send_email(self, sender, recipient, subject, body, attachment=None):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment:
            attachment_name = attachment.split("/")[-1]
            with open(attachment, "rb") as attach_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attach_file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename= {attachment_name}')
                msg.attach(part)

        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.user, self.password)
            text = msg.as_string()
            server.sendmail(sender, recipient, text)
            server.quit()
            print(f"El reporte de ventas se envió a {recipient} desde {sender}")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")