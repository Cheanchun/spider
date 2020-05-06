import argparse
import os
import sys

import redis

argparse.ArgumentParser().parse_args()
r = redis.Redis(host='47.105.54.129', port=6388, db=2, password='admin')
print(r.hgetall('hash'))
print(r.delete('hash', '1', '3c'))


def do_sth():
    print('do sth')


def restart_program():
    print("restart")
    python = sys.executable
    os.execl(python, './Intelligent_text_parse.py', *sys.argv)


if __name__ == '__main__':
    for i in range(100):
        if i == 5:
            break
    restart_program()
