import paramiko

# Thông tin đăng nhập SSH
hostname = '103.110.32.71'
port = 9900
username = 'htb'  # Tên người dùng SSH
password = 'your_password'  # Mật khẩu SSH

# Tạo kết nối SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)

# Gửi lệnh và nhận kết quả
stdin, stdout, stderr = client.exec_command('ls -l')
output = stdout.read().decode('utf-8')
error = stderr.read().decode('utf-8')

# In kết quả
if output:
    print('Kết quả:')
    print(output)
if error:
    print('Lỗi:')
    print(error)

# Đóng kết nối SSH
client.close()
