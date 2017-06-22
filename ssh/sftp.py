#!/usr/bin/python
# -*- coding: utf-8 -*-
#基于nopasswdSSH2.py,sftp
import paramiko
import StringIO

# t = paramiko.Transport("192.168.56.142", "22")
# t.connect(username="root", password="Inteplay007",)
# sftp = paramiko.SFTPClient.from_transport(t)
# remotepath = '/var/log/yum.log'
# localpath = 'yum.log'
# sftp.get(remotepath, localpath)
# t.close()


def ssh_connect_key(hostname, port, username, keyfile, keypassword, execmd):
    # a password to use for authentication or for unlocking a private key
    private_key = paramiko.RSAKey.from_private_key(keyfile, password=keypassword)
    paramiko.util.log_to_file('ssh.log', level=10)
    s = paramiko.SSHClient()
    s.load_system_host_keys()

    #允许连接不在know_hosts文件中的主机
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #ssh.load_system_host_keys()
    s.connect(hostname, port, username, pkey=private_key)
    t = s.get_transport()
    sftp = paramiko.SFTPClient.from_transport(t)  #新建一个SFTPClient对象，该对象复用之前的SSH连接,不需要再次进行用户认证。

    # 下载
    sftp.get("/var/log/dmesg", "dmesg")
    # 上传
    # d = sftp.put("G:\\SoftWare\\System\\CentOS\\CentOS-7-x86_64-DVD-1611.iso", "/tmp/CentOS-7-x86_64-DVD-1611.iso")


    stdin, stdout, stderr = s.exec_command(execmd)
    #stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    print stdout.read()
    s.close()

def main():
    #hostname = '182.16.45.146'
    hostname = '192.168.56.142'
    port = 22
    username = 'inteplay'

    #密钥的密码
    passwd = '20170217'
    execmd = 'df -h'
    #execmd = '/home/yetugeng/shell/a.sh'

    # 使用with as结构，可以自动关闭打开的文件,加载私钥。
    with open("id_rsa", "r") as f:
        text = f.read()

    # StringIO经常被用来作为字符串的缓存，应为StringIO有个好处，他的有些接口和文件操作是一致的，也就是说用同样的代码，可以同时当成文件操作或者StringIO操作。
    not_really_a_file = StringIO.StringIO(text)

    print("\n")
    print "=======Starting======"
    ssh_connect_key(hostname, port, username, not_really_a_file, passwd, execmd)
    not_really_a_file.close()
    print "=======Ending======"

if __name__ == "__main__":
    main()