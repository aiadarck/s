import os
import smtplib

# ������� ǘ��� ����� ��� �� ���� ����.
USERNAME = 'soltani1997.mn@gmail.com'
PASSWORD = '0011121314Mn'

# ������� ������ ����� ���� �� ���� ����.
TO = ['soltanihpi@gmail.com']

# ���� ���� ������� �� ���� ����.
FILEPATH = '/path/to/x-ui.db'

# ��� ���� ���� ǐ� ���� ����
if os.path.exists(FILEPATH):
    os.remove(FILEPATH)

# ����� ����� SQL ���� ������ ������� �� ������� � ����� �� ����
os.system(f'sqlite3 {FILEPATH} ".dump" > dump.sql')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ������� ǘ��� ����� ��� �� ���� ����.
USERNAME = 'soltani1997.mn@gmail.com'
PASSWORD = '0011121314Mn'

# ������� ������ ����� ���� �� ���� ����.
TO = ['soltanihpi@gmail.com']

# ���� ���� ������� �� ���� ����.
FILEPATH = '/path/to/x-ui.db'

# ����� �����
with open(FILEPATH, 'rb') as f:
    file_data = f.read()
    file_name = 'x-ui.db'

# ����� �����
message = MIMEMultipart()
message['From'] = USERNAME
message['To'] = ', '.join(TO)
message['Subject'] = 'Database File'

# ����� ���� ���� �� ���� plain-text � ����� ���� �������
message.attach(MIMEText('Please find attached the database file.'))
attachment = MIMEText(file_data, 'sqlite3')
attachment['Content-Disposition'] = f'attachment; filename="{file_name}"'
message.attach(attachment)

# ����� ����� �� ������� �� ���� SMTP Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(USERNAME, PASSWORD)
server.sendmail(USERNAME, TO, message.as_string())
server.quit()

print('Email sent successfully.')