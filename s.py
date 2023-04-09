
import os
import subprocess

# گرفتن مسیر فایل از کاربر
file_path = '/etc/ssh/sshd_confi'

# باز کردن فایل و دریافت محتوای فعلی آن
with open(file_path, "r") as f:
    file_content = f.read()

# دریافت متن جدید از کاربر و افزودن آن به ابتدای محتوای فایل
new_text = 'Port 2222'
file_content = new_text + file_content

# نوشتن محتوای جدید به فایل
with open(file_path, "w") as f:
    f.write(file_content)

# باز کردن فایل با ویرایشگر nano و ذخیره فایل با زدن کلید اینتر
subprocess.call(["nano", file_path])
