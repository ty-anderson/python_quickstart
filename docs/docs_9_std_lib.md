# Notes on Standard Library

## IO package

[https://docs.python.org/3/library/io.html](https://docs.python.org/3/library/io.html)

The io module provides Python’s main facilities for dealing with various types of I/O. 
There are three main types of I/O: text I/O, binary I/O and raw I/O. 
These are generic categories, and various backing stores can be used for each of them. 
A concrete object belonging to any of these categories is called a file object. 
Other common terms are stream and file-like object.

Independent of its category, each concrete stream object will also have various 
capabilities: it can be read-only, write-only, or read-write. It can also allow 
arbitrary random access (seeking forwards or backwards to any location), or 
only sequential access (for example in the case of a socket or pipe).

Text I/O

Text I/O expects and produces str objects. This means that whenever the backing store 
is natively made of bytes (such as in the case of a file), encoding and decoding of 
data is made transparently as well as optional translation of platform-specific newline characters.

The easiest way to create a text stream is with open(), optionally specifying an encoding:

``f = open("myfile.txt", "r", encoding="utf-8")``

In-memory text streams are also available as StringIO objects:

``f = io.StringIO("some initial text data")``

StringIO is useful when you need to read or write data to a string buffer as 
if it were a file, rather than creating an actual file on disk. It can be 
used to create strings that mimic file objects, allowing you to read and 
write data to them in the same way you would with a file.

![bytesio.png](images/bytesio.png)

Binary I/O

Binary I/O (also called buffered I/O) expects bytes-like objects and produces bytes objects. 
No encoding, decoding, or newline translation is performed. This category of streams can 
be used for all kinds of non-text data, and also when manual control over 
the handling of text data is desired.

The easiest way to create a binary stream is with open() with 'b' in the mode string:

``f = open("myfile.jpg", "rb")``

In-memory binary streams are also available as BytesIO objects:

``f = io.BytesIO(b"some initial binary data: \x00\x01")``


## SMTP - Sending Emails

You can send emails directly through python using the simple mail transmission protocol.

```py
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = 'email@address.com'
msg['To'] = 'recipient@address.com'
msg['Subject'] = 'This is an Email'

msg.set_content('Body of email here.')

mailserver = smtplib.SMTP('smtp.office365.com', 587)  # connect to email service
mailserver.starttls()  # starts TLS (security protocol that encrypts data sent over the internet
mailserver.login(msg['From'], 'password')  # login to the email service account
mailserver.sendmail(msg['From'], msg['To'], msg.as_string())  # send the email
mailserver.quit()
```

Mail with attachment

```py
import os
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = 'email@address.com'
msg['To'] = 'recipient@address.com'
msg['Subject'] = 'This is an Email'

msg.set_content('Body of email here.')

file = 'path/to/file.txt'
extension = os.path.basename(file).split('.')[1]
with open(file, 'rb') as f:
    file_data = f.read()
msg.add_attachment(file_data, maintype='application', subtype=extension, filename=os.path.basename(file))

mailserver = smtplib.SMTP('smtp.office365.com', 587)  # connect to email service
mailserver.starttls()  # starts TLS (security protocol that encrypts data sent over the internet
mailserver.login(msg['From'], 'password')  # login to the email service account
mailserver.sendmail(msg['From'], msg['To'], msg.as_string())  # send the email
mailserver.quit()
```

You can also send nicely formatted HTML emails with MIME

```py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('mixed')
msg['From'] = 'email@address.com'
msg['To'] = 'recipient@address.com'
msg['Subject'] = 'Subject Here'

html_body = MIMEMultipart('alternative')

html_body_text = MIMEText('<html><div>HTML Content here</div></html>', 'html')
html_body.attach(html_body_text)

# Attach the multipart/alternative part to the multipart/mixed message
msg.attach(html_body)

# Remaining code for sending the email
mailserver = smtplib.SMTP('smtp.office365.com', 587)
mailserver.starttls()
mailserver.login(msg['From'], 'password here')
mailserver.send_message(msg)
mailserver.quit()
```
