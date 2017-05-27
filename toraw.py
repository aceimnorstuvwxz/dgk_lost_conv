#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
处理.conv 文件，变成纯粹的 txt 文件 ，无行头。
'''

import sys
import re
import chardet


reload(sys)
sys.setdefaultencoding("utf-8")

def toraw(fn, fno):

    with open(fn, 'r') as fp:
        lines = fp.readlines()
        fpo = open(fno, 'w')

        for l in lines:
            if len(l) > 3:
                fpo.write(l[1:])

        fpo.close()


if __name__ == "__main__":

    usage = 'USAGE  ./toraw.py fn fno'
    if len(sys.argv) != 3:
        print usage
        exit()

    toraw(sys.argv[1], sys.argv[2])
    print 'DONE'
