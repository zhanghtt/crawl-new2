#!/usr/bin/env python
# -*- coding: utf-8 -*-
import paramiko, getpass
import socket


class Cluster(object):
    def __init__(self, ip2slaver_num={"192.168.0.117": 0, "192.168.0.113": 0}, username=None, port=22, master_host="192.168.0.117"):
        if not username:
            self.username = getpass.getuser()
        else:
            self.username = username
        self.master_host = master_host
        self.ip2slaver_num = ip2slaver_num
        self.port = port

    def start_all(self):
        pass

    def start_slaver(self):
        pass

    def start_master(self, is_background=True):
        #启动muster
        password = getpass.getpass("password:")
        self.ssh_exec(host_or_ip_user_passwd_tupe=(self.master_host,self.port, self.username, password), cmd="ls", is_background=is_background)

    def ssh_exec(self, host_or_ip_user_passwd_tupe, cmd, is_background=True):
        # SSH远程连接
        host_or_ip, host_port, user_name, password=host_or_ip_user_passwd_tupe
        ssh = paramiko.SSHClient()  # 创建sshclient
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
        ssh.connect(host_or_ip, host_port, user_name, password)

        if is_background:
            # 执行命令并获取执行结果
            ssh.exec_command(cmd)
            ssh.close()
        else:
            # 执行命令并获取执行结果
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.readlines()
            err = stderr.readlines()
            ssh.close()
            return out, err


if __name__ == "__main__":
    c = Cluster(hosts_or_ips=["192.168.0.117"])
    for i in c.start_master():
        print(i)



