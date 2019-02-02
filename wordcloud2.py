# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 21:55:14 2019

@author: Zhe Xu
"""

import jieba.analyse

path = 'D:\\weiboSpider-master\\weibo\\2407533890.txt'
file_in = open(path, 'rb')
content = file_in.read()

try:
    jieba.analyse.set_stop_words("D:\\weiboSpider-master\\zxmtingyongci.txt")
    tags = jieba.analyse.extract_tags(content, topK=50, withWeight=True)
    for v, n in tags:
        #权重是小数，为了凑整，乘了一万
        print (v + '\t' + str(int(n * 10000)))

finally:
    file_in.close()