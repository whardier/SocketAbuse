#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""SocketAbuse"""

import sys
import argparse
import logging

import socketabuse

import tornado
import redis

################################################################################
## ┏┳┓┏━┓╻┏┓╻
## ┃┃┃┣━┫┃┃┗┫
## ╹ ╹╹ ╹╹╹ ╹

def main():

    parser = argparse.ArgumentParser(
        description=socketabuse.__description__,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-v',
        dest='verbose',
        action='count',
        help='add multiple times for increased verbosity'
    )

    subparsers = parser.add_subparsers(title='Command', dest='command')

    client_parser = subparsers.add_parser('client',
        help='Client Mode',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    client_parser.add_argument('listenuri',
        action='store',
        help='tcp://host[:port]',
        metavar='LISTENURI'
    )

    client_parser.add_argument('redisuri',
        action='store',
        help='tcp://host[:port]',
        metavar='REDISURI'
    )

    client_parser.add_argument('uri',
        action='store',
        help='tcp://host[:port]',
        metavar='URI'
    )

    server_parser = subparsers.add_parser('server',
        help='Server Mode',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    server_parser.add_argument('listenuri',
        action='store',
        help='tcp://host[:port]',
        metavar='LISTENURI'
    )

    server_parser.add_argument('redisuri',
        action='store',
        help='tcp://host[:port]',
        metavar='REDISURI'
    )

    server_parser.add_argument('uri',
        action='store',
        help='tcp://host[:port]',
        metavar='URI'
    )

    args = parser.parse_args()

    loglevel = logging.CRITICAL

    if args.verbose >= 4:
        loglevel = logging.DEBUG
    elif args.verbose == 3:
        loglevel = logging.INFO
    elif args.verbose == 2:
        loglevel = logging.WARNING
    elif args.verbose == 1:
        loglevel = logging.ERROR

    logging.basicConfig(level=loglevel)

    clilogger = logging.getLogger('CLI')

    for arg, value in vars(args).iteritems():
        clilogger.debug('%s:%s' % (arg, value))

    clilogger.info('Arguments Parsed.. moving along.')

    if args.command == 'server':
        clilogger.info('Server Mode')
    elif args.command == 'client':
        clilogger.info('Client Mode')
    else:
        clilogger.error('Interesting... I should not have been called.')

if __name__ == '__main__':
    sys.exit(main())
