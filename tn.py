#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
紧接着 tr.py。
tn.py 负责对 句子 
1，分词
2，标记拼音（假）
3，标记音素

限制0-499 余下的丢弃

TODO 分词的粒度可能需要更小  社会保险-》社会，保险
'''

import sys,re
import jieba

reload(sys)
sys.setdefaultencoding("utf-8")


#分词
def replace_fuhao(l):
    '''只剩中文，留下空格'''
    a= re.findall(u"([\u4e00-\u9fff]+)", l)
    return " ".join(a)


def fenci(ucc):
    rr = []
    for l in ucc:
        t = replace_fuhao(l)
        ww = jieba.cut(t, cut_all=False)
        ww = [w.strip() for w in ww]
        nl = ' '.join(ww)
        
        rr.append(nl)
        
    return rr

#音素
dict = {}


def load_lexicon_dict():
	with open('lexicon.txt', 'r') as fp:
		cc = fp.readlines()
		cc = [c.decode('utf-8') for c in cc]
		for c in cc :
			k = c.find(' ')
			k, v= c[0:k], c[k+1:-1] #-1去掉换行
			dict[k] = v
	
def phoneme(w):
	'''给一个词寻找 phoneme'''
	if dict.has_key(w):
		return dict[w].strip()
	r = u''
	for c in w:
		r = r + dict[c] + ' '
	
	return r.strip()

def mark_phoneme(l):
    r = u''
    ww = l.split(u' ')
    for w in ww:
        r = r + phoneme(w) + u' '
    return r.strip()



def gen(fn, prefix):
    with open(fn, 'r') as fp:
        cc = fp.readlines()
        
        ucc = [c.decode("utf-8") for c in cc]
        
        #unicode start
        
        ucc = fenci(ucc)
        fucc = [mark_phoneme(c) for c in ucc]
        

        #unicode end
        cc = [c.encode("utf-8") for c in ucc]
        fcc = [c.encode("utf-8") for c in fucc]
        
        
        for c, fc in zip(cc, fcc):
            print c,fc
        
        print 'Total=%d'%len(cc)
        
        cnt = 0
        for c,fc in zip(cc,fcc):
            if cnt > 499:
                break
            with open(prefix + "_" + str(cnt) + ".trn", "w") as fpo:
                fpo.write(c+"\n")
                fpo.write(fc+"\n")
                fpo.write(fc+"\n")
            cnt = cnt + 1

            
        
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "usage: tn.sh fn prefix"
        sys.exit()
        
    print sys.argv[1], sys.argv[2]
    
    load_lexicon_dict()
    
    gen(sys.argv[1], sys.argv[2])
