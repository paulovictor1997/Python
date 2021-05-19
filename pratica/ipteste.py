import socket as s

host = 'google.com'
ip = s.gethostbyname(host)

print(f'O IP do host {host} é : {ip}')
