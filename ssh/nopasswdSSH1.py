#!/usr/bin/python
# -*- coding: utf-8 -*-
#免密码登陆ssh，使用私钥。
#直接将私钥写在文本
#

import paramiko
import StringIO


ip = '192.168.56.142'
username = 'root'
port = 22

key_string = '''-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,E8A946E25B1ECDE4

aBKUdw0yoBF5QrYZx2Fn1La5KKxvEM97mMowaAjaekPTquRe+zaIWWQ/GAIrVhX8
F9luffARaaNAcyprrve9jvRHZ+sqL96QEfkMHy32wNruxYLizZ86GtJVkNlC/pku
erGMedv9eNF02bNRqYIHkSJyim653tgneb1YOaSDVXuV7EOCRyoFKkc293+iMntw
WdGJp+d45BbXxFP27p2sdk9GEp85lYb9s5IRn0m/CRRnA6uttrxcT/4bpfndK9qS
+GvxUzyHIRJCZXhHq5CrvyvTPaBB4qvfutdIEcmDdo7xqWBSEejKqVLxHSB//lEF
mzXsKm56IwRkcDWLM/oVOXTYuG+Cb5vDJP2GTv9uUJVqPyvtnNkDWTDW2Xb8ZLfz
LO0x3THN1kBsgw/P7nS0TmxbCBhD3PmCwQp33OJblY6G8fP9mywzLizUeun4znvi
a9g+giDGNvVE3rHahcoTjQaRMKtADx7dV0oCQpsF4dvkxZ9zpHMoXYKNbek9/Vg2
mYnpPtovJhWl3y3yR6cO12qHtBqpjF+0etRjkGCnvvGqjs7M7UpsX90JTkFSl1/H
d8Z6KBJn7yUjVzDbhg3nnv0R5luJ1xj8OHs3F8pBKymKyDx0FdlAy/6GFI6vHf+J
khv20yfuN+x05jc4roOPozYo67DJ38dApa/65Nus0rVyphV8hW/8MNwuhzouFd7M
FyRgVPekCVP7h/YGgQDTrNpagoLRLbwKi1FPxlPkxUuMKw9qEC4mfyA9+w2+WKy6
Vy84K2YkrMySJOD+tFLyK7odhu4q56YyNnBp3VfGPJuH8f7T/yQMnuJJIWHFZgoh
NTVf2p1rsBCM/M5U5YI0Ef2Gq3TNPU6fnXN2LkHLy1/aDDQwWHFn/tC2n1KCQ5gy
OFsG4hCt8f8prOnxoZQMRplIkIAt0b3gUsJ22zD6KoCCpWbCjsGbVRyzey0aZfg9
h0bOcNnvJoXkdL2km4UIDLbCsRckN/di8x/+vYmKuBCnlFsbbN3a2sKXLbBqH3yd
SR0sZUYHQLWF7CzlQrwSV1g/1aBhgclRrY5E35tgVi0MBsS1icQYiEVPM4LJD3j7
ZCDd0ETheFEEU7Ws8KxquykmTyOg7d4UVGNAc/BOnP2/jfoBYwO41AqDIz/ftqjE
vTDE45K4hr2WsPwGdk0xkglt2mAsFIZ30/o/Hb9penzU34wmjjAnMqR5KoHgmpkU
HS12PWlZqW3F6NI9N/FKIoD4SBo/JJDTgZAasb2DSlSN+WmdfGOnM58Z0BesnY7P
PjkgLSQyjuzG747A4KBd+xOI5sY6TJ7MZx2dVnD2ANIB0EDD03mG9MIjPE/T0NQi
47XifRwAA6BPVmpV0Z3PW2OReyJNFjRtOQpbrCjilslcy1joxor672u3HrV6RF8w
ZAd4IPA9zMt4prjLZ3LZHU0T4lV+M9mjlE4LUAG4PvT/scWRl4bxekk6dNVe/XDV
qs3LVRBxSX5TK8tIsVP/VNREruoVpf9q0g/L5ZndYKaE/fobWTBqmHONt9VsaGn5
GQXkIzPXFa9dwG6nZk5Gi/xZjNUevqpkALoCVXhyKGfU1/lOFXN3OQ==
-----END RSA PRIVATE KEY-----
'''

not_really_a_file = StringIO.StringIO(key_string)
# 带有解密密码的密钥
private_key = paramiko.RSAKey.from_private_key(not_really_a_file, password='20170217')

paramiko.util.log_to_file('ssh.log')

s = paramiko.SSHClient()

s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print "Starting"
s.connect(ip, port, username, pkey=private_key)
stdin, stdout, stderr = s.exec_command('ls -lh;echo '';ifconfig')

print stdout.read()
s.close()
not_really_a_file.close()
