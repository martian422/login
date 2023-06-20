from UCASSrunLogin.LoginManager import LoginManager

# -*- coding: UTF-8 -*-


import sys
import getopt


def main(argv):

    _username_ = ""
    _password_ = ""

    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["help", "username=", "password="])
    except getopt.GetoptError:
        print('Error: test_arg.py -u <username> -p <password>')
        print('   or: test_arg.py --username=<username> --password=<password>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('test_arg.py -u <username> -p <password>')
            print('or: test_arg.py --username=<username> --password=<password>')
            sys.exit()
        elif opt in ("-u", "--username"):
            _username_ = arg
        elif opt in ("-p", "--password"):
            _password_ = arg
    print('username:', _username_)

    for i in range(0, len(args)):
        print('parameter %s is %s' % (i + 1, args[i]))

    lm = LoginManager()
    lm.login(
        username = _username_,
        password = _password_
    )

    print('You can use logout.py to log out.')


if __name__ == "__main__":

    main(sys.argv[1:])
