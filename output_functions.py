#!/usr/bin/env python3
"""
Class used to manage all output messages
"""


class output():
    LOWRED = '\033[94m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


    def hello(self):
        """
        Welcoming ascii art
        """
        print(self.BOLD + "\n\
                                            \`.     \n\
                  .--------------.___________) \         \n\
                  |" +
              self.LOWRED +
              '//////////////' +
              self.ENDC +
              self.BOLD + "|___________[ ]         \n\
                  `--------------'           ) (         \n\
                                            \\'-'/        " +
              self.ENDC)
        print(self.BOLD + self.FAIL +
              '                   	          HAMMER     SSH      \n' +
              self.ENDC)

    # General ouputs
    def print_front(self, c, color):
        print(self.BOLD + '[' + color + c + self.ENDC +
              self.BOLD + '] ' + self.ENDC, end='')

    def print_error(self):
        self.print_front('-', self.FAIL)
        print(self.FAIL + "Error" + self.ENDC + ': ', end='')

    # File checks
    def file_does_not_exist(self, filename):
        self.print_error()
        print(filename + " file does not exist")
        return 1

    def wrong_perm_on_file(self, filename):
        self.print_error()
        print("you don't have the right to read " + filename)

    # Bruteforcing ouputs
    def no_passwd_to_try(self, filename):
        self.print_front('-', self.FAIL)
        print('{0} is an empty file'.format(filename),
              self.ENDC)

    def success(self, passwd, user):
        print('\n')
        self.print_front('†', self.OKGREEN)
        print(self.BOLD + 'The SSH gate collapse' + self.ENDC)
        self.print_front('†', self.OKGREEN)
        print('user: ' + self.BOLD + self.OKGREEN + user +
              self.ENDC + ' | password: \"' + self.BOLD +
              self.OKGREEN + passwd + '\"\n' + self.ENDC)

    def connection_failed(self, user, passwd):
        self.print_front('-', self.FAIL)
        print('Fail connecting to host: ' + self.LOWRED +
              user + self.ENDC + ':' + self.FAIL + passwd +
              self.ENDC)

    def printWhereFindOutput(self):
        print("\n\n")
        self.print_front('!', self.LOWRED)
        print("      " +
              self.BOLD +
              "OUTPUT IN: " +
              self.FAIL +
              self.UNDERLINE +
              "crackingResult.passwd" +
              self.ENDC)
