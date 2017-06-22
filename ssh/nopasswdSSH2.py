#!/usr/bin/python
# -*- coding: utf-8 -*-
#免密码登陆ssh，使用私钥。
#直接导入私钥文件。

import paramiko
import StringIO

def ssh_connect_key(hostname, port, username, keyfile, keypassword, execmd):
    # 带有解密密码的密钥
    private_key = paramiko.RSAKey.from_private_key(keyfile, password=keypassword)
    paramiko.util.log_to_file('ssh.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()

    #允许连接不在know_hosts文件中的主机
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, pkey=private_key)

    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    print stdout.read()
    s.close()

def main():
    hostname = '192.168.56.142'
    port = 22
    username = 'root'

    #密钥的密码
    passwd = '20170217'
    execmd = '/home/yetugeng/shell/a.sh'

    # 使用with as结构，可以自动关闭打开的文件。
    with open("id_rsa", "r") as f:
        text = f.read()
    #print('私钥如下' + "\n" + text)

    # StringIO经常被用来作为字符串的缓存，应为StringIO有个好处，他的有些接口和文件操作是一致的，也就是说用同样的代码，可以同时当成文件操作或者StringIO操作。
    not_really_a_file = StringIO.StringIO(text)
    #print('文件缓存对象如下' + "\n")
    #print(not_really_a_file)

    print("\n")
    print "=======Starting======"
    ssh_connect_key(hostname, port, username, not_really_a_file, passwd, execmd)
    not_really_a_file.close()
    print "=======Ending======"

if __name__ == "__main__":
    main()



