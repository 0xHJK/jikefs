#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def tree():
    return defaultdict(tree)

def ls(t):
    pass


def cd(t, args):
    pass


def mkdir(t, args):
    pass

if __name__ == '__main__':
    t = tree()
    pwd = ''
    while True:
        line = raw_input().strip()
        if not line:
            break
        words = line.split()
        cmd = words[0]
        if len(words) == 2:
            args = words[1]
        if cmd == 'ls':
            ls(t, pwd)
        elif cmd == 'cd':
            pwd = cd(t, args)
        elif cmd == 'mkdir':
            mkdir(t, args)
        else:
            print('error')
            break


