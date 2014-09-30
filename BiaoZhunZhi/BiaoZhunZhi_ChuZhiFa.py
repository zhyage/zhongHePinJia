# -*- coding:utf-8 -*-
from scipy import *
import numpy as np
from GuangYiZhiShuFaCommon import guangYiZhiShuFaWuLiangGangHuaConv
from GuangYiZhiShuFaCommon import zhengZhiBiaoNiZhiBiaoPrompt


def BiaoZhunZhi_ChuZhiFa(matrix, wuLiangMatrix, arrayNum, argsList):
    print "execute BiaoZhunZhi_ChuZhiFa"
    lineArr = matrix[arrayNum, :]
    wuLiangLineArr = wuLiangMatrix[arrayNum, :]
    zhengZhiBiao = argsList[0]
    firstOrLast = argsList[1]
    biaoZhunZhi = 0.0
    # print lineArr

    if '0' == firstOrLast:
        biaoZhunZhi = lineArr[0]
    else:
        biaoZhunZhi = lineArr[-1]

    guangYiZhiShuFaWuLiangGangHuaConv(lineArr, wuLiangLineArr, biaoZhunZhi, zhengZhiBiao)


def BiaoZhunZhi_ChuZhiFa_Prompt_function(sheet):
    returnArgList = []
    res, zhengZhiBiao = zhengZhiBiaoNiZhiBiaoPrompt()
    if True == res:
        returnArgList.append(zhengZhiBiao)
    else:
        return False, []
    print "first is the ChuZhi or Last is the ChuZhi ?"
    print "0 first"
    print "1 last"
    firstOrLast = raw_input("please select :")
    if firstOrLast.strip() != '0' and firstOrLast.strip() != '1':
        print "invalid argument"
        return False, []

    returnArgList.append(firstOrLast.strip())

    return True, returnArgList
