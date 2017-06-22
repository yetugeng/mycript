#!/usr/bin/python
# -*- coding:utf-8 -*-
import paramiko



def sshclient_execmd(hostname, port, username, execmd):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #AutoAddPolicy():Policy for automatically adding the hostname and new host key to the local HostKeys object, and saving it. This is used by SSHClient.

    keyfile = './intemars.pub'
    pubkey = paramiko.RSAKey.from_private_key_file(keyfile)

    #s.connect(hostname=hostname, port=port, username=username, password=password)
    s.connect(hostname=hostname, port=port, username=username,pkey=pubkey)

    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.

    print stdout.read()

    s.close()


def main():
    hostname = '192.168.56.142'
    port = 22
    username = 'root'
    password = 'Inteplay007'
    # shell_file = open('shell_file.txt', 'r')
    # try:
    #     all_the_text = shell_file.read()
    #
    # finally:
    #     shell_file.close()

    execmd = '''df -h;free
    /usr/sbin/ip ad
    date'''

    sshclient_execmd(hostname, port, username, execmd)

    # file_write = file("out/username.xml","w+")
    # file_write.writelines(file_rec)
    # file_write.close()


if __name__ == "__main__":
    main()
