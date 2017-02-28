#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def tree():
    return defaultdict(tree)

def ls(t, args):
    dirs = args.split('/')
    for d in dirs:
        if d:
            t = t[d]
    for k in t.keys():
        print(k)

def cd(t, args):
    pass


def mkdir(t, args):
    pass

if __name__ == '__main__':
    t = tree()
    t['a']['b']['c'] = 'zxc'
    t['a']['e']['f'] = 'bmn'
    pwd = 'a/'
    while True:
        line = input().strip()
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


