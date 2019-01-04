#/usr/bin/env py3

from output_functions import output
from manage_options import user_options
from ssh_hammer import bruteforce_ssh


if __name__ in '__main__':
    printer = output()
    printer.hello()

    given_options = user_options(printer)
    given_options.check_options_validity()

    my_job = bruteforce_ssh(given_options.host,
                           given_options.user,
                           given_options.passwd_file)
    my_job.start_bruteforcing()
