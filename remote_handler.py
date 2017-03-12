#!/usr/bin/env python

import json
import os
import sys
import optparse

from auth_conn import Auth


class RemoteHandler(Auth):
    """Handler of remote connection."""

    def __init__(self, host, username, password, port):
        super(RemoteHandler, self).__init__(host,
                                            username,
                                            password,
                                            port)

    def command(self, args, outpath):
        """Define a command"""
        cmd = '%s %s' % (outpath, args)
        return self.exec_commands(cmd)

    def exec_commands(self, cmd):
        """Execution Command"""

        try:

            stdin, stdout, stderr = self.conn.exec_command(cmd)
        except Exception:
            raise

        results = stdout.read()
        return results

    def copy_module(self, sourcepath, destinationpath):
        """Upload file"""
        ftp = self.conn.open_sftp()
        ftp.put(sourcepath, destinationpath)
        ftp.close()
        return destinationpath

    def excutor(self, outpath, args):
        """execute command and get result"""

        result = self.command(args, outpath)
        result = json.dumps(result)
        return (self.host, result)


class RemoteResources():
    """define remote handler resources"""
    def __init__(self):
        self.host_list = self.get_host()
        self.command = self.get_command()

    def get_host(self):
        host_list = ['localhost', '127.0.0.1']
        return host_list

    def get_command(self):
        command_list = []
        try:
            input_file = sys.argv[1]
        except Exception as err:
            return command_list
        else:
            if not os.path.exists(sys.argv[1]):
                print "Sorry, %s is not exist" % sys.argv[1]
                sys.exit(1)
            with open(sys.argv[1]) as f:
                for command in f.readlines():
                    command_list.append(command)
                return command_list

    def interactive(self):
        count = 1
        while count:
            input = raw_input("[command]>> ")
            if not input:
                continue
            return input


def main(command, host_list):
    for host in host_list:
        handler = RemoteHandler(host,
                                username='xuxingzhuang',
                                password='root123.',
                                port=22)
        host, result = handler.excutor(command, '')
        print "%s: %s" % (host, result)


if __name__ == "__main__":
    remote_resource = RemoteResources()
    command_list = remote_resource.command
    host_list = remote_resource.host_list
    if not len(command_list):
        while 1:
            command = remote_resource.interactive()
            if command == 'quit' or command == 'exit':
                sys.exit(0)
            main(command, host_list)
    else:
        for command in command_list:
            main(command, host_list)
