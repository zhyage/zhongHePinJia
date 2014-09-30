# -*- coding:utf-8 -*-
from scipy import *
import numpy as np


def guangYiZhiShuFaWuLiangGangHuaConv(srcLine, dstLine, biaoZhunZhi, zhengZhiBiao):
    # k = x/b, x = k * b
    if '0' == zhengZhiBiao:
        for i in range(0, srcLine.size):
            dstLine[i] = srcLine[i] / biaoZhunZhi
    else:
        for i in range(0, srcLine.size):
            dstLine[i] = biaoZhunZhi / srcLine[i]


def zhengZhiBiaoNiZhiBiaoPrompt():
    result = True
    print "ZhengZhiBiao or NiZhiBiao ?"
    print "0 ZhengZhiBiao"
    print "1 NiZhiBiao"
    ZhengZhiBiaoRes = raw_input("please select :")
    if ZhengZhiBiaoRes.strip() != '0' and ZhengZhiBiaoRes.strip() != '1':
        print "invalid ZhengZhiBiao NiZhiBIao option"
        return False, 0
    else:
        return True, ZhengZhiBiaoRes
