#!/usr/bin/env python

import paramiko
import six
import re


PARAMIKO_LOG = '/var/log/check_file/check_file.log'
HOSTS_PATH = '/etc/hosts'


class Auth(object):
    """Auth for connection."""

    def __init__(self, host_ipaddr, username, password, port):
        self.host = host_ipaddr
        self.conn = self._get_connect(port, username, password)

    def _get_connect(self, port, username, password):
        """Get ssh connect object."""
        paramiko.util.log_to_file(PARAMIKO_LOG)
        ssh_obj = paramiko.SSHClient()
        ssh_obj.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh_obj.connect(self.host, port, username=username,
                            password=password,
                            allow_agent=True)
        except Exception as err:
            print "Can't access node %s, detailed error as %s" % (
                host,
                six.text_type(err))
        return ssh_obj
