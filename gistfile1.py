#!/usr/bin/env python
#vim: encoding=utf-8

"""
拼音分词
"""

__author__ = "dreampuf<soddyque@gmail.com>"

import unittest
import cPickle as pickle
from collections import defaultdict
from pprint import pprint

tree = lambda : defaultdict(tree)

py = set([u'gu', u'qiao', u'qian', u'ge', u'gang', u'ga', u'lian', u'liao', u'rou', u'zong', u'tu', u'seng', u'ti', u'te', u'ta', u'nong', u'zhang', u'fan', u'tuan', u'gua', u'die', u'gui', u'guo', u'gun', u'sang', u'diu', u'tei', u'zi', u'ze', u'za', u'chen', u'zu', u'ruo', u'dian', u'diao', u'nei', u'suo', u'sun', u'zhao', u'sui', u'kuo', u'kun', u'kui', u'zhai', u'zuan', u'kua', u'bo', u'ning', u'lei', u'neng', u'men', u'mei', u'geng', u'chang', u'shua', u'cha', u'che', u'fen', u'chi', u'fei', u'chu', u'shui', u'me', u'ma', u'mo', u'mi', u'mu', u'dei', u'cai', u'zhan', u'cao', u'can', u'den', u'wang', u'beng', u'zhuang', u'tan', u'tao', u'tai', u'eng', u'song', u'ping', u'hou', u'cuan', u'\u0148g', u'lan', u'lao', u'fu', u'fa', u'jiong', u'mai', u'xiang', u'mao', u'fo', u'a', u'jiang', u'kuang', u'bing', u'su', u'si', u'sa', u'se', u'zan', u'm\u0300', u'xuan', u'zei', u'zen', u'kong', u'pang', u'le', u'jia', u'jin', u'lo', u'lai', u'li', u'peng', u'lu', u'yi', u'yo', u'ya', u'cen', u'dan', u'dao', u'ye', u'din', u'cei', u'zhen', u'jiu', u'bang', u'nou', u'yu', u'weng', u'wong', u'en', u'ei', u'kang', u'dia', u'er', u'ru', u'keng', u're', u'ren', u'gou', u'ri', u'she', u'tian', u'tiao', u'que', u'shi', u'shun', u'shuo', u'qun', u'xue', u'yun', u'xun', u'fiao', u'yue', u'ding', u'zao', u'rang', u'xi', u'yong', u'zai', u'guan', u'guai', u'dong', u'kuai', u'ying', u'kuan', u'xu', u'xia', u'xie', u'yin', u'rong', u'xin', u'tou', u'nian', u'niao', u'xiu', u'man', u'kou', u'niang', u'hua', u'chao', u'hun', u'huo', u'hui', u'shuan', u'quan', u'shuai', u'chong', u'bei', u'ben', u'dang', u'sai', u'ang', u'sao', u'san', u'reng', u'ran', u'rao', u'ming', u'l\u01dc', u'l\u01da', u'l\u01d8', u'lie', u'lia', u'min', u'miao', u'mian', u'mie', u'liu', u'zou', u'miu', u'nen', u'kai', u'kao', u'kan', u'dai', u'ka', u'ke', u'yang', u'ku', u'deng', u'dou', u'shou', u'chuang', u'nang', u'feng', u'meng', u'cheng', u'di', u'de', u'da', u'gei', u'du', u'gen', u'qu', u'shu', u'sha', u'\u1e3f', u'ban', u'bao', u'bai', u'nun', u'nuo', u'sen', u'kei', u'fang', u'teng', u'lun', u'luo', u'ken', u'wa', u'wo', u'ju', u'tui', u'wu', u'jie', u'ji', u'huang', u'tuo', u'cou', u'la', u'mang', u'ci', u'tun', u'tong', u'ca', u'pou', u'ce', u'gong', u'cu', u'dui', u'dun', u'duo', u'ting', u'qie', u'yao', u'yan', u'pi', u'po', u'suan', u'chua', u'chun', u'\u0148', u'chui', u'gao', u'gan', u'ao', u'gai', u'xiong', u'tang', u'n', u'pian', u'piao', u'cang', u'heng', u'xian', u'xiao', u'bian', u'biao', u'zhua', u'duan', u'cong', u'zhui', u'zhuo', u'zhun', u'hong', u'shuang', u'juan', u'zhei', u'pai', u'shai', u'shan', u'shao', u'pan', u'pao', u'nin', u'nia', u'hang', u'\u01f9g', u'nie', u'zhuai', u'mou', u'zhuan', u'yuan', u'niu', u'zhong', u'qi', u'lin', u'guang', u'nao', u'n\u01d8', u'n\u01da', u'n\u01dc', u'hai', u'han', u'hao', u'wei', u'wen', u'ruan', u'cuo', u'cun', u'cui', u'bin', u'bie', u'l\xfce', u'shen', u'shei', u'fou', u'xing', u'\u0144g', u'qia', u'qiang', u'nuan', u'pen', u'pei', u'\u01f9', u'rui', u'run', u'ba', u'sheng', u'rua', u'bi', u'bu', u'chuan', u'qing', u'chuai', u'pu', u'o', u'chou', u'ou', u'zui', u'luan', u'zuo', u'jian', u'jiao', u'sou', u'wan', u'jing', u'qiong', u'wai', u'long', u'pa', u'liang', u'lou', u'huan', u'hen', u'hei', u'huai', u'n\xfce', u'\u0144', u'jue', u'shang', u'jun', u'hu', u'hm', u'ling', u'ha', u'he', u'zhu', u'ceng', u'zha', u'zhe', u'zhi', u'qin', u'pin', u'ai', u'chai', u'chan', u'pie', u'zeng', u'an', u'qiu', u'ni', u'na', u'zang', u'nai', u'nan', u'ne', u'ng', u'chuo', u'tie', u'you', u'nu', u'zheng', u'leng', u'zun', u'zhou', u'lang', u'e', u'hng'])

def pinyin_sub_gen(nodes, s, v):
    for p, sub_node in nodes.iteritems():
        for sub in pinyin_sub_gen(sub_node, p, v):
            if s == p:
                yield sub
            else:
                yield [v[s:p]] + sub
    yield []

def pinyin_split(pinyin):
    root = tree()
    node = root[0]
    nodes = [(0, node)]

    while nodes:
        new_nodes = []
        for pos, node in nodes:
            for p in py:
                py_len = len(p)
                if pinyin[pos:pos+py_len] == p:
                    new_nodes.append((pos+py_len, node[pos+py_len]))
        nodes = new_nodes

    #pprint(root)
    candidates = list(pinyin_sub_gen(root, 0, pinyin))
    candidates = sorted(candidates, key=lambda x: len(x), reverse=True)
    return candidates[0]

class TestCase(unittest.TestCase):
    def test_pinyin_dp(self):
        v = "woshidewenfensi"
        pprint(pinyin_split(v))
        v = "woaibeijinganmen"
        pprint(pinyin_split(v))

if __name__ == "__main__":
    unittest.main()