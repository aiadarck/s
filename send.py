import os
import smtplib

# ÇØáÇÚÇÊ Ç˜ÇäÊ Çíãíá ÎæÏ ÑÇ æÇÑÏ ˜äíÏ.
USERNAME = 'soltani1997.mn@gmail.com'
PASSWORD = '0011121314Mn'

# ÇØáÇÚÇÊ ÏÑíÇİÊ ˜ääÏå íÇã ÑÇ æÇÑÏ ˜äíÏ.
TO = ['soltanihpi@gmail.com']

# ãÓíÑ İÇíá ÏíÊÇÈíÓ ÑÇ æÇÑÏ ˜äíÏ.
FILEPATH = '/path/to/x-ui.db'

# ÍĞİ İÇíá ŞÈáí¡ ÇÑ æÌæÏ ÏÇÑÏ
if os.path.exists(FILEPATH):
    os.remove(FILEPATH)

# ÇÌÑÇí ÏÓÊæÑ SQL ÈÑÇí ÏÑíÇİÊ ÇØáÇÚÇÊ ÇÒ ÏíÊÇÈíÓ æ ĞÎíÑå ÏÑ İÇíá
os.system(f'sqlite3 {FILEPATH} ".dump" > dump.sql')

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ÇØáÇÚÇÊ Ç˜ÇäÊ Çíãíá ÎæÏ ÑÇ æÇÑÏ ˜äíÏ.
USERNAME = 'soltani1997.mn@gmail.com'
PASSWORD = '0011121314Mn'

# ÇØáÇÚÇÊ ÏÑíÇİÊ ˜ääÏå íÇã ÑÇ æÇÑÏ ˜äíÏ.
TO = ['soltanihpi@gmail.com']

# ãÓíÑ İÇíá ÏíÊÇÈíÓ ÑÇ æÇÑÏ ˜äíÏ.
FILEPATH = '/path/to/x-ui.db'

# ÇíÌÇÏ íæÓÊ
with open(FILEPATH, 'rb') as f:
    file_data = f.read()
    file_name = 'x-ui.db'

# ÇíÌÇÏ Çíãíá
message = MIMEMultipart()
message['From'] = USERNAME
message['To'] = ', '.join(TO)
message['Subject'] = 'Database File'

# ÇÖÇİå ˜ÑÏä íÇã Èå ÕæÑÊ plain-text æ íæÓÊ İÇíá ÏíÊÇÈíÓ
message.attach(MIMEText('Please find attached the database file.'))
attachment = MIMEText(file_data, 'sqlite3')
attachment['Content-Disposition'] = f'attachment; filename="{file_name}"'
message.attach(attachment)

# ÇÑÓÇá Çíãíá ÈÇ ÇÓÊİÇÏå ÇÒ ÓÑæÑ SMTP Gmail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(USERNAME, PASSWORD)
server.sendmail(USERNAME, TO, message.as_string())
server.quit()

print('Email sent successfully.')