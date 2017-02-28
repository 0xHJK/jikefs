#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from pyecho import echo

class Node(object):
    """docstring for DirNode"""
    def __init__(self, value, parent = None):
        super(Node, self).__init__()
        self.value = value
        self.parent = parent
        self._childs = []

    # 返回当前路径
    def get_pwd(self):
        n = self
        pwd = n.value
        while True:
            if not n.parent:
                break
            pwd = n.parent.value + '/' + pwd
            n = n.parent
        return pwd

    # 获取所有子节点名称
    def get_child_value(self):
        return [x.value for x in self._childs]

    # 根据索引获得单个子节点
    def get_child(self, idx):
        return self._childs[idx]

    def ls(self):
        for n in self._childs:
            echo.log(n.value)

    def add(self, n):
        if not isinstance(n, Node):
            n = Node(n)
        self._childs.append(n)
        n.parent = self

    def cd(self, args):
        n = self
        for v in args:
            if v == '.':
                continue
            elif v == '..':
                n = n.parent
            elif v in n.get_child_value():
                idx = n.get_child_value().index(v)
                n = n.get_child(idx)
            else:
                echo.error('Path is not exists')
                n = self
                break
        return n


# 生成模拟数据
def mock():
    rx = [2, 3, 5, 6, 4]
    chars = ['a', 'b', 'd', 'e', 'f', 'g']
    t = Node('')
    for x in rx:
        p = Node(random.choice(chars))
        t.add(p)
        for i in range(x):
            q = Node(random.choice(chars) + random.choice(chars))
            p.add(q)
    return t

def argv(line):
    words = line.split()
    cmd = words[0]
    if len(words) == 2:
        args = words[1].split('/')
    else:
        args = []
    return cmd, args


if __name__ == '__main__':
    # 随机生成模拟数据
    t = mock()
    while True:
        line = input().strip()
        if not line:
            break
        cmd, args = argv(line)
        if cmd == 'ls':
            tmp = t.cd(args)
            tmp.ls()
        elif cmd == 'cd':
            t = t.cd(args)
            echo.bright('Current Path: %s' % t.get_pwd())
        elif cmd == 'mkdir':
            t.add(args[0])
        elif cmd == 'pwd':
            echo.bright('Current Path: %s' % t.get_pwd())
        else:
            echo.error('error')


