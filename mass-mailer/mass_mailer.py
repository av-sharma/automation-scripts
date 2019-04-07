import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename

### Initial Values
# csv file name
csvFile = '####.csv'

# your email id
fromaddr = "#######@gmail.com"

# CC address
ccaddr = "#######@gmail.com"

# your password
password = "########"

# subject of the mail
subject = "subject"

success = 0
failed = 0
with open(csvFile, 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        try:
            toaddr = row[0]
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['CC'] = ccaddr

            msg['Subject'] = subject;

            body = """
            	### BODY OF THE MESSAGE IN HTML FORMAT
            """.format(var1=name, var2=chapter, var3=number)
            msg.attach(MIMEText(body, 'html'))

            # List of files to attach if any
            files = []
            for f in files:
                with open(f, "rb") as file:
                    part = MIMEApplication(file.read(), Name=basename(f))
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, password)
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            print ("Successfully sent email to ", row[0])
            success = success + 1
        except smtplib.SMTPException:
            print ("Failed to send email to ", row[0])
            failed = failed + 1
total = success + failed
print(success, " emails sent out of ", total)
print("Failed to send ", failed, " emails")
