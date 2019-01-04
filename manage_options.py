# !/usr/bin/python3

import optparse
import os
from output_functions import output


class user_options():
    """
    Manage user options given at script launch
    """
    def __init__(self, printer):
        self.printer = printer
        self.parser = self.create_parser()
        (options, arg) = self.parser.parse_args()
        self.host = options.host
        self.user = options.user
        self.passwd_file = options.passwd_file
        self.cmd_file = options.cmd_file

    def create_parser(self):
        """
        Create options parser object with an help text
        """
        parser = optparse.OptionParser(self.printer.BOLD + 'Usage: ' +
                                       self.printer.ENDC +
                                       'py3 ssh_hammer --host <HOST>\n' +
                                       '\t\t\t--user <USERNAME>\n' +
                                       '\t\t\t-f <passwdDictionnary>\n' +
                                       '\t\t\t--cmds <fileWithCmds>')
        parser.add_option('--host', dest='host', type='string')
        parser.add_option('--user', dest='user', type='string')
        parser.add_option('-f', dest='passwd_file', type='string')
        parser.add_option('--cmds', dest='cmd_file', type='string')
        return parser

    def check_options_validity(self):
        if (self.passwd_file is not None and
            self.is_valid_file(self.passwd_file) is False) or \
            (self.cmd_file is not None and
             self.is_valid_file(self.cmd_file) is False):
            exit()
        if (self.user_gave_all_necessary_options() is False):
            print(self.parser.usage)
            exit()

    def user_gave_all_necessary_options(self):
        if (self.host is None or
            self.user is None or
            self.passwd_file is None):
            return False
        return True

    def is_valid_file(self, f):
        if not os.path.isfile(f):
            self.printer.file_does_not_exist(f)
            return False
        elif not os.access(f, os.R_OK):
            self.printer.wrong_perm_on_file(f)
            return False
        return True
