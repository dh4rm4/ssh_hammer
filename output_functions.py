#!/usr/bin/env python3

class col:
    LOWRED      = '\033[94m'
    OKGREEN     = '\033[92m'
    YELLOW      = '\033[93m'
    FAIL        = '\033[91m'
    ENDC        = '\033[0m'
    BOLD        = '\033[1m'
    UNDERLINE   = '\033[4m'


###################################
#                                 #
#      Output functions           #
#                                 #
###################################

def printError():
    printFront('-', col.FAIL)
    print (col.FAIL + "Error" + col.ENDC + ': ', end='')

def printFront(c, color):
    print (col.BOLD + '[' + color + c + col.ENDC + col.BOLD + '] ' + col.ENDC, end='')

def printConnectFail(user, passwd):
    printFront('-', col.FAIL)
    print ('Fail connecting to host: ' + col.LOWRED + user + col.ENDC + ':' + col.FAIL + passwd + col.ENDC)

def fileDoNotExist(filename):
    printError()
    print (filename + " file does not exist")
    return 1

def wrongPermOnFile(filename):
    printError()
    print ("you don't have the right to read " + filename)

def printHello():
    print (col.BOLD + "\n\
                                            \`.     \n\
                  .--------------.___________) \         \n\
                  |" + col.LOWRED + '//////////////' +
           col.ENDC + col.BOLD + "|___________[ ]         \n\
                  `--------------'           ) (         \n\
                                            \\'-'/        " +
           col.ENDC)
    print (col.BOLD + col.FAIL + '                   	          HAMMER     SSH      \n' + col.ENDC)

def printSuccess(passwd, user):
    print ('\n')
    printFront('†', col.OKGREEN)
    print(col.BOLD + 'The SSH gate collapse' + col.ENDC)
    printFront('†', col.OKGREEN)
    print ('user: ' + col.BOLD + col.OKGREEN + user +
           col.ENDC + ' | password: \"' + col.BOLD +
           col.OKGREEN + passwd + '\"\n' + col.ENDC)

def printWhereFindOutput():
    print ("\n\n")
    printFront('!', col.LOWRED)
    print ("      " + col.BOLD + "OUTPUT IN: " + col.FAIL + col.UNDERLINE + "crackingResult.passwd" + col.ENDC)
