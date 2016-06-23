#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
处理.srt 字幕文件，生成 Utf-8编码的.conv 文件
.conv 文件是一个对话的记录。

.conv 格式
一行表示一个单边语句，一个对话由来回的多个行组成。在每个行的开头做标记，M 表示话语，E 表示分割。
E
M 话语 a
M 话语 b
M 话语 c
M 话语 d
E
M 话语 a
M 话语 b
M 话语 c
M 话语 d
E
'''

import sys
import re
import chardet
import jieba



reload(sys)
sys.setdefaultencoding("utf-8")


def srttime(time):
    '''00:03:27,061  这种结构 返回毫秒单位的时间'''
    t = time.strip()
    ts = t.split(',')
    r = 0
    r = r + int(ts[1])
    ts = ts[0].split(':')
    r = r + 1000 * (int(ts[0]) * 3600 + int(ts[1]) * 60 + int(ts[2]))
    return r

def cvgen(fn, fno):
    print fn, fno
    with open(fn, 'r') as fp:
        all = fp.read()
        dec = chardet.detect(all)['encoding']
        print dec

        cc = []
        with open(fn, 'r') as fp2:
            cc = fp2.readlines()

        cc = [c.decode(dec) for c in cc]

        print 'lines', len(cc)

        # unicode begin
        tmp = []
        items = []
        for l in cc:
            if len(l) <= 2:
                if len(tmp) >= 3:
                    items.append(tmp)
                tmp = []

            else:
                tmp.append(l)

        print 'cps', len(items)
        cps = []
        for item in items:
            cp = {}
            cp['t'] = item[1]
            cp['c'] = item[2]
            cps.append(cp)

        for cp in cps:
            pass
            #print cp['t']


        #去掉带有这些关键字的条目
        dirty_keys = [u'字幕', u'时间轴', u'压缩', u'翻译', u'后期', u'监制', u'上集', u'<', u'>', u'=', u'【', u'[', u'*', u'■']

        ncps = []
        for cp in cps:
            good = True
            for k in dirty_keys:
                if k in cp['c']:
                    good = False
                    break
            if good:
                ncps.append(cp)

        print "ncps", len(ncps)


        currt = -1000000


        ret = []
        cnt = 0

        for cp in ncps:
            ts = cp['t'].split(u'-->')
            startt = srttime(ts[0])
            endt = srttime(ts[1])


            SPLIT_INTERVAL = 1000
            if cnt < 2:
                SPLIT_INTERVAL = 5000
            elif cnt < 3:
                SPLIT_INTERVAL = 2000

            if startt - currt > SPLIT_INTERVAL:
                #new conv
                ret.append(u'E\n')
                cnt = 0

            ret.append(u'M ' + cp['c'])
            cnt = cnt + 1
            currt = endt

        #拆分 --aaaaaaaa  --bbbbbb 这种同行但是多句的
        nret = []
        for r in ret:
            if u'-' in r:
                cs = (r[1:-1]).split(u'-')
                for c in cs:
                    a = c.strip()
                    if len(a) >= 2:
                        nret.append("M "+a+"\n")

            else:
                nret.append(r)


        #分词
        nnret = []
        
        for r in nret:
            if len(r) >= 3:
                d = r[2:]

                #ww = jieba.cut(d, cut_all=False)
                ww = [w for w in d]
                #ww = [w.strip() for w in ww]
                nl = '/'.join(ww[:-1])
                nnret.append("M "+nl+"\n")
            else:
                nnret.append(r)

        with open(fno, 'w') as fpo:
            for r in nnret:
                fpo.write(r.encode('utf-8'))



if __name__ == "__main__":

    usage = 'USAGE  ./cvgen.py target.srt output.conv'
    if len(sys.argv) != 3:
        print usage
        exit()


    cvgen(sys.argv[1], sys.argv[2])
